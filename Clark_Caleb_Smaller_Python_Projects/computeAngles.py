#cs1030
#Caleb
##700745292
#description: Display the figures angles
#Import math
import math
x1,y1,x2,y2,x3,y3 = eval(input("Enter six cordinates of three sperate points by commas"))

#Compute edges
a = math.sqrt(pow(x2 - x3,2) * (x2 - x3) + pow(y2 -y3,2))
b = math.sqrt(pow(x1 - x3,2) + pow(y1 - y3,2))
c = = math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))

#compute angles
