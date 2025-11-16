Weight = float(input("Weight (kg): "))
Height = float(input("Height (m): "))
bmi = Weight / (Height * Height )

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
