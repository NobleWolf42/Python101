# Get the size of the table from the user
size = int(input("Enter multiplication table size: "))

# Print the column header numbers
print("     ", end="")
for column in range(1, size + 1):
    print("{:>4}".format(column), end="")
print()
# Print the separating line
print("    +", end="")
for column in range(1, size + 1):
    print("----", end="")
print()

# Print each row of the table
for row in range(1, size + 1):
    # Print the header for the row
    print("{:>3}".format(row), end=" |")

    # Print the line that makes up the row
    for column in range(1, size + 1):
        print("{:>4}".format(row*column), end="")
    print()

