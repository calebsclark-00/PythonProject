#cs1030
#Caleb
##700745292
#Asignment 2 2_16
'''
Step 1: prompting the user for input 1 time with 3 diffrent inputs
Step 2: Calculating formula
step 3: display results

Formula: a = (v1 -v0) / t
'''
#Step 1: prompt user for v0, v1, and t
v0, v1, t=eval(input("Enter v0, v1, and t: "))

#step 2: calculate formula
a = (v1 -v0) / t

#Step 3:
print(f"The average aceleration is {a}")
