name = str(input("Enter student name:"))
if name == "":
  print("Invalid")
else;:
  print("Valid")

age = input("Enter age, it must be a number from 11 to 18:")
if age.isdigit():
  print("Valid")
  agee = int(age)
else:
  print("Invalid")

if agee >= 18 or agee =< 11:
  print("Invalid")

grade = int(input("Enter grade level, must be from 7 to 12:"))
if grade >= 12 or grade =< 7:
  print("Invalid grade level")
else:
  print("Valid")

email = str(input("Enter email, must contain @"))
if "@" in email:
  print("Valid")
else:
  print("Invalid")

code = str(input("Enter code"))  
if len(code) == 6:
  print("Valid")
else:
  print("Invalid")
