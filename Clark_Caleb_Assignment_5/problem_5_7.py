#Description: Conversion from degrees to sin and cos
#import math
import math

#Display the headings
print(f"{'Degrees':10s}{'Sin':>10s}{'Cos':>10s}")

#Display the top divider
print('-' * 40)

#Initialize degrees
degrees = 0

#Create a while loop to iterate through untill 360
while degrees < 361:

    #Display the conversions
    print(f"{degrees:<10d}{math.sin(degrees):10.4f}{math.cos(degrees):10.4f}")

    #Increment degrees by 1
    degrees += 1
