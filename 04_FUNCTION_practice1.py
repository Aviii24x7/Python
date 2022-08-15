''' LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
 if both numbers are even, but returns the greater if one or both numbers are odd'''


from unittest import result


def func2(a, b):

    if (a % 2 == 0 and b % 2 == 0) and a > b:
        return b
    elif (a % 2 == 0 and b % 2 == 0) and b > a:
        return a
    elif (a % 2 != 0 or b % 2 != 0) and b > a:
        return b
    elif (a % 2 != 0 or b % 2 != 0) and a > b:
        return a


x = int(input('enter the first num:'))
y = int(input('enter the second num:'))
result2 = func2(x, y)
print(result2)

# ORRRR!!!


def func1(a, b):
    if a % 2 == 0 and b % 2 == 0:
        result1 = min(a, b)
    else:
        result1 = max(a, b)
    return result1


x = int(input('enter the first num:'))
y = int(input('enter the second num:'))
ans = func1(x, y)
print(ans)
