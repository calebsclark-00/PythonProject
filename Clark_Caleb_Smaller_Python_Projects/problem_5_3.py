#Description: Conversion from kilogram to pounds
#Note: 1 kilogram is 2.2 pounds

#Display the headings
print(f"{'Kilograms':10s}{'Pounds':>10s}")

#Display the top divider
print('-' * 20)

#Initialize kilograms
kilograms = 1

#Create a while loop to iterate through untill 199
while kilograms < 200:

    #Display the conversions
    print(f"{kilograms:<10d}{kilograms * 2.2:10.1f}")

    #Increment kilograms by 2
    kilograms += 2
