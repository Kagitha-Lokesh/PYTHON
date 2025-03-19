days = int(input('enter n : '))
years = days//365
remainder1 = days % 365
weeks = remainder1//7
remainder2 = remainder1 % 7

print(years)
print(weeks)
print(remainder2)