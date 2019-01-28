#!/usr/bin/python
'''
MaxSizeList.py was a practice project where the assignment was to make a class of lists that are kept within a size
limit.  The max list size is set on a per instance basis, an all instances have a push method to add a value to the
list.
'''


# My first version creates a list filled with None objects.  The initial list is within size limits, and pushes
# simply append and then pop the first entry. This works, but having a list of [None, None, None] isn't really ideal.
# It'd be better to be able to make [] the initial list, and to have some data validation to ensure we don't go over the
# limit.
class SetSizeList(object):

    def __init__(self, size):
        self.list = []
        for i in range(size):
            self.list.append(None)

    def push(self, entry):
        self.list.append(entry)
        self.list.pop(0)

    def get_list(self):
        print(self.list)


# This is my second version.  It stores a "max_size" attribute on every instance, and every time you do a push it
# will pop entries until the list length equals the max_size. This lets us make lists that are below the max length,
# and it gives us built in validation whenever we do a push.
class ListSizeValidator(object):

    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def push(self, obj):
        self.list.append(obj)
        # the while loop gives the push method built in validation. We pop the first item until the list is within limit
        while len(self.list) > self.max_size:
            self.list.pop(0)


a = ListSizeValidator(7)
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print("Lets look at the list. We added 4 values but its staying within the size limit of {}".format(a.max_size))
print(a.list)

for i in range(a.max_size):
    a.list.append(a.list[-1] + 1)
print("After manually appeneding to a.list, the list is over the size limit.  Not good!")
print(a.list)

a.push(a.list[-1] + 1)
print("Our push method pops the first item from the list until it is within the limit.  After pushing a new value, "
      "the list is once again within the size limit we set")
print(a.list)