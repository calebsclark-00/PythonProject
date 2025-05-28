#Create the main function
def main():
    x = 1#represents int value
    y = [1,2,3]#represents a list

    #invoke m
    m(x,y)
    #display results
    print(f"x is {x}")
    print(f"y is {y[0]}")
def m(number,numbers):
    number = 1001#Asign a new value to number
    numbers[0] = 5555 #assign a new value to the list at index 0
    
#invoke main
main()
