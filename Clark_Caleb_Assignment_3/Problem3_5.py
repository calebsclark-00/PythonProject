#cs1030
#Caleb
##700745292
#Asignment 3 3_5
'''

step 1: Prop the user to enter the number od sides and enter the side length

step 2: Calculate the  area using a formula to find the area
the area.

step 3: Display the area of the polygon
'''
#import math
import math

#Step 1
n = eval(input("Enter the number of sides: "))
s = eval(input("Enter the side: "))

#step 2

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

#step 3
print(f"The area of the polygon is {area}")
