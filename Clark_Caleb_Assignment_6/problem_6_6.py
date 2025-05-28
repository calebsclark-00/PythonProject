#Description: Display a pyramid between 1 and 15

#import the sys module
import sys

#Create a main function
def main():
    
    #Prompt the user to enter the number of lines
    n = eval(input("Enter the number of lines (1 - 15): "))
    displayPattern(n)


def displayPattern(n):
    #Create a one-way if statement to check user input
    if n < 1 or n > 15:

        #Display an error message
        print("Error: number of lines needs to be 1 through 15!")

        #terminate the program
        sys.exit()

    #Create an outer loop to control our rows
    for row in range(1,n + 1):

        #First for loop is for our padding
        for column in range(n - 1):
            print(" ", end = '')

        #for loop to build the left half or the pyramid (leading numbers)
        for num in range(row, 0, -1):
            print(f"{num:3d}", end = '')


        #start the next row
        print()
#Invoke the main function
main()
