height = float(input("Height (meters): ")) #in meters
weight = float(input("Weight (KG): ")) #in KG

BMI = weight / height**2
BMI_round = round(BMI, 1) # int 

if(BMI_round <= 18.5):
    print(f"With a BMI of {BMI_round} you are declared Underweight")
    
elif(BMI_round < 25):
    print(f"With a BMI of {BMI_round} you are declared Normal Weight")

elif(BMI_round < 30):
    print(f"With a BMI of {BMI_round} you are declared Overweight")

elif(BMI_round < 35):
    print(f"With a BMI of {BMI_round} you are declared Obese")

else:
    print(f"With a BMI of {BMI_round} you are declared Clinically Obese")
