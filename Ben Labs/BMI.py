lbs = int(input("Please enter your weight in pounds: "))
print ("Next, enter your height in feet and inches . . .")
ft = int(input("Enter feet: "))
inc = int(input("Enter inches: "))
weight = float(lbs*0.454)
totalinches = float(inc+(ft*12))
height = float(totalinches*0.0254)
BMI = float(weight/(height*height))
print("Your BMI is:", BMI)
if BMI < 18.5 and BMI > 0:
    Class = "Underweight"
elif BMI >= 18.5 and BMI < 25:
    Class = "Normal Weight"
elif BMI >= 25 and BMI < 30:
    Class = "Overweight"
elif BMI >= 30:
    Class = "Obese"
else:
    print("Error")
print("Your classification is:",Class)