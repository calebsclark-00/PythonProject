#Description: Conversion from kilogram to pounds and reverse
#Note: 1 kilogram is 2.2 pounds

#Display the headings
print(f"{'Kilograms':10s}{'Pounds':>10s}{'Pounds':>10s}{'Kilograms':10s}")

#Display the top divider
print('-' * 40)

#Initialize kilograms and pounds
kilograms = 1
pounds = 1

#Create a while loop to iterate through untill 199
while kilograms < 200:

    #Display the conversions
    print(f"{kilograms:<10d}{kilograms * 2.2:10.1f}{'|'}{pounds:10.1f}{pounds * 2.2:10.1f}")

    #Increment kilograms by 1 and pounds by 1
    kilograms += 1

    pounds +=1
