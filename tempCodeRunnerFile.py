n=10
#Hollo Square
for i in range(n):
    if i==0 or i == n-1:
        print("* "*(n))
    else:
        print("* "+" "*((n-2)*2)+"*")
print("\n")
#Hollow Pyramid
for i in range(n):
    if i == n-1:
        print("* "*(n))
    else:
        if i==0:
            print(" "*(n-1)+"*")
        else:
            print(" "*(n-1-i)+"*"+"  "*(i-1)+" *")
print("\n")
#Hollow Reverse Pyramid
for i in range(n):
    if i == 0:
        print("* "*(n))
    else:
        if i==n-1:
            print(" "*(n-1)+"*")
        else:
            print(" "*i+"*"+"  "*(n-2-i)+" *")
print("\n")
#Hollow Right angle Triangle
for i in range(n):
    if i == n-1:
        print("*"*n)
    else:
        print("*"+" "*(i-1)+"*")
print("\n")
# for i in range(n):
#     if i == n-1:
#         print("*"*n)
#     else:
#         if i==0:
#             print(" "(n-1)+"")
#         else:
#             print(" "(n-1-i)+""+" "(i-1)+"")
            
# print("\n")
# for i in range(n):
#     if i == n-1:
#         print("*")
#     else:    
#         if i == 0:
#             print("*"*n)
#         else:
#             print(""+" "(n-2-i)+"*") 
# print("\n")
# for i in range(n):
#     if i == n-1:
#         print(" "(n-1)+"")
#     else:    
#         if i == 0:
#             print("*"*n)
#         else:
#             print(" "i+""+" "(n-2-i)+"")
# print ("\n")