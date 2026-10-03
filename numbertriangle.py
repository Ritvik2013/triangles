print("Welcome to the triangle world")
rows=int(input("How many rows of numbers do you want to print?"))
numbers=1

for i in range(1,rows+1):

    for j in range(1,i+1):
        print(numbers,end=' ')
    numbers=numbers+1
    print()