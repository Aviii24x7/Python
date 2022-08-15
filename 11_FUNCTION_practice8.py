'''PAPER DOLL:Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'''


def paper_doll(name):
    mylist = list(name)
    newlist = []
    for i in range(len(mylist)):
        newlist.append(mylist[i]*3)
    return ''.join(newlist)


print(paper_doll('Hello'))

# ___________Orrrrr!!


def paper(name2):
    empty = ''
    for char in name2:
        empty = empty+char*3
    return empty


print(paper('mississippi'))
