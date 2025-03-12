a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
if(a<b and a<c):
    print('a is smallest :',a)
elif(b<a and b<c):
    print('b is smallest :',b)
elif(c<a and c<b):
    print('c is smallest :',c)
elif(a==b and a<c):
    print("a & b are smallest : ",a)
elif(a==c and a<b):
    print("a & c are smallest : ",a)
elif(c==b and b<a):
    print("b & c are smallest : ",b)
elif(a==b==c):
    print('All are same.')
else:
    print('Invalid input')