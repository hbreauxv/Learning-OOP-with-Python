import json
import time
import requests

headers = {
    'X-CP-API-ID': '...',
    'X-CP-API-KEY': '...',
    'X-ECM-API-ID': '...',
    'X-ECM-API-KEY': '...',
    'Content-Type': 'application/json',
}


class SpeedTest(object):
    global headers

    def __init__(self, ids, host, account_id):
        # router ids you want to run the test on. Must be a list
        self.ids = ids
        # ip address of the NetPerf server you want to run the test against
        self.host = str(host)
        # your NCM account id
        self.account_id = account_id
        self.resource_uri = ''
        self.payload = {
            "account": "https://www.cradlepointecm.com/api/v2/accounts/{}/".format(self.account_id),
            "config": {
                "host": self.host,
                "max_test_concurrency": 5,
                "net_device_ids": self.ids,
                "port": 12865,
                "size": None,
                "test_timeout": 30,
                "test_type": "TCP Download",
                "time": 5
            }
        }

    def run_test(self):
        try:
            # post test payload
            r = requests.post('https://www.cradlepointecm.com/api/v2/speed_test/', headers=headers,
                              data=json.dumps(self.payload))
            # resource_uri is the url for the results of the speed test.
            self.resource_uri = r.json()["resource_uri"]
            print("Speed Test job posted.  This may take some time to complete. \nJob ID: {}".format(r.json()["id"]))
            print("Results url:" + self.resource_uri)
        except Exception as e:
            print(e)

    def get_results(self):
        try:
            # check to make sure a test was run
            if self.resource_uri == '':
                print("You haven't run a test yet! Use the run_test method.")
                return
            # get the results of the test that was run
            r = requests.get(self.resource_uri, headers=headers).json()

            # start a loop to check every 10 seconds until the test is complete
            while r["state"] != "complete":
                r = requests.get(self.resource_uri, headers=headers).json()
                if r["state"] == "started":
                    print("Job State: {} \n    Waiting 10 seconds and then checking again".format(r["state"]))
                    time.sleep(10)
                # if the test is complete, pretty print the json results
                elif r["state"] == "complete":
                    print("Job Completed.  Results:\n")
                    print(json.dumps(r["results"], indent=4, sort_keys=True))
        except Exception as e:
            print(e)


# RouterTestA = SpeedTest([1023423], '1.1.1.1', 11111)
# RouterTestA.run_test()
# RouterTestA.get_results()

# RouterTestB = SpeedTest([1023423, 5023421, 12305415], '1.1.1.1', 11111)
# RouterTestB.run_test()
# RouterTestB.get_results()
