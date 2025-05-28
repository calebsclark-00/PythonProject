#cs1030
#Caleb
##700745292
#Asignment 2 2_8
'''
Step 1: prompting the user for input 3 times
Step 2: Calculating formula
step 3: display results

Formula: m * (finalTempature - initialTempature) * 4184
'''
#Step 1: prompt user for m, initialTempature, and finalTempature
m=eval(input("Enter the amount of water in kilograms: "))
initialTempature=eval(input("Enter the inital temperature: "))
finalTempature=eval(input("Enter the final temperature: "))

#Step 2: calculate fromula
Q = m * (finalTempature - initialTempature) * 4184

#Step 3:
print(f"The energy needed is {Q}")
