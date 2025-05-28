#Description: Conversion from meters to Kilometers

#Display the headings
print(f"{'Meters':10s}{'Kilometers':>10s}")

#Display the top divider
print('-' * 10)

#Initialize kilograms
meters = 1

#Create a while loop to iterate through untill 10
while meters < 11:

    #Display the conversions
    print(f"{meters:<10d}{meters * 1.60934:10.1f}")

    #Increment meters by 1
    meters += 1
