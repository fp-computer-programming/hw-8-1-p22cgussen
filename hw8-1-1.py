# Author CCG 12/9/21

def bmi_calc(h,w):
    bmi = (int(w) / int(h) ** 2) * 1000

    if bmi < 19:
        return("You are underweight")
    elif bmi < 25:
        return("You are healthy")
    elif bmi < 25:
        return("You are overweight")
    elif bmi < 25:
        return("You are obese")
    else:
        return("You are very obese")

height = input("What is your height in centimeters?")
weight = input("What is your weight in kilograms?")

print(bmi_calc(height,weight))

print(bmi_calc(150,75) == "You are underweight")
print(bmi_calc(150,100))
# == "You are underweight")
print(bmi_calc(175,200))
# == "You are underweight")
