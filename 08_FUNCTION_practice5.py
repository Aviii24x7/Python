'''MASTER YODA:Given a sentence, return a sentence with the words reversed'''

from posixpath import split


def func(name):
    mylist = name.split()
    mylist2 = []
    for i in range(len(mylist)):
        mylist2.append(mylist[(len(mylist)-1-i)])
    return ' '.join(mylist2)


mystr = input('Enter the string:')


result = func(mystr)
print(result)

# _______OR!!!!!


def func(name2):
    list2 = name2.split()
    list2 = list2[::-1]
    return ' '.join(list2)


output = func('my name is aviiii')
print(output)
