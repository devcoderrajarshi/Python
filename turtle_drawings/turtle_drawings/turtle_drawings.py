import turtle
#import math

#for steps in range(4): #for loop 
#    turtle.color("red")
#    turtle.forward(100)
#    turtle.right(90)
 

#turtle.right(45)
#turtle.color("blue")
#turtle.forward (100*(pow(2,0.5)))

#turtle.right(135)
#turtle.color("red")
#turtle.forward (100)
#turtle.right(135)
#turtle.color("blue")
#turtle.forward (100*(pow(2,0.5)))
    




#for steps in range(1,10,2):  #this line means i=1 to 10 ,i=i+2
#             print(steps)



#for steps in range(1,10)   # it will execute upto 9.when it will be equals to 10 then it stops





#for steps in [1,2,3,4,5,6,7]:  #specifying the exact value of loop
#    print(steps)





# more fun with turtle

for colour in ["red","blue","green","violet","orange"]:     #you can also mix up datatypes in loop int,str,float,boolean etc
    turtle.color(colour)
    turtle.right(360/5)
    turtle.forward (50)
    for steps in ["red","blue","green","violet","orange"]:
        turtle.color(steps)
        turtle.right(360/5)
        turtle.forward (100)
   





