#answer = 0
#a=0
#while answer !="4":
#    answer= input("What is 2+2 ?\n\n")
#    a=a+1
#    while a==5 :
#        print("You failed")
#        break
    
#print("Yes! 2 + 2 = 4\n\n")



#import turtle
#counter=0

#while counter<4:
#    turtle.forward(100)
#    turtle.right(90)
#    counter+=1



#generalized turtle


#import turtle

#pencolor="init"
#angle="0"
#turn="init"
#linelength=1
#linelen=0
#while linelength!=0:
    
#    linelength=input("Enter the line length :\n")
#    pencolor=input("Enter a pencolour:\n")
#    angle=input("Enter an angle:\n")
#    turn=input("Enter turn:\n")

#    if turn.lower()=="right":
#        turtle.right(int(angle) )
#        turtle.color(pencolor)
#        turtle.forward(int(linelength))
#    else:
#        turtle.left(int(angle) )
#        turtle.color(pencolor)
#        turtle.forward(int(linelength))
     
#    linelen+=1  
 
    
    







index = 1
while index < 5 :
    index += index + index
print(index)



index = 1
while index < 5 :
    index += 1

print(index)

ndex = 1
while index < 5 :
    index = index + 1
print(index)

index = 0
while index < 5 :
    print("loop")