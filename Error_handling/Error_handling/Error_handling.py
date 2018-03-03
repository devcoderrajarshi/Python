import sys
try:
    firstnum=float(input("Enter a number"))
except:
    print("oops, follow the rules baby:\n")
        
try:
    secnum=float(input("Enter another number"))
except:
    print("oops, follow the rules baby:\n")

    




#result=firstnum/secnum    #error is generated in this line when secnum==0

##if error occurs inside of try it will go to the :except: loop
#try:
#    result=firstnum/secnum        #code that can genetrate error
#    print(result)
#except:
#    error=sys.exc_info()[0]
#    print("Sorry, Something went Wrong")   #if error occurs this line will be executed
#    print("The error is:\n")
#    print(error)
#finally:
#    print("I will always Execute!!!\n")     #this code always executes








#try:
#    result=firstnum/secnum        
#    print("Result is:\n")
#    print(result)
#except ZeroDivisionError:         #if you know the error from the code "error=sys.exc_info()[0]" or by assumption then put it into "except"
 
#    print("Result is infinity\n") 
#    sys.exit()                                          #exits from the code immediately if error ocurs
#except:                                   #if other errors occurs then it will execute
#    error=sys.exc_info()[0]                         
#    print("Wtf: just you did!!!!\n") 
#    print(error)
#    sys.exit()
##difference btw finally: and print()
##if you use finally: it will always execute wheather there is sys.exit() or not but in case of print() it will not execute as we are exiting from the program
#    print("I will always Execute!!!")

#finally:                                  #same as print("any statement") at last but this is a format of error handling in oop language
#    print("I will always Execute!!!\n")    
  
    
  
#how to not execute a code when error is occured?
secnum=0.0
try:
    result=firstnum/secnum
    print(result)
    errorcon=False
except ZeroDivisionError:
    print("infinty")
    errorcon=True

if not errorcon:
    print("There is no eror in this program:\nhave fun\n")




print("Its OK")