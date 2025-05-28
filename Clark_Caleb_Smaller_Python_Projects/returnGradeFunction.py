#redesign the print grade function

#Return the grade for the score function

def getGrade(score):
     if score < 0 or score > 100:
        return "(WARNING INVALID INPUT!!!)"
    
     if score >= 90:
        return 'A'
     elif score >= 80:
        return 'B'
     elif score >= 70:
        return 'C'
     elif score >=60:
        return 'D'
     else:
        return 'F'

def main():

    score = eval(input("Enter a score: "))

    print(f"The grade is {getGrade(score)}")
main()
