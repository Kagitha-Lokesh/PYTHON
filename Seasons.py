month = int(input("Enter month number : "))
if month in [1 , 2 , 11 , 12]:
    print("Winter")
elif month in  [3 , 4]:
    print("Spring")
elif month in [5 , 6]:
    print("Summer")
elif month == [7 , 8 , 9 , 10]:
    print("Rainy")
else:
    print("Invalid input")