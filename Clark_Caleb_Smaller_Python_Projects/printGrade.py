
answer = eval(input(f"What is the student score: "))

#Checks letter grade in a nested if statment
if answer < 0 or answer > 100:
     print("(WARNING INVALID INPUT!!!)")
    
if answer >= 90:
     Score = 'A'
elif answer >= 80:
     Score = 'B'
elif answer >= 70:
     Score = 'C'
elif answer >=60:
     Score = 'D'
else:
     Score = 'F'
#Display Results     
print(f"The student percentage {answer}% and the grade is {Score}!")
