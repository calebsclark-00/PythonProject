#Description: shows time

#Import time module
import time

numOfLines = eval(input("Enter the number of seconds: "))

#Get current Time and counts down to 0 and prints stopped
while numOfLines > 0:
    curentTime = time.time()
    print(f"{numOfLines} seconds remaining")
    time.sleep(numOfLines)
    numOfLines -= 1
print("Stopped")
