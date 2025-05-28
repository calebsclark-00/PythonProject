def printDistinctNumbers(n):
    #Make two lists
    list1 = [int(x) for x in n]
    list2 = []

    
    #Checks for distinct numbers 
    for dNum in list1:
        if dNum not in list2:
            list2.append(dNum)

    #Prints the distinct numbers         
    print("The distinct numbers are: ", end='')
    for dNum in list2:
        print(dNum, end=' ')
    print()

#Initalize main    
def main():
    #Asks for ten numbers
    data = input("Enter ten numbers: ")
    #Splits input
    n = (data.split())
    #calls printDistinctNumbers function
    printDistinctNumbers(n)
main()
