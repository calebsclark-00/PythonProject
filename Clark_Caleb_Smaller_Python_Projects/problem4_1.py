#cs1030
#Caleb
##700745292
#Asignment 4 4_1
'''
solve quadratic equations
formulas given:
b * a - 4 * a * c
root1: (-b + discreminite ** 0.5) / ( 2 * a)
root2: (-b - discreminite ** 0.5) / ( 2 * a)

note: check for three  cases

Case 1 if postive two real roots
case 2 if it is zero the equation has one root
case 3 if negative no real roots
'''
#Prompt the user to enter 3 points a,b,c
a,b,c = eval(input("Enter a,b,c: "))

# store the 
discreminite = b * b - 4 * a * c

# Create the multip way to check our three cases
if discreminite < 0:
    print("The equation has no real roots")
elif discreminite == 0:
    r1 = -b / (2 * a)
    print(f"The root is {int(r1)}")

else:
    #We have a postive
    r1 = (-b + discreminite ** 0.5) / (2 * a)
    r2 = (-b - discreminite ** 0.5) / (2 * a)
    print(f"The roots are {r1:.6f} and {r2:.5f}")
