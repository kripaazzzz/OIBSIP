name = input("Enter your name: ")

# weight and height input 
w = float(input("Enter weight(in kgs): "))
h = float(input("Enter height(in cms):"))

# height conversion in m
h = h/100

# BMI calculation
BMI = w/(h*h)

# user info
print(name)
print(w)
print(h)
print(BMI)

# BMI categories
if(BMI<18.5):
  print("Underweight")

elif(BMI>=18.5 and BMI<25):
  print("Normal Weight")

elif(BMI>=25 and BMI<30):
  print("Overweight")

elif(BMI>=30 and BMI<35):
  print("Obese")

elif(BMI>=35 and BMI<40):
  print("Extremely Obese")

elif(BMI>=40):
  print("Morbidly Obese")
  
else:
  print("Enter valid input.")
