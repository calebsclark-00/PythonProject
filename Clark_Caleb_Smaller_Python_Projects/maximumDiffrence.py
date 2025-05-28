'''
Note: Calling a function executes the code in the function

Note:In a function definiton, you define what is in to do. You use a function,
you have to call or invoke it. The program that calls the function is caller

'''

def max(num1, num2):

    #Check if num1 is greater than num2
    if num1 > num2:
        result = num1
    else:
        result = num2

    #We need to return the result back to the caller
    return result
def main():
    i = 5
    j = 2
    k= max(i,j) #invoking the max function and passing the arguements for i and j

    #Display results and return back to calller
    print(f"The maximum {i} and {j} is {k}")

#Invoke main function
main()
