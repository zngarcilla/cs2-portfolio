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

attendance = input("Attendance status:").title()  
if attendance in ["Absent", "Late", "Present"]:
  attendance_valid = True
else:
  print("Please choose a proper status.")
  attendance_valid = False
