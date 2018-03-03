import sys

filename=input("Enter a file name to read:\n")


try:
    filecontent=open(filename,"r")
    filecontent=filecontent.read()
    print("Read Successful:\n")
    print(filecontent)
except:
    errorname=sys.exc_info()[0]
    print("Sorry, File does not exist:\n")
    print(str(errorname)+"\n")
    
finally:
    print("Have a good day:\n")