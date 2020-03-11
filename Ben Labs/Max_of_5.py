print("Please enter five integer values.")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
number3 = int(input("Number 3: "))
number4 = int(input("Number 4: "))
number5 = int(input("Number 5: "))
maxnumber = number1
if maxnumber < number2:
    maxnumber = number2
if maxnumber < number3:
    maxnumber = number3
if maxnumber < number4:
    maxnumber = number4
if maxnumber < number5:
    maxnumber = number5
print("The maximum number is:", maxnumber)