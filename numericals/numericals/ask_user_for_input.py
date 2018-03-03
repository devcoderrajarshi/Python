salary=0
bonus=0
salary = input("Enter your salary")
salary=int(salary)                              #converts a string value to a integer value 
bonus=input("Enter your bonus")
bonus=int(bonus)                                #also can be used as float(value),str(value),long(value)

paycheckamt=float(salary)+int(bonus) # another new process without assigning

print("The total salary is %.5f"%paycheckamt)

