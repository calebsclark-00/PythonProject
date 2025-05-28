#Create a main function
def main():
    #Prompt to enter number
    number = eval(input("Enter an interger: "))
    reverse(number)

#Reverse function
def reverse (number):
    #Extract the remainder
    remainder = number % 10

    print(f"{remainder}", end = '')

    number //= 10

#Invoke the main function
main()
