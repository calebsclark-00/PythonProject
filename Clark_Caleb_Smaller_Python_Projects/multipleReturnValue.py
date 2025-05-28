def sort(num1,num2):
    if num1 < num2:
        return num1, num2
        else:
            return num2, num1

def main():
    n1,n2 = sort(3.2)
    print(f"n1 is {n1} and n2 is {n2}")
main()
