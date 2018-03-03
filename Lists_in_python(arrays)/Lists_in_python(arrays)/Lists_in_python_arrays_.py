party=["raj","friends","parents","docs","teachers","teachers"]

score=[50,20,47,98,501]

mix=["50","Name","Salary","Pension","Office"]   #python can store different values in one list

guests=[]       #empty list

#for steps in range(5):
#    print(party[steps]+"\n\n")
#    print(str(score[steps])+"\n\n")




#for steps in range(-5,-1):       #reverse printing  party[raj]=-5,party[friends]=-4 and so on
#    print(party[steps]+"\n\n")      




#party.append(input("Enter a new name:\n"))  #adds a value to the end of the list

#for steps in range(6):
    
#    print(party[steps])


#party.remove(input("Enter a value to remove:"))  # removes the value which comes first from left
    
#for steps in range(5):
#     print(party[steps])



#del party[0]  #another process
#print(party[0])   # list will automatically shift left  and [1] becomes [0] and so on

#if index is known use "del" or the value is known use ".remove"
        
#print(party.index("teachers"))     # index of the element position which comes first from left

# if the value  is not in the list then it will return an "error"


# if the index is not known to us then use len

animals=["dog","cat","tiger","donkey","horse"]


#for steps in range(len(animals)):
#    print(animals[steps])


#for currentAnimal in animals:       # dynamic way to get a value
#    print(currentAnimal)


#sorting list


animals.sort()                        
for currentAnimal in animals:   
    print(currentAnimal)




cityList = ["Seattle", "London", "Paris", "Sydney"]
print(cityList[-1])