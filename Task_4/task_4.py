inputNumber = int(input())
max = 0

while inputNumber != 0:
    if inputNumber % 10 > max:
        max = inputNumber % 10
    inputNumber = inputNumber // 10

print(max)