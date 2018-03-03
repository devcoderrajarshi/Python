#def main():
#    printNames()
#    return


#def printNames():         #def is the acronym of define
#    names=["Raj","kalu","Raju"]
#    for name in names:
#        print(name)
    
   
#    return



#main()                    #Executing main func
#printNames()              #to do that the func must be created 





#def main():
#    names=["Raj","Raja","Bjoy"]
#    newName=input("Enter name:\n")
#    names.append(newName)
#    printNames(names)
#    return         #as soon as we reach at the return variables are no longer available so we can reuse them in other func


#def printNames(list):  #list=names passing name into printNames here list is a parameter can also use "names" which is used before
#    for name in list:
#        print(name)
#    return

#main()  



def getMessage(name):
    message="Hi,"+name+"   I am I-MAX"
    return message                            #returning value "message".Also can directly implemented as   "Hi,"+name+"   I am I-MAX"   inplace of message


def printMessage(msg):
    print(msg)
    return


                                              #output=getMessage(input("Enter your name please:\n"))
                                              #printMessage(output)


def main():
    #names=getMessage(input("Enter your name please:\n"))
    printMessage(getMessage(input("Enter your name please:\n"))) # func inside a func.


main()


