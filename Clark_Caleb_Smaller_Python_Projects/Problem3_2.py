#cs1030
#Caleb
##700745292
#Asignment 3 3_2
'''
(Gemotry: Great Circle Distance)

step 1: Prop the user to enter the latitude and longitude
of tow points (x1,xy1) and (x2,y2)

step 2: Calculate the distance between the two points
using the formula that is given
in the questiion

step 3: Display the great circle distance
'''
#import math
import math

#Step 1
x1,y1 =eval(input("Enter point 1 (latitude and longitude) in degrees: "))

x2,y2 =eval(input("Enter point 2 (latitude and longitude) in degrees: "))

#step 2

d = 6371.01 * math.acos(math.sin(math.radians(x1)) * \
                        math.sin(math.radians(x2)) + \
                        math.cos(math.radians(x1)) * \
                        math.cos(math.radians(x2)) * \
                        math.cos(math.radians(y1 - y2)))
#step 3
print(f"The distance between the two points is {d} km !")
