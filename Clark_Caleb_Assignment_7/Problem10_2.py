#Prompt the user to enter the string from the console
s = input("Enter numbers sperated by 1 space")

#Exctract items from the string
items = s.string()

#L.C to convert items to numbers
numbers = [eval(x) for x in items]

#We can use the reverse method in the list class
numbers.reverse()

#Display results
print(numbers)
