string = input('Enter : ')
found=False
for i in range (len(string)):
    if(string[i] == ' '):
        space = string[i]
        found=True
        break
if(found==True):
    string_1 = string[:i].strip()
    string_2 = string[i+1:].strip()
    string_1 = string_1.upper()
    rev_1 = string_1[-1::-1]
    string_2 = string_2.upper()
    rev_2 = string_2[-1::-1]
    if(string_1 == rev_1 and string_2 == rev_2):
        print('palindrome')
    else :
        print('Not a palindrome')
elif(found==False):
    string=string.upper()
    rev = string[-1::-1]
    if(string == rev):
        print('palindrome')
    else :
        print('Not a palindrome')