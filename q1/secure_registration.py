name = input("Enter name:")
if name == "":
  print("Student name is required.")
  name_valid = False
else:
  name_valid = True

club = input("Enter club name:").title()  
if club in ["Robotics", "Science", "Mathematics", "Programming"]:
  club_valid = True
else:
  print("Please choose a valid club.")
  club_valid = False

email = input("Enter email:")
email_valid = False
if "@" and "." in email:
    email_valid = True
  
attendance = input("Attendance status:").title()  
if attendance in ["Absent", "Late", "Present"]:
  attendance_valid = True
else:
  print("Please choose a proper status.")
  attendance_valid = False

if name_valid and club_valid and email_valid and attendance_valid:
  print("\nREGISTRATION ACCEPTED")
  print(f"Student: {name}")
  print(f"Section:")
  print(f"Club: {club}")
  print(f"Email: {email}")
  print(f"Attendance:"{attendance})
