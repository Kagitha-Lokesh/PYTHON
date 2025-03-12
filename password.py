password = input('Enter password : ')
special = ['!','@','#','$','%','^','&','*','(',')','-','=','+','[',']','{','}','|',':',';','"',"'",'<','>',',','.','/','?','_']
upper_case=lower_case=digit=spl=False
if(len(password)>=8):
    for i in password:
        if(i.isupper()):
            upper_case=True
        elif(i.islower()):
            lower_case=True
        elif(i.isdigit()):
            digit=True
        elif(i in special):
            spl=True
if(upper_case==lower_case==digit==spl==True):
    print('valid password')
else:
    print('Invalid password')