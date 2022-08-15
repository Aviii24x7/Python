'''OLD MACDONALD:Write a function that capitalizes the first and fourth letters of a name'''

# from ntpath import join


def func(name):
    text = []
    for i in range(len(name)):
        if i == 0 or i == 3:
            text.append(name[i].upper())
        else:
            text.append(name[i])
    return ''.join(text)


result = func('avinash')
print(result)

# _____OR!!!!!!


def newfunc(name2):
    first_letter = name2[0]
    inbetween = name2[1:3]
    fourthLetter = name2[3]
    afetrall = name2[4:]
    return first_letter.upper() + inbetween + fourthLetter.upper() + afetrall


ans = newfunc('Chauhan')
print(ans)

# _____OR!!!!!!!!


def funct(name3):
    fisrt_half = name3[:3]
    second_half = name3[3:]
    return fisrt_half.capitalize() + second_half.capitalize()


output = funct('macdonald')
print(output)
