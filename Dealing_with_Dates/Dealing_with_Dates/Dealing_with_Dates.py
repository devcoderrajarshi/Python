import datetime
currentdate=datetime.date.today()

#print(currentdate)
#print(currentdate.year)
#print(currentdate.month) #intellisense will not appear in . operator because we haven't initialize the value to a date
#print(currentdate.day)
#print("\n\n")

#print(currentdate.strftime('%B %a %A%d %b,%y')) #to aviod confusion in slash date formats we use strftime shows a particular date
#                                        # %d=date ,%b=short form of the month (as month and minutes has m so using b ),%Y=year 😃
#                                        #%B=is the full month name
#                                        #%y is the two digit year
#                                        #%a is the day of the week short form
#                                        #%A is the day of the week
#                                        #reference use http://www.strftime.org/
                                        #for local date and time formats use http://babel.pocoo.org/

#userinput=input("Please enter your next birthday(dd/mm/yyyy)\n")
#birthday=datetime.datetime.strptime(userinput,"%d/%m/%Y").date()   #strptime is reconstructing the userinput as date using given format "%d.%m.%Y"
#print("your birthday is")
#print(birthday)
#difference= birthday-currentdate
#print(difference)                                            #for more info http://labix.org/python-dateutil


currenttime= datetime.datetime.now()

print(currenttime)
print(currenttime.hour)
print(currenttime.minute)
print(currenttime.second)

print(datetime.datetime.strftime(currenttime,"%H or %I:%M:%S %p"))

