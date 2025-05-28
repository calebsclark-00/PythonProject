#Description: Conversion from number to squared root
#inported math
import math

#Display the headings
print(f"{'Number':10s}{'Square root':>10s}")

#Display the top divider
print('-' * 40)

#Initialize number
number = 0

#Create a while loop to iterate through untill 20
while number < 21:

    #Display the conversions
    print(f"{number:<10d}{math.sqrt(number):10.4f}")

    #Increment number by 1
    number += 1
