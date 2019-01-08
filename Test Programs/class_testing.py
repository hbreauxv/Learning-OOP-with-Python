import random


# Random Character Constructor
class RandomCharacter(object):
    def __init__(self, name):
        self.job_choices = ["Developer", "Salesperson", "Support Engineer"]
        self.name = name
        self.job = random.choice(self.job_choices)
        self.weight = random.randint(100, 300)
        self.age = random.randint(18, 80)

    # print information about the character
    def about(self):
        print("{} is a {}, weighs {} pounds, and is {} years old.".format(self.name, self.job, self.weight, self.age))

    # change careers to something else
    def change_career(self):
        # make a new list of job choices that doesn't contain current job
        list_choice = [i for i in self.job_choices if i != self.job]
        self.job = random.choice(list_choice)
        print("{} changed their career to a {}".format(self.name, self.job))

    # exercise to reduce weight!
    def exercise(self):
        # integrity check: never exercise if below 50 pounds
        if self.weight > 50:
            weight_lost = random.randint(1, 5)
            self.weight = self.weight - weight_lost
            print("{} lost {} pounds and now weighs {} pounds".format(self.name, weight_lost, self.weight))
        else:
            print("{} is too frail to lose weight.".format(self.name))


Joe = RandomCharacter('Joe')
Jane = RandomCharacter('Jane')
Doug = RandomCharacter('Doug')

Joe.about()
Jane.about()
Doug.about()

Doug.change_career()
for i in range(50):
    Doug.exercise()
