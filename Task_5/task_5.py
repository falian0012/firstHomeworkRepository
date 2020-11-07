print('Enter the revenue value: ')
revenue = int(input())
print('Enter cost value: ')
cost = int(input())

if revenue > cost:
    print('profit')
    profitability = revenue / cost
    print(profitability)
elif revenue < cost:
    print('loss')
else:
    print('0')

print('Enter the number of employees: ')
numberOfEmployees = int(input())

profitForOneEmployee = (revenue - cost) / numberOfEmployees
print(profitForOneEmployee)
