'''write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.'''

def count_case(str):
    up=0
    low=0
    for char in str:
        if char.isupper():
            up+=1
        elif char.islower():
            low+=1
    print(f'the number of uppercase letters are {up}')
    print(f'the number of lowercase letter are {low}')

count_case('My name is Avinash Chauhan AVIII')