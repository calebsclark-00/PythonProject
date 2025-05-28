day = 0
questionOne = "Is your birthday in set one: \n" + \
                         "1 3 5 7 \n" + \
                         "9 11 13 15" + \
                         "17 19 21 23" + \
                         "25 27 29 31" + \
                         "Enter 0 for No and for YES"
answer = eval(input(questionOne))
if answer == 1:
    day += 1


questionTwo = "Is your birthday in set one: \n" + \
                         "2 4 6 8 \n" + \
                         "10 12 14 16" + \
                         "18 20 22 24" + \
                         "26 28 30" + \
                         "Enter 0 for No and for YES"
answer2 = eval(input(questionTwo))
if answer2 == 1:
    day += 1
