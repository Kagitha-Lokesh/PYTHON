amount=int(input("Enter amount: "))
five_hundred_notes = amount//500
remaining_amount1 = amount % 500
hundred_notes = remaining_amount1//100
remaining_amount2 = remaining_amount1%100
fifty_notes = remaining_amount2//50
remaining_amount3 = remaining_amount2%50
ten_notes = remaining_amount3//10
remaining_amount4 = remaining_amount3%10
ones_notes = remaining_amount4//1
remaining_amount5 = remaining_amount4%1
print("Five Hundred Notes (500) : ",five_hundred_notes)
print("Hundred Notes (100) : ",hundred_notes)
print("Fifty Notes (50) : ",fifty_notes)
print("Ten Notes (10) : ",ten_notes)
print("One Rupee (1's) : ",ones_notes)