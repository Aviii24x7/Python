'''ALMOST THERE:Given an integer n, return True if n is within 10 of either 100 or 200'''


def func(num):
    if abs(num-100 <= 10) or abs(num-200 <= 10):
        return True
    else:
        return False


print(bool(func(123)))

# unsolve problem
