#Create a main function
def main():
    #Prompt to enter three number
    num1, num2, num3 = eval(input("Enter an interger: "))
    displaySortedNumbers(num1, num2, num3)

#displaySortedNumbers function
def displaySortedNumbers (num1, num2, num3):
    if num1 > num2:
        num1,num2 = num2, num1
    if num2 > num3:
        num2,num3 = num3, num2
    if num1 > num2:
        num1,num2 = num2, num1
    print(f"The sorted numbers are {num1},{num2},{num3}")

#Invoke the main function
main()
