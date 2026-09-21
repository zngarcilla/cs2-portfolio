# Fundamentals of Cybersecurity and Data Privacy 
**Activity:** PSHS Secure Club Registration System 

**Name:** Zoe Naomi G. Arcilla 

**Section:** 8 Dahlia 

**Quarter:** 1 

--- 
## Activity Overview 
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple PSHS Club Registration System. 
The goal is to create a program that collects only necessary information and accepts only correct, expected, and appropriate input. 
--- 
# Part A - Cybersecurity Threat Analysis 
## Assigned Case
**Case Number:** 1
**Case Title:** Fake Login Alert 
> The case shows an email asking to click a link to enter their username and password to enable their account.
--- 
### 1. What cybersecurity threat is shown? 
> Phishing, specifically credential phishing wherein scammers impersonate to be an official source to lure the user to type in their login information. 
### 2. What warning signs make the situation suspicious? 
> It states that the account will be disabled if not done and it asked to click a link where the information should be typed. 
### 3. What may be affected? 
Check or describe all that apply: 
- Data 
- Account 
- Application 
> Data could be affected since the information may be accessed, account has a risk to being taken over, and the login page may be impersonating.
### 4. What information could be exposed or misused? 
> The student’s username, password, and personal information in the account may be exposed. Scammers can use the information to log in to the real account, obtaining data and pretending to be the user.
### 5. What should the user do to reduce the risk? 
> To not click the link and type information. Go to an official website to check the account’s status, verify that the message actually came from an official source. If not, the student should report it.
--- 
# Part B - Data Privacy and Secure Data Capture 
A proposed Club Registration System wants to collect the following information. Determine whether each item is really necessary. 
| Data | Collect / Do Not Collect | Reason | 
|---|---|---| 
| Student Name | Collect | to identify who is registering| 
| Section | Collect | for class classification | 
| Club Choice | Collect | for club membership | 
| School Email | Collect | for communication | 
| Attendance Status | Collect | eligibility to join | 
| Password | Do Not Collect | creates security risks| 
| OTP | Do Not Collect | only for login verification| 
| Home Address | Do Not Collect | not needed in registration |
| Parent Bank Account | Do Not Collect | not needed in registration | 
--- 
## Privacy Question 
Why is it safer to collect only information that the program actually needs? 
> Less data obtained means less harm can be done. It also protects a users privacy.
--- 
# Part C - Security-Focused Validation Rules 
Complete the table before writing your program. 
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message | 
|---|---|---|---|---|---| 
| Student Name | any non-empty text| fake names | “”| Must not be empty| “Student name is required.”| 
| Section | sections specified by the teacher| typos or inconsistent formatting|”Wala class” | Must be in the list of sections given |”Please choose a valid section” | 
| Club Choice | Programming or Robotics or Science or Mathematics| misspellings/typos| “prougrsmminf” | Must be one of the 4 clubs given |”Please choose a valid club” | 
| School Email | any text containing @ and .| fake emails, typos, personal emails | “email ko”, “nakalimutan ko na”| Should contain both @ and . | “Please enter valid email”| 
| Attendance Status | Present or Late or Absent| typos, inconsistent answers | “here”, “anditooo akooo”| Must be exactly Present, Late, or Absent|”Please enter either Present, Late, or Absent.” | 
--- 
## Secure Data Capture Questions 
### 1. What should your program accept? 
> Write your answer here. 
### 2. What should your program reject? 
> Write your answer here. 
### 3. How do your validation rules help reduce incorrect or unsafe input? > Write your answer here. 
--- 
# Part D - Secure Program Implementation 
## Program 
Create a simple **PSHS Club Registration System**. 
The program should collect only: 
- Student Name 
- Section 
- Club Choice 
- School Email
- Attendance Status 
It should **not request passwords, OTPs, banking information, or unnecessary personal information**. 
--- 
## Source Code File 
[`secure_registration.py`](secure_registration.py) 
--- 
## Final Code 
```python 
# Paste your final program here. 
name = input("Enter name:")
if name == "":
  print("Student name is required.")
  name_valid = False
else:
  name_valid = True

section = input("Enter section:").title()
valid_sections = ["Diamond", "Emerald", "Sapphire", "Jade", "Dahlia", "Ilang-Ilang", "Sampaguita", "Rosal", "Beryllium", "Platinum", "Silicon", "Magnesium", "Photon", "Graviton" "Gluon", "Electron", "Biology", "Chemistry", "Physics", "Biochemistry"]
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
---

 
## Security Practices Applied 
### Required Input 
> Explain how you handled blank input. 
### Allowed Values 
> Explain which fields accept only predefined values. 
### Format Check 
> Explain your simple email validation rule. 
### Error Messages 
> Explain why clear error messages are useful. 
### Data Minimization 
> Explain what information you intentionally did NOT collect and why. 
--- 
# Part E - Testing and Reflection 
## Testing 
| Test | Input Situation | Expected Output | Actual Output | Result | 
|---:|---|---|---|---| 
| 1 | All data valid | | | | 
| 2 | Blank student name | | | | 
| 3 | Invalid section | | | |
| 4 | Invalid club choice | | | | 
| 5 | Email missing `@` | | | | 
| 6 | Email missing `.` | | | | 
| 7 | Invalid attendance status | | | | 
| 8 | Different valid inputs | | | | 
Use: 
- **PASS** if the actual result matches the expected result. 
- **FAIL** if it does not. 
--- 
# Reflection 
### 1. What is one cybersecurity threat that can affect an application or user? > Write your answer here. 
### 2. How can users reduce the risk of phishing or suspicious messages? > Write your answer here. 
### 3. How can validation rules improve the security of user input? > Write your answer here. 
### 4. Why should a program avoid collecting unnecessary personal information? > Write your answer here. 
### 5. How did SG7's input validation concepts become security practices in SG8? > Write your answer here. 
--- 

