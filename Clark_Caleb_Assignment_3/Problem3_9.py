#cs1030
#Caleb
##700745292
#Asignment 3 3_9
'''
step 1: Prop the user to enter the employee data

steps: Calculate the conversion of tax rate and gross pay and net pay

step 3: Display the results
'''

#Step 1
name =(input("Enter an employee's name: "))
hours =eval(input("Enter number of hours worked in a week: "))
hourly =eval(input("Enter hourly pay rate: "))
fedTax =eval(input("Enter federal tax withholding rate: "))
stateTax =eval(input("Enter state tax withholding rate: "))

#step 2

grossPay = hourly * hours
fedWith = grossPay * fedTax
stateWith = grossPay * stateTax
totWith = stateWith + fedWith
netpay = grossPay - totWith

#step 3
print(f"Employee name: {name}")
print(f"Hours worked: {hours}")
print(f"Pay Rate: ${hourly}")
print(f"Gross Pay: ${grossPay}")
print(f"Deductions:")
print(f"    Federal Withholding (20.0%): ${fedWith}")
print(f"    State Withholding (9.0%): ${stateWith}")
print(f"    Total Deduction: ${totWith}")
print(f"Net Pay: ${netpay}")

