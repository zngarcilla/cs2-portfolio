name = input("Enter student name:")
if name == "":
    print("Student name is required.")
    name_valid = False
else:
    name_valid = True

age_input = input("Enter age:")
age_valid = False
age_value = 0

if age_input.isdigit():
    age_value = int(age_input)
    if 11 <= age_value <= 18:
        age_valid = True
    else:
        print("Age must be from 11 to 18.")
else:
    print("Age must be a number.")

grade = input("Enter grade level:")
grade_valid = False
if grade in ("7", "8", "9", "10", "11", "12"):
    grade_valid = True
else:
    print("Invalid grade level.")

email = input("Enter email:")
email_valid = False
if "@" in email:
    email_valid = True

reg_code = input("Enter registration code:")
code_valid = False
if len(reg_code) == 6:
    code_valid = True
else:
    print("The registration code must contain exactly 6 characters.")

if name_valid and age_valid and grade_valid and email_valid and code_valid:
    print("REGISTRATION ACCEPTED")
    print(f"Student: {name}")
    print(f"Age: {age_value}")
    print(f"Grade Level: {grade}")
    print(f"Email: {email}")
    print(f"Registration Code: {reg_code}")
else:
    print("REGISTRATION NOT ACCEPTED")
