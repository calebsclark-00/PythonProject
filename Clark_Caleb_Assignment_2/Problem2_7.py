#cs1030
#Caleb
##700745292
#Asignment 2 2_7
'''

Step 1: Read an number of minutes from console

step 2: Covert the munutes into days and years

step 3: Display the results

'''

#Step 1: Prompt user for minutes

minutes = eval(input("Enter the number of minutes: "))

#Step 2:
days = minutes // 1440
years = days // 365
days %= 365

#Step 3:

print(f"{minutes} minutes is aproximately {years} years and {days} days")
