#favouritefood=input("What is your favourite dish?")
#if favouritefood.capitalize()=="Biryani" :
#    print("You are a Bengali")
#print("It's okay if you are a south/north indian")


#deposit=float(input("Enter your amount"))
#if deposit>100:
#    print("get your gift from the counter")
#else:
#    print("ok")


#win=True
#bigwin=True

#if win and bigwin:
#    print("You can retire")
#else:
#    print("Enjoy your life")

# 'and' statement both should be correct to get correct


#team=input("Ener your fav hockey team").upper()   #upper is to take input as uppercase
#sport=input("Enter your fav sport").upper()

#if sport=="HOCKEY" and team=="RANGERS":
#    print("I miss Messier")
#else:
#    print("I don't know that team")



# 'or' statement any one can be correct  to get correct

#dog=False
#cat=False

#if dog or cat:         
#    print("I have one")
#else:
#    print("I have not anyone of them")






#team=input("Ener your fav hockey team").upper()   #upper is to take input as uppercase
#sport=input("Enter your fav sport").upper()

#if sport=="HOCKEY" and team=="RANGERS":
#    print("I miss Messier")
#elif team=="LEAFS" or team=="SENATORS":
#    print("Good luck getting the cup this year")
#else:
#    print("I don't know that team")


#country="canada"
#country=country.upper()
#pet="moose"
#pet=pet.upper()

#if country=="CANADA" and (pet=="MOOSE" or pet=="BEAVER"):   #combinations of "and" ,"or" prioritized by the operators like *=and ,+=or BODMAS
#    print("Do you play hockey too??")
#else:
#    print(" Nice to meet you.")




monday=False
freshCoffee=True

if monday:   # default check for true value

    if not freshCoffee:     # default check for false value
        print("go buy coffee")
    print("now you can start work")
else:
 print("nothing to do")


 myValue = "yes"
if myValue != "yes":
    print("Hello")
print("World")


myCredits = 100
itemCost = 50

if myCredits > 100 and myCredits >= itemCost :
    print("You are eligible to purchase the item")
elif myCredits <= 100 and myCredits >= itemCost :
    print("You need over 100 credits to purchase anything")
elif myCredits > 100 :
    print("You need more credits to purchase this item")
else:
    print("You are not eligible to purchase this item")






result = ""
parameter = 10

if result == "success" or parameter == 10:
    result = "handled"
elif result == "" and parameter == 10:
    result = "no result" 
else:
    result = "unhandled"


print(result)




canPurchase = False
isAvailable = False 
if not isAvailable and canPurchase:
    print("success") 

canPurchase = False
isAvailable = False 
if not isAvailable or canPurchase:
    print("success") 

canPurchase = True
isAvailable = False 
if isAvailable or canPurchase:
    print("success") 




nextTurn = "arrived"
if nextTurn == "left" :
    print("Take your next left")
elif nextTurn == "right" :
    print("Take your next right")
elif nextTurn == "forward":
    print("Continue forward")
else:
    print("No direction found")




for index in range(2):
    print("Hello")
print("World")