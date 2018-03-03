country=input("Enter your country please\n")
amount=float(input("Enter the price of the product \n"))
tax=0.0
if country.upper()=="CANADA":
    province=input("Enter your province\n")
    if province.capitalize()=="Alberta":
        tax=(amount*0.05)
        print("The Genral Sales Tax(5%) is: ${0:.2f}".format(tax))
        
    elif province.capitalize()=="Ontario" or province.capitalize()=="New brunswick" or province.capitalize()=="Nova scotia":
        tax=(amount*0.13)
        print("The Harmonized Sales Tax(13%) is: ${0:.2f}\n".format(tax))
        
    else:
        tax=((amount*0.06)+(amount*0.05))
        print("the Total tax = Provincial Sales Tax(6%) + Genral Sales Tax(5%) is: ${0:.2f}\n".format(tax))
        
else:
     print("No tax charges are applied")         



print("The amount including of all taxes: ${0:.2f}".format(amount+tax))           