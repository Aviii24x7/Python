'''COUNT PRIMES: Write a function that returns the number of prime numbers that
exist up to and including a given number
count_primes(100) --> 25'''

def check_prime(value):
    for i in range(2,value):            
        if value % i == 0:
            return False
        else:
            continue
    return True

# print(check_prime())

def count_prime(nu):
    counter = 0                     
    for a in range(2,nu+1):
        
        if check_prime(a) == True:
            counter+=1
        else: 
            continue
    return counter

z=int(input("Enter the number:"))
print(f'the number of prime numbers are:{count_prime(z)}')


