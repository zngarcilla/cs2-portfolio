name = input("Enter name:")
if name == "":
  print("Student name is required.")
  name_valid = False
else:
  name_valid = True

section = input("Enter section:").title()
valid_sections = ["Diamond", "Emerald", "Sapphire", "Jade", "Dahlia", "Ilang-ilang", "Sampaguita", "Rosal", "Beryllium", "Platinum", "Silicon", "Magnesium", "Photon", "Graviton", "Gluon", "Electron", "Biology", "Chemistry", "Physics", "Bio-Chemistry"]
if section in valid_sections: 
  section_valid = True
else:
  print("Please pick a valid section")
  section_valid =False


club = input("Enter club name:").title()  
if club in ["Robotics", "Science", "Mathematics", "Programming"]:
  club_valid = True
else:
  print("Please choose a valid club.")
  club_valid = False

email = input("Enter email:")

if "@" and "." in email:
    email_valid = True
else:
  email_valid = False
  print("Please put an appropriate email.")
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
  print(f"Attendance:{attendance}")
else:
  print("\nREGISTRATION NOT ACCEPTED")
