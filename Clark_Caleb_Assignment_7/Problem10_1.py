#Initalize asignGrade
asignGrade(n):
    best = int(max(n))
    #Initalize x
    x = 0

    
    while x < len(n):
        #get's score
        score = int(n[x])

        #if else statement to asign grade
        if score >= best - 10:
            print("Student", x, "score is", score, "and the grade is A!")
        elif score >= best - 20:
            print("Student", x, "score is", score, "and the grade is B!")
        elif score >= best - 30:
            print("Student", x, "score is", score, "and the grade is C!")
        elif score >= best - 40:
            print("Student", x, "score is", score, "and the grade is D!")
        else:
            print("Student", x, "score is", score, "and the grade is F!")
        #Icrement student
        x += 1

#Initalize main
def main():
    #takes input of scores
    studentScore = (input("Enter Scores:  "))

    #Splits input
    n = (studentScore.split())

    #Calls asignGrade
    asignGrade(n)

main()
