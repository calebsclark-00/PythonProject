#cs1030
#Caleb
##700745292
#Asignment 3 3_1
'''
step 1: Prop the user to enter the length from the center to vortex

step 2: Calculate the  area by finding x

step 3: Display the area of the pentagon
'''
#import math
import math

#Step 1
length =eval(input("Enter the length from the center to a vertex: "))

#step 2

x = 2 * length * math.sin(math.pi/5)
area = 3 * math.sqrt(3) / 2 * x ** 2

#step 3
print(f"The area of the pentagon is {area}")
