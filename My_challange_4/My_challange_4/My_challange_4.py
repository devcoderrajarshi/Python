
name=[]
n=""
while n!="stop":
    
    n=input("Enter name of guest:(Enter a stop for no more names)\n\n")
    name.append(n)
    

name.sort()
print("the guest list you have entered\n")
for each in range(len(name)-1):
    print(name[each])