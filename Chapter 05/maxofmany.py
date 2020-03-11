# Allow the user to enter an arbitrary number of nonnegative
# integers.  The user terminates the list with a negative integer.

in_value = 0
max = -1
sum = 0
while in_value >= 0:
    in_value = int(input("Enter a nonnegative integer (-1 quits): "))
    if max < in_value:
        max = in_value
    if in_value >= 0:
        sum += in_value
if (max > -1):
    print("Maximum value entered:", max)
    print("Sum of the numbers is:", sum)
else:
    print("You entered no nonnegative numbers")
