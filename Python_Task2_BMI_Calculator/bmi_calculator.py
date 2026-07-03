name = input("Enter your name: ")

# weight and height input 
w = float(input("Enter weight(in kgs): "))
h = float(input("Enter height(in cms):"))

if w <= 0 or h <= 0:
  print("Enter valid input.")

else:
  # height conversion in m
  h = h/100

  # BMI calculation
  BMI = w/(h*h)
  
  # user info
  print("Name:", name)
  print("Weight:", w)
  print("Height:", h)
  print("BMI:", round(BMI,2))
  
  # BMI categories
  if(BMI<18.5):
    print("Underweight")
  
  elif(BMI>=18.5 and BMI<25):
    print("Normal Weight")
  
  elif(BMI>=25 and BMI<30):
    print("Overweight")
  
  else:
    print("Obese")
  
