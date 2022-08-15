"""ANIMAL CRACKERS:Write a function takes a two-word string and 
returns True if both words begin with same letter """

def func1(text1):
    myList1 = text1.split()

    first = myList1[0]
    second = myList1[1]

    letter1 = first[0]
    letter2 = second[0]

    if letter1 == letter2:
        return True
    else:
        return False


result1 = func1('avi avinash')
print(result1)

# ORR!!!


def func2(text2):
    myList2 = text2.split()

    if myList2[0][0] == myList2[1][0]:
        return True
    else:
        return False


result2 = func2('avi avinash')
# a != A

print(result2)
