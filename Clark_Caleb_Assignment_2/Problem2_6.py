#cs1030
#Caleb
##700745292
#Asignment 2 2_6
'''
(Sum of the digits in the iteger)

Step 1: Read an interger between 0 and 1000

step 2: extract and remove each digit to be added togethor

step 3: Display the results

Hint: Use the % operator to extract digits and the // to remove digits
Example: 932 % 10 = 2 and 932 // 10 = 93
'''

#Step 1:

number = eval(input("Enter a number between 0 and a 1000: "))

#Step 2:
#For digit 1 we will extract and remove the last digit
digit1 = number % 10#Extract the last digit

#number = number // 10
number //=10#Remove last digit

#For digit 2 we will extract and remove the last digit
digit2 = number % 10
number //=10

#For digit 3 we will extract and remove the last digit
digit3 = number % 10
number //=10

#Extract the fourth digit
digit4 = number % 10

results= digit1 + digit2 + digit3 + digit4
#Step 3
print(f"The sum of the digits is {results}")
