__author__ = 'Landon Stoner'

#This section generates the variables for passing and failing students
passing = 0
failing = 0
GPA = 0

#This section prompts the user for the student grades
print('Please enter the grades of each student. (Entering "Z" ends data entry.)')
grade = ""
while grade != "Z":
    grade = input()
    grade = grade.upper()

#This section takes the input grade and increases number of passing or failing students, It also adds to the GPA
    if grade == "A":
        passing = passing + 1
        GPA = GPA + 4
    elif grade == "B":
        passing = passing + 1
        GPA = GPA + 3
    elif grade == "C":
        passing = passing + 1
        GPA = GPA + 2
    elif grade == "D":
        passing = passing + 1
        GPA = GPA + 1
    elif grade == "F":
        failing = failing + 1

#This section calculates the percents of passing and failing students and the class GPA
totalstudents = float(passing) + float(failing)
passingdecimal = passing / totalstudents
passingpercent = passingdecimal * 100
failingdecimal = failing / totalstudents
failingpercent = failingdecimal * 100
averageGPA = GPA / totalstudents

#This section prints the final data
print("Students Passing: ", passing, " (", round(passingpercent, 2), "%)", sep="")
print("Students Failing: ", failing, " (", round(failingpercent, 2), "%)", sep="")
print("\n")
print("Class GPA:", round(averageGPA, 2))
