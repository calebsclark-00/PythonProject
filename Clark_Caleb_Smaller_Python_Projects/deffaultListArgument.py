'''
#Create a add function where you append the value in list
def add(x, 1st = []):
    #Check if x is not in list
    if x not in 1st:
        1st.append(x)
    #Return 1st back to coller
    return 1st
'''
def add(x, 1st = None):
    if 1st == None:
        1st = []

    if x is not 1st:
        1st.append(x)

#Create main function
def main():
    #Invoke add
    list1 = add(1)
    print(list1)

    list1 = add(2)
    print(list2)

    list1 = add(3)
    print(list3)
    
    list1 = add(4)
    print(list4)

main()
