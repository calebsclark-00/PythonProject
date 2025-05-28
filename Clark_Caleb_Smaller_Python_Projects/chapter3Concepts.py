#cs1030
#Caleb
##700745292
#description: Examples of chapter 3 concepts

#Import turtle
import turtle

#Settings and characters
letter ='A'
letter ="A"

mesage = 'Good evening'
mesage = "Good evening"

#Built in functions and string data type
s="Welcome"
#Len function
print(len(s))

#Max and min functions
print(max(1, 4, 5, 55, 4, 3, 2))
print(min(66,77,88,4))

print(max(s))
print(min(s))

#ord function
print(ord('A'))
print(ord('a'))

print(chr(65))
print(chr(97))

print(ord('a') - ord('A') + 1)


print("\tHE, n\ \"John's program is easy to read\"")

#print(item, end = 'Anything string'
print( "Hello", end = ', ')
print( "World", end = '!')

print("\n")
print("AAA", end = '   ')
print("BBB", end = '***')
print("CCC", end = '$')
print("DDD", end = '!!!')
print("\n")

#Str converts a number to a sting
s = str(3.8)
print(s)

r = str(5)
print(type(r))
message = "welcome" + "to" + "python"
print(message)

firstName = input("Enterr your first name: ")
lastName = input("Enterr your last name: ")
print("student name: " + firstName + " " + lastName)

s = "Friday"
s1 = "Next Friday"
s2 = "Friday after next"
print(s.lower())
print(s1.lower())
print(s2.lower())
print(s,s1,s2)

s = "   Welcome to python"
print(s.lstrip())#Left side
print(s.rstrip())#ride side
print(.lstrip())#both
