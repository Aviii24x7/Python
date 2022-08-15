'''FIND 33:Given a list of ints, return True if the array contains a 3 next to a 3 somewhere'''


def func(mylist):
    # if we do not -1 then for last digit there will be no i+1 for
    for i in range(len(mylist)-1):
        if (mylist[i] == mylist[i+1] == 3):
            print(True)
        else:
            pass


list1 = [3, 3, 1, 2, 4, 5]
func(list1)
