'''STAR PATTERNS:

Problem1

        *
        * *
        * * * 
'''

for i in range(1, 4):
    print('*' * i)

'''Problem2

          *
        * * *
      * * * * *
'''

print('\n\n')


for j in range(3):  # j=0
    print(' ' * (3-j-1), end='')
    print('*' * ((2*j)+1), end='')
    print(' ' * (3-j-1))

'''Problem3

     * * *
     *   *
     * * *
'''

print('\n\n')

for k in range(3):
    for l in range(3):
        if(k == 0 or k == 2 or l == 0 or l == 2):
            print('*', end='')
        else:
            print(' ', end='')
    print('')


'''Problem4

   *********
   **** ****
   ***   ***
   **     **
   *       *
   **     ** 
   ***   ***
   **** ****
   *********
'''

print("\n\n")
num = int(input('enter the ODD no. of rows for the pattern:'))

if(num % 2 == 0):
    print('No Even num accepted!! \n ')
    num = int(input("ENTER THE ODD NUMBER:"))
else:
    pass
print('*'*num)

for a in range(int(num/2)):
    print('*'*(int(num/2)-a), end='')
    print(' '*(2*a+1), end='')
    print('*'*(int(num/2)-a))

for b in range(int(num/2)-1):
    print('*'*(2+b), end='')
    print(' '*(num-(4 + (2*b))), end='')
    print('*'*(2+b))

print('*'*num)
