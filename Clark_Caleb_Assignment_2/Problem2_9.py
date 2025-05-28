#cs1030
#Caleb
##700745292
#Asignment 2 2_9
'''
Step 1: prompting the user for input 2 times
Step 2: Calculating formula
step 3: display results

Formula: twc = 35.74 + 0.6215 * t - 35.75 * y^0.16 + 0.4275 * t * y^0.16
'''
#Step 1: Prompt user for t and y
t=eval(input("Enter the tempature in Fahrenheit between -58 and 41: "))
y=eval(input("Enter the wind speed in miles per hour: "))


#Step 2: calculate fromula
twc = 35.74 + 0.6215 * t - 35.75 * y ** 0.16 + 0.4275 * t * y **0.16

#Step 3:
if t < -58 or t > 41:
    print("The tempature is invalid")
elif y < 2:
    print("The wind speed is invalid")
else:
    print(f"The wind chill index is {twc}")
