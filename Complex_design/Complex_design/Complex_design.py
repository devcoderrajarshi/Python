import turtle
#a=True
#b=False

#for steps in range(10):
#    if b:
#        a=True
        
#        turtle.color("red")
#        turtle.forward(50)
#        turtle.right(36)
#    elif a:
        
#        turtle.color("blue")
#        turtle.forward(50)
#        turtle.right(36)



#design :1

#for steps in range(5):
#    turtle.color("red")
#    turtle.forward(100)
#    turtle.right(360/5)
#    for moresteps in range(5):
#        turtle.forward(50)
#        turtle.right(360/5)


#design :2

#for steps in range(4):
#    turtle.color("red")
#    turtle.forward(50)
#    turtle.right(90)
#    for steps1 in range(4):
#        turtle.color("blue")
#        turtle.forward(200)
#        turtle.right(90)



#design :2

#for steps in range(10):
#    turtle.color("red")
#    turtle.forward(100)
#    turtle.right(36)
#    for steps1 in range(10):
#        turtle.color("red")
#        turtle.forward(50)
#        turtle.right(36)
        





#generalized case

sidenum=int(input("Enter the number of sides:")) 

for steps in range(1,sidenum):                      #specifying counting from 1
    turtle.color("red")
    turtle.forward(50)
    turtle.right(360/(sidenum-1))                    #nested for loop
    for steps1 in range(1,sidenum):               
        turtle.color("red")
        turtle.forward(100)
        turtle.right(360/(sidenum-1))
        #for steps1 in range(sidenum):
        #    turtle.color("red")
        #    turtle.forward(80)
        #    turtle.right(360/sidenum)

        
