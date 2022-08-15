'''MAKES TWENTY:Given two integers, return True if the sum of the integers is 20 or 
if one of the integers is 20. If not, return False'''


def func(a, b):
    if a == 20 or b == 20 or (a+b) == 20:
        return True
    else:
        return False


c = int(input('the first no.:'))
d = int(input('the second no.:'))

result = func(c, d)
print(result)
