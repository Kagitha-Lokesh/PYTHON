digit = input('Enter : ')
size=len(digit)
add=0
for i in range (size):
    num = int(digit[i]) ** size
    add=add+num

if int(digit) == add:    
    print ('Armstrong')
else:
    print('Not armstrong ')