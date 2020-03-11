#Here are the varibles that need to be defined prior to use
done = False
t = int(0)
passing = int(0)
failing = int(0)
tl = ""

letter = input("Please input the letter grade here (Z will terminate the List):")
letter = letter.upper()
#Here is the looping input statement
while not done:
    if letter == "A":
        t = t+4
        tl = tl+letter
        passing = passing+1
    elif letter == "B":
        t = t+3
        tl = tl+letter
        passing = passing+1
    elif letter == "C":
        t = t+2
        tl = tl+letter
        passing = passing+1
    elif letter == "D":
        t = t+1
        tl = tl+letter
        passing = passing+1
    elif letter == "F":
        t = t+0
        tl = tl+letter
        failing = failing+1
    else:
        pass
    letter = input()
    letter = letter.upper()
    if letter == "Z":
        done = True
    else:
        pass

#This gives the percentage of students passing and failing
ts = passing+failing
passper = round(float((passing/ts)*100), 2)
failper = round(float((failing/ts)*100), 2)

#GPA Calculation
GPA = round(t/ts, 2)

#This prints the data
print("There are ", passing," students passing.(",  passper,"%)", sep="")
print("There are ", failing," students failing.(",  failper,"%)", sep="")
print("The class GPA is:", GPA)