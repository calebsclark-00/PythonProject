#cs1030
#Caleb
##700745292
#Asignment 3 3_8
'''
step 1:Takes the input for ammount given

step 2: Converts the amount given to dolars, quarters, dimes, nickels, pennies

step 3: Prints the calculation of the conversions and input given

'''

#step 1:
amount = int(input("Enter an amount, for example 1156: "))

#step 2:
numberOfDollars = amount // 100
amount %= 100

numberOfQuarters = amount // 25
amount %= 25

numberOfDimes = amount // 10
amount %= 10

numberOfNickels = amount // 5
numberOfPennies = amount % 5

#step 3:
print("Your amount", {amount}, "consists of\n",
      "\t", {numberOfDollars}, "dollars\n",
      "\t", {numberOfQuarters}, "quarters\n",
      "\t", {numberOfDimes}, "dimes\n", "\t",
      {numberOfNickels}, "nickels\n", "\t",
      {numberOfPennies}, "pennies")
