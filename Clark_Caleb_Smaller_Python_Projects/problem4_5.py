#cs1030
#Caleb
##700745292
#Asignment 4 4_5
'''
find future dates
note: sunday = 0 monday = 1 saturday = 6
'''
#Prompt the user to enter a interger for todays day
today = int(input("Enter todays day (0-6): "))


#Prompt the user to enter the number of days elasped
eDays = int(input("Enter the number elasped from today: "))

# Create the multip way to check today and its string day
if today == 0:
    nameDay = "Sunday"
elif today == 1:
    nameDay = "Monday"
elif today == 2:
    nameDay = "Tuesday"
elif today == 3:
    nameDay = "Wendnesday"
elif today == 4:
    nameDay = "Thursday"
elif today == 5:
    nameDay = "Friday"
elif today == 6:
    nameDay = "Sunday"

#find the future day
fday = (today + eDays) % 7

#Create a multiway to check for future string day
if fday == 0:
    nameFuture = "Sunday"
elif fday == 1:
    nameFuture = "Monday"
elif fday == 2:
    nameFuture = "Tuesday"
elif fday == 3:
    nameFuture = "Wendnesday"
elif fday == 4:
    nameFuture = "Thursday"
elif fday == 5:
    nameFuture = "Friday"
elif fday == 6:
    nameFuture = "Sunday"
print(f"Today is {nameDay} and the future day is {nameFuture}")
