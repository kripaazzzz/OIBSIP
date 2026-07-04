name = input("Enter your name: ")
 
w = float(input("Enter weight(in kgs): "))
h = float(input("Enter height(in cms):"))

if w <= 0 or h <= 0:
  print("Enter valid input.")

else:
  h = h/100 
  BMI = w/(h*h)
  
  print("Name:", name)
  print("Weight:", w, "kgs")
  print("Height:", h, "m")
  print("BMI:", round(BMI,2))
  
  if(BMI<18.5):
    print("Underweight")
  
  elif(BMI>=18.5 and BMI<25):
    print("Normal Weight")
  
  elif(BMI>=25 and BMI<30):
    print("Overweight")
  
  else:
    print("Obese")
  
