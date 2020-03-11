#This section prompts the user for the input of their weight and height
pounds = float(input("Please enter your weight in pounds: "))
print("Enter your height, separately, in feet and inches...")
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

#This section preforms conversions from standard to metric
kilos = pounds*0.454
total_inches = (feet*12)+inches
meters = (total_inches*0.0254)

#This section calculates and prints the user's BMI
BMI = kilos/(meters**2)
print("Your BMI is:", BMI)

#The section tells the user their classifaction
if BMI < 18.5:
    print("Your classifaction is UNDERWEIGHT")
elif BMI >= 18.5 and BMI < 25:
    print("Your classifaction is NORMAL WEIGHT")
elif BMI >= 25 and BMI < 30:
    print("Your classifaction is OVERWEIGHT")
elif BMI >= 30:
    print("Your classifaction is OBESE")