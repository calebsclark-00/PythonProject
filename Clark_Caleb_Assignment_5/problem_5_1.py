#Collects the 4 inputs
num1 = eval(input("Enter an interger, the input ends if it is 0: "))
num2 = eval(input("Enter an interger, the input ends if it is 0: "))
num3 = eval(input("Enter an interger, the input ends if it is 0: "))
num4 = eval(input("Enter an interger, the input ends if it is 0: "))

#Calculates average and total
average = (num1 + num2 + num3 + num4) / 4
total = num1 + num2 + num3 + num4

#Checks if a zero was inputed and shows total and average
if num1 == 0:
    print("You did not enter a number")
elif num2 == 0:
    print("You did not enter a number")
elif num3 == 0:
    print("You did not enter a number")
elif num4 == 0:
    print("You did not enter a number")
else:
    print(f"The total is {total}")
    print(f"The average is {average}")
