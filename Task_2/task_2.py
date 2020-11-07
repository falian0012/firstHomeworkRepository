inputSeconds = int(input())

hours = inputSeconds // 3600
minuts = (inputSeconds - hours * 3600) // 60
seconds = inputSeconds - hours * 3600 - minuts * 60

print (f'{hours:02}:{minuts:02}:{seconds:02}')