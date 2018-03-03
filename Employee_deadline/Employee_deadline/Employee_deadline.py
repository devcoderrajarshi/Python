import datetime
currentdate=datetime.date.today()


userinput=input("Enter deadline of your project (dd/mm/yyyy)\n\n")
deadline=datetime.datetime.strptime(userinput,"%d/%m/%Y").date()      #       ".date()" only helps you to get only the date value rather than time
days=deadline-currentdate
print(days)
k=int(days.days) #converting to integer
year=int((k/365))
yearrem=(k%365)
month=int((yearrem/30))   #converting to integer
monthrem=(yearrem%30)
week=int((monthrem/7))     #converting to integer
weekrem=(monthrem%7)
daysrem=int((weekrem%7))    #converting to integer

                                                   #possible cases for month,week and days

#if month==0 and week==0 :
#    print("You have {0:d} days remaining for your project".format(daysrem))
#elif week==0 and daysrem==0:
#    print("You have {0:d} month remaining for your project".format(month))
#elif month==0 and daysrem==0:
#    print("You have {0:d} week remaining for your project".format(week))
#elif month==0:
#    print("You have {0:d} week and {1:d} days remaining for your project".format(week,daysrem))
#elif week==0 :
#    print("You have {0:d} month and {1:d} days remaining for your project".format(month,daysrem))
#elif daysrem==0:
#    print("You have {0:d} month and {1:d} week  remaining for your project".format(month,week))
#else:    
    
print("You have {0:d} year {1:d} month and {2:d} week and {3:d} remaining for your project".format(year,month,week,daysrem))
