"""
Name: RAJ KANSAL
PRN: 20190802013
SEM: 5th (3rd Year)

"""

#Equation Used y = mx + c (Equation of a straight line)

new_x = int(input("Enter the Value of x: "))
m = int(input("Enter the Value of m: "))
c = int(input("Enter the Value of c: "))


partial_derivation = lambda x: m*x + c
learning_rate = 0.01
precision = 0.0001
previous_step_size = 1
while previous_step_size > precision:
    old_x = new_x
    new_x = new_x - learning_rate * partial_derivation(old_x)
    previous_step_size = abs(new_x - old_x)
    print("Final value of x is : ", new_x)
    
print("The Gradient Descent for the equation will be : ", new_x)
print('\n')
