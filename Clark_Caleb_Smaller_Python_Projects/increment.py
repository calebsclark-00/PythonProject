def main():

    x = 1
    print(f"Before the call, x is {x}")
    increment(x)
    print(f"After the call, x is {x}")
def increment(n):
    n += 1
    print(f"\tn inside the increment is {n}")
main()

x = 4
y = x

print(id(x), x)
print(id(y), y)

y = y + 1
print(id(y), y)
