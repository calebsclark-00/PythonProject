#Description: Display a pyramid between 1 and 15

#import the sys module
import sys

#Prompt the user to enter the number of lines
numOfLines = eval(input("Enter the number of lines (1 - 15): "))

#Create a one-way if statement to check user input
if numOfLines < 1 or numOfLines > 15:

    #Display an error message
    print("Error: number of lines needs to be 1 through 15!")

    #terminate the program
    sys.exit()

#Create an outer loop to control our rows
for row in range(1,numOfLines + 1):

    #First for loop is for our padding
    for column in range(1,numOfLines - row + 1):
        print("   ", end = '')

    #for loop to build the left half or the pyramid (leading numbers)
    for num in range(row,0, -1):
        print(f"{num:3d}", end = '')

    #for lloop to build the right half of the pyramid
    for num in range(2, row + 1):
        print(f"{num:3d}", end = '')

    #start the next row
    print()
