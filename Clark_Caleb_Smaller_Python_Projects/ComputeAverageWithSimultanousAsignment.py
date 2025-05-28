#Description: Compute the average three numbers
#simultanous Asignment Demo

#Prompt the user to enter the 3 asignments

num1,num2,num3 = eval(input("Enter 3 values (seperated by commas)"))

#Compute average
average = (num1 + num2 + num3) / 3

pirnt(f"The average of {num1},{num2},{num3} is {average}")

#swapping variable values
x = 8

y = 12

x, y = y, x#Swaps the values of x and y

print(x, "", y)


