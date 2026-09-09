name = str(input("Enter student name:"))
if name == "":
  print("Invalid")
  name_valid = False
else:
  print("Valid")
  name_valid = True

age = input("Enter age, it must be a number from 11 to 18:")
if age.isdigit():
  print("Valid")
  age_v = True
  agee = int(age)
else:
  print("Invalid")
  age_v = True

if agee > 18 or agee < 11:
  print("Invalid")
  age_v = False
  

grade = int(input("Enter grade level, must be from 7 to 12:"))
if grade > 12 or grade < 7:
  print("Invalid grade level")
  grade_v = False
else:
  print("Valid")
  grade_v= True

email = str(input("Enter email, must contain @"))
if "@" in email:
  print("Valid")
  e_v = True
else:
  print("Invalid")
  a_v = False

code = str(input("Enter code"))  
if len(code) == 6:
  print("Valid")
  code_v = True
else:
  print("Invalid")
  code_v = False

if name_valid and age_v and grade_v and code == "Valid":
  print("REGISTRATION ACCEPTED")
else:
  print("REGISTRATION NOT ACCEPTED")
