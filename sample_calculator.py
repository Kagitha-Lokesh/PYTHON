num_1=int(input("Enter First : "))
operator = input("Operation : ")
num_2=int(input("Enter Second : "))
if(operator=='+'):
    print(num_1+num_2)
elif(operator=='-'):
    print(num_1-num_2)
elif(operator=='*'):
    print(num_1*num_2)
elif(operator=='/'):
    print(num_1/num_2)
elif(operator=='%'):
    print(num_1%num_2)
elif(operator=='//'):
    print(num_1//num_2)
elif(operator==''):
    print(num_1**num_2)
else:print("Invalid")