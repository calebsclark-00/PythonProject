for i in range(NUM_OF_ELEMENTS):
    #value = evale(inpiut("Enter a new number: ")
    value = random.randint(1,20)
    numbers.append(value)

    sum += value

average = sum / NUM_OF_ELEMENTS

count = 0


for i in range(NUM_OF_ELEMENTS):
    if numbers[i] > average

    aboveAveNumbers.append(numbers[i])

    count += 1

aboveAveNumbers.sort()
print(aboveAveNumbers)
print(f"Average is {average}!")
print(f"Number of elements above the averahe {count}")

##################################################################
for x in range(len(numbers)):
    print(f"Iteration: {x} Element Value:
