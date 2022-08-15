'''Write a function that checks whether a number is in a given range (inclusive of high and low)'''

def ran(num,low,high):
    if num<=high and num>=low:
        return True
    else:
        return False

print(ran(4,5,12))