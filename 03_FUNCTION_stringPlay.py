'''UP AND DOWN: uppercasing the even and loweercasing the odd indexes in a string'''


def myfunc(name):
    blank = []
    for i in range(len(name)):
        if i % 2 == 0:
            blank.append(name[i].upper())
        else:
            blank.append(name[i].lower())
    return ''.join(blank)


yo = input('enter the string:')
result = myfunc(yo)
print(result)
