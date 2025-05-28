#Description: Conversion from meters to Kilometers and reverse

#Display the headings
print(f"{'Meters':10s}{'Kilometers':10s}{'Kilometers':>13s}{'Meters':>10s}")

#Display the top divider
print('-' * 40)

#Initialize kilometers and meters
meters = 1
kilometers = 1

#Create a while loop to iterate through untill 10
while meters < 11:

    #Display the conversions
    print(f"{meters:<10d}{meters * 1.60934:10.1f}{kilometers:10.1f}{meters * 0.621:10.1f}")

    #Increment meters by 1 and kilometers by 1
    meters += 1

    kilometers +=1
