#Game:Hangman

#Import the random module
import random

#Create a main function
def main():

    #Create a list of possible words
    words = ["write","that","program","nice","study"]

    #Select random word
    while True:
        #Randomly selects the index (word to be used)
        index = random.randint(0,len(words) - 1)

        #Store that word into new variable
        hiddenWord = words[index]

        #Using the length function we can blurr the letters
        guessedWord = len(hiddenWord) * ['*']

        #Track the number of letters guess correctly / and incorrectly
        numOfCorrect = 0
        numOfIncorrect = 0

        while numOfCorrect < len(hiddenWord):
            #Prompt the user to guess a letter
            letter = input(f"(Guess) Enter a letter in word {toString(guessedWord)}: ").strip()

            if letter in guessedWord:
                print(f"\t{letter} is already in the word")

            elif hiddenWord.find(letter) < 0:
                print(f"\t{letter} is not in the word")

                #Increment number of misses
                numOfIncorrect += 1
            else:
                #Found the letter and reveal that letter
                k = hiddenWord.find(letter)

                while k >= 0:
                    #Reveal the letter
                    guessedWord[k] = letter

                    #Increment the correct guess
                    numOfCorrect += 1

                    #Search the word for multiple instances of a letter
                    k = hiddenWord.find(letter,k +1 )
        #Display results
        print(f"The Word is {hiddenWord}. You missed {numOfIncorrect}" +
              (" time" if (numOfIncorrect <+ 1) else " times"))
        #Prompt the user to see if they want to play again
        anotherGame = input("\nDo you want to guess for another word? Enter y or n: ").strip()

        #Check the user response
        if anotherGame == 'n':
            print("\nFinished")
            break #End the loop
#Create a function to strip our list to a string
def toString(list):
    #Create an empty string
    s = ""

    #Iterate through the list placing each letter into our empty string
    for element in list:
        s += element
    return s

#iNVOKE MAIN
main()
