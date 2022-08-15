'''REVERSE MULTIPLICATION TABLE'''

n = int(input('enter the number to get its reverse table:'))

for a in range(10, 0, -1):
    print(f"{n} * {a} = {n*a}")
