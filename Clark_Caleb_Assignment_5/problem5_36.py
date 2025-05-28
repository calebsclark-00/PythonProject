import random
#cs1030
#Caleb
##700745292
#Asignment 5 5_36


#initalize win counts
win = 0
#continues program until 3 wins
while win < 3:
    #Generates 1 random numbers
    computer = random.randint(0,2)
    
    #Prompt the user to enter an 1,2,3
    user = eval(input("Please enter zero for scissors, 1 for rock, or 2 for paper: "))

    #Display results for each outcome
    if computer == 0 and user == 0:
        print("You both selected scissors")
    elif computer == 0 and user == 1:
        print("You Won! You selected rock and they selected scissors.")
        win += 1
    elif computer == 0 and user == 2:
        print("You Lost! You selected Paper and they selected scissors.")
    elif computer == 1 and user == 1:
        print("You both selected rock")
    elif computer == 1 and user == 0:
        print("You Lost! You selected scissors and they selected rock.")
    elif computer == 1 and user == 2:
        print("You Won! You selected paper and they selected rock.")
        win += 1
    elif computer == 2 and user == 0:
        print("You Won! You selected scissors and they selected paper.")
        win += 1
    elif computer == 2 and user == 1:
        print("You Lost! You selected rock and they selected paper.")
    elif computer == 2 and user == 2:
        print("You both selected paper")
