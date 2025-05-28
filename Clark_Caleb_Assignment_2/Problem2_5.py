#cs1030
#Caleb
##700745292
#Asignment 2 2_5
'''
(Convert feet To Meters)
Step 1: reads a value of subtotal and gratuity from the console
step 2: Convert the input by adding them togethor for total
step 3: Display results
'''

#Step 1: Prompting the user for sub total and gratuity

subtotal, gratuity=eval(input("Enter the sub total and a gratuity rate: "))

#step:2
total = gratuity + subtotal

#step 3:
print(f"The gratuity is {gratuity} and the total is {total}")
