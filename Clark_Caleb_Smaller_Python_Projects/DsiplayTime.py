#Description: Write a program that obtains minutes and displays remaining seconds
#From in ammount in time in seconds

#prompt the user for seconds
seconds = eval(input("Enter an interger for seconds: "))

#Get minutes and remaining seconds
minutes = seconds // 60
remainingSeconds = seconds % 60

#Display results
print(f"{seconds} seconds is {minutes} minutes and {remainingSeconds} seconds!")

int("3.4")
eval("3+4")
eval("0005")
