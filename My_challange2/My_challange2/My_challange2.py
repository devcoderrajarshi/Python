total=int(input("Enter the amount of your total purchase\n"))
if total<50:
    total+=10
    print("Your total amount with Rs {0:f} shipping charges is Rs {1:f}\n".format(10,total))
else:
    print("Your total amount is {0:f}\n".format(total))
