print('Enter number A: ')
numberA = int(input())
print('Enter number B: ')
numberB = int(input())

day = 1

while numberA <= numberB:
    day = day + 1
    numberA = numberA * 1.1

print(f'Result is {day}')