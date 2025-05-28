#cs1030
#Caleb
##700745292
#Asignment 2 2_2
'''
(Convert feet To Meters)
Step 1: reads a value of raduus and length from the console
step 2: Convert the radius abd length to area and volume
step 3: Display two results
'''

#Step 1: Prompting the user

radius, length=eval(input("Enter the radius and length of a cylinder: "))

#Step 2:
area = radius * radius * 3.14
volume = area * length
#step 3:
print(f"The area is {area}")
print(f"The volume is {volume}")
