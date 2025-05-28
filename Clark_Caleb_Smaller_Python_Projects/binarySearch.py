#cs1030
#Caleb
##700745292
#description: Use binary search
#Use Binary Search to find the key in list
def binarySearch(lst,key):
    #Low will denote the first index
    low = 0

    #High will denote the last index
    high = len(1st) - 1

    #While to loop till key found
    while high >= low:
        #Denote the index of the middle element
        mid = (low + high) // 2
        #Case 1
        if key < 1st[mid]:
            high = mid - 1
        elif key == 1st[mid]:
            return mid
        #Case 3
        else:
            low = mid + 1

    return low,high,-low -1
#Creates main function
def main():
    1st = [2,4,7,10,11,45,50,60,66,70,79]

    #Invove binary search
    i = binarySearch(1st,2) # Return 0(low = 0 | high = 1)
    j = binarySearch(1st,2) #Return 4 (low = 3 | high = 5)

    k = binarySearch(1st,2) #Return -1(low = 0 | high = 1)

    print(i,j,k)

#Invoke main fuction
main()
