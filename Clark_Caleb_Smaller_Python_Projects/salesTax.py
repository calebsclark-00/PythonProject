#Description: Get ammount from user and commpute sales tax

#Prompt the user for purchase ammount
item = eval(input("Enter purchase ammount: "))

#Compute Sales TAX
tax = item * 0.06

#Display results
print(f"Sales tax is ${tax:.2f}")
print("Sales tax is: $",int(tax * 100) / 100.0)

'''
tax * 100 = 1185.3
int(tax * 100) = 1185
int(tax * 100) / 100.0) = 11.85
'''
