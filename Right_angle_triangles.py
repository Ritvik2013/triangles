print("Welcome to patterns.")
n=int(input("How many (*) do you want to print in a row?"))

for i in range(n):

    for j in range(i+1):
        print("*",end=" ")
    print()