'''PRINT BIG: Write a function that takes in a single letter, and 
returns a 5x5 representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
'''





star= {1: '*   *', 2: '*    ', 3:'  *  ', 4: '*****', 5:'* *  ', 6:' * * ',7:'**** ',8:' *   ', 9:'   * '}
letter= {'A':[3,6,4,1,1], 'B':[7,1,7,1,7], 'C':[4,2,2,2,4], 'D': [2,5,1,5,2], 'E': [4,2,4,2,4]}

def print_big(alpha):
    for x in letter[alpha.upper()]:
        print(star[letter])
print_big('a')
