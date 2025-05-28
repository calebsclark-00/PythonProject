#Create a main function
def main():

    #Create a list of possible zodiac signs
    zodiacSigns = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]

    #Prompt the user to input their birth year
    birthYear = int(input("Please enter your birth year: "))

    # Determine the zodiac sign results for the given birth year
    zodiacSign = zodiacSigns[(birthYear) % 12]

    #Prints zodiac sign result
    print(f"The year of the {zodiacSign}")
main()
