import random 
def main():
    #Initalize count
    count = 0
    #Check within range of 10000
    for i in range(10000):
        #Checks if A
        if getRandomUpperCaseLetter() == 'A':
            count += 1
    #Prints prompt and checks the percentage        
    print("The probability of A in a range of 10,000 is: ", count / 10000,"!")
#Generate a random character between ch 1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(random.randint(ord(ch1), ord(ch2)))
#Generate a random character lowercase
def getLowercaseLetter():
    return getRandomCharacter('a','z')
#Generate a random character uppercase
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')
#Generate a random digit charcater 
def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')
#Generate a random charcater 
def getRandomASCIICharacter():
    return chr(random.randint(0, 127))
#Invoke the main function
main()
