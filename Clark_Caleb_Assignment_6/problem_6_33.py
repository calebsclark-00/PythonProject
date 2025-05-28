#cs1030
#Caleb
##700745292
#Asignment 3 3_4
'''
step 1: Prop the user to enter the side of the pentagon

step 2: Calculate the  area using the side

step 3: Display the area of the pentagon
'''
#import math
import math
#Create a main function
def main():
    #Step 1
    s = eval(input("Enter the side of the pentagon: "))
    area(s)
#Area calculation function
def area(s):

    #step 2

    area = (5 * (s ** 2)) / (4 * (math.tan(math.pi / 5)))

    #step 3
    print(f"The area of the pentagon is {area}")
main()
