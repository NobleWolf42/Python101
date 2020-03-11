size = int(input("Enter multiplication table size: "))
for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(row*column, " ", end="")
    print()

