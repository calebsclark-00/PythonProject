def countOccurence(numbers):
    #initalize count to hold intergers within 1 and 100
    count = [0 for i in range(1, 101)]

    nums = [int(n) for n in numbers]

    for i in nums:

        count[i - 1] += 1
    #Goes through the list and prints the numbers entered and the times 
    for x in range(len(count)):

            if count[x] == 1:

                print ((x + 1), "occurs", (count[x]), "time!")  

            elif count[x] != 0:

                print ((x + 1), "occurs", (count[x]), "times!")

def main():
    #Takes input of numbers

    numbersInput = input("Enter integers between 1 and 100: ")

    #split the numbers inputed

    numbers = numbersInput.split(" ")

    #calls countOccurence
    countOccurence(numbers)
main()
