#filename=input("Enter  a file name with extension")
##access modifiers of python
#write="w"      # overwrite the file    
#read="r"        #read attribute to the file
#append="a"      #add information in the end of file
#binary="b"         #opens a binary file
#readwrite="w+"          #readwrite access
#readwrite1="r+"

#myfile = open(filename,mode=readwrite)
#myfile.write("Rajarshi,21\n")
#myfile.write("Stud2,22\n")
#myfile.write("Stud3,26\n")
#myfile.write("Stud4,22\n")
#myfile.write("Stud5,29\n")

#myfile = open(filename,mode=append)  #giving the files access modifier values (mode="")
#fileinfo=input("Enter file info:\n")
#myfile.write(fileinfo)                          #writing info into file
#myfile.close()                              #always close the file
#print("write successful! have fun ")



#opening a files
#read() function converts all content into one string 
#mystudentsfile=open("demo.csv","r")
#read all file contents
#firstline=mystudentsfile.readline()    #getting the first line
#print(firstline)

#allcontents=mystudentsfile.read()
#print(allcontents)

import csv
filename="demo.csv"

#method 1 for default closing
#with open(filename,"r") as myCSVfile:   #using "with open() as" instead of myCSVfile=open() because if we forget to close the file used by another program at that instance it will always close that thing to prevent error protecting me from data lose
#    allrowlist=csv.reader(myCSVfile)   
#    for currentrow in myCSVfile:
#        print(currentrow)



##method 2 for without default closing
#myCSVfile=open(filename,"r")
#for currentrow in myCSVfile:
#        print(currentrow)


#dataFromFie is a list having all data assigned into it
#each row will be one list items not individual values in "dataFromFile"



#with open(filename,"r") as myCSVfile:    #trying to print one word like name of the student not age
#    allrowlist=csv.reader(myCSVfile)
#    for currentrow in allrowlist:
#        print(currentrow)
#        for currentword in currentrow:
#            print(currentword)          # square brackets are printed




#no square brackets printed


with open(filename,"r") as myCSVfile:    #trying to print one word like name of the student not age
    allrowlist=csv.reader(myCSVfile)
    for currentrow in allrowlist:
                        #with brackets
        print("/age--- ".join(currentrow)) # customized view 





def myPrintout() :
    return "Hello"

print("World")
print(myPrintout())

