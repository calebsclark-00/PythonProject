#void function
def printGrade(score):
    if score < 0 or score > 100:
        print("Invalid input")
        return None
    
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >=60:
        print('D')
    else:
        print('F')

def main():
    score = eval(input("Enter a score: "))
    print("The grade is ", end = '')

    print(f"{printGrade(score)}")
main()
