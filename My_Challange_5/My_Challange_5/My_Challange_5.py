def FileName(Name):
    
    Filename=open(Name,mode="a")
    return

def FileInfo(info,name):
    message=open(name,mode="a")
    message.write(info)
    return

def main():
    msgname=input("Enter the filename with extension:\n") 
    information=input("Enter the info:\n") 
    FileName(msgname)
    FileInfo(information,msgname)


main()