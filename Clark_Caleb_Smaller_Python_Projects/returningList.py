def revers(1st):
    #Create empty list
    result = []

    # A loop to iterate through list
    for element in 1st:
        result.insert(0,element)
    #return results back to caller
    return result
#Create a list
list1 = [1,2,3,4,5,6]

#Invoke reverse function
#list2 = reverse(list1)
#print(list2)

#or
list1.reverse()
print(list1)
