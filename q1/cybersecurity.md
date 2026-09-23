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
> Less data obtained means less harm can be done. It also protects a user’s privacy.
--- 
# Part C - Security-Focused Validation Rules 
Complete the table before writing your program. 
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message | 
|---|---|---|---|---|---| 
| Student Name | any non-empty text| fake names | “”| Must not be empty| “Student name is required.”| 
| Section | "Diamond", "Emerald", "Sapphire", "Jade", "Dahlia", "Ilang-ilang", "Sampaguita", "Rosal", "Beryllium", "Platinum", "Silicon", "Magnesium", "Photon", "Graviton", "Gluon", "Electron", "Biology", "Chemistry", "Physics", "Bio-Chemistry"| typos or inconsistent formatting|”Wala class” | Must be in the list of sections given |”Please choose a valid section” | 
| Club Choice | Programming or Robotics or Science or Mathematics| misspellings/typos| “prougrsmminf” | Must be one of the 4 clubs given |”Please choose a valid club” | 
| School Email | any text containing @ and .| fake emails, typos, personal emails | “email ko”, “nakalimutan ko na”| Should contain both @ and . | “Please enter valid email”| 
| Attendance Status | Present or Late or Absent| typos, inconsistent answers | “here”, “anditooo akooo”| Must be exactly Present, Late, or Absent|”Please enter either Present, Late, or Absent.” | 
--- 
## Secure Data Capture Questions 
### 1. What should your program accept? 
> Name: any non empty text,  Sections: "Diamond", "Emerald", "Sapphire", "Jade", "Dahlia", "Ilang-ilang", "Sampaguita", "Rosal", "Beryllium", "Platinum", "Silicon", "Magnesium", "Photon", "Graviton", "Gluon", "Electron", "Biology", "Chemistry", "Physics", "Bio-Chemistry", Club:"Robotics", "Science", "Mathematics", "Programming", School email: any text with @ and ., Attnedance: “Present”, “Late”, “Absent”
### 2. What should your program reject? 
> Empty inputs in student name, invalid formatting, typos, invalid emails, and unnecessary data.
### 3. How do your validation rules help reduce incorrect or unsafe input? 
> It helps in checking inputs against the restrictions give, blocking the incorrect entries before they enter the system. 
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

 
## Security Practices Applied 
### Required Input 
> I checked if the user’s name is empty with if name == “”. If the user’s input is blank a message saying “Student name is required” will pop up.
### Allowed Values 
> Sections: Only accepts Diamond, Emerald, Jade, Sapphire, Dahlia, Ilang-ilang, Rosal, Sampaguita, Beryllium, Magnesium, Platinum, Silicon, Electron, Gluon, Graviton, Photon, Biology, Chemistry, Physics, Bio-chemistry.
> Clubs: Only accepts Programming, Robotics, Science, Mathematics.
> Attendance status: Only accepts Absent, Late, Present.
### Format Check 
> The email must contain the symbols “@“ and “.”. It is a basic format check so students will not put wrong inputs.
### Error Messages 
> It is useful so the students will know what went wrong and why their registration was not accepted. 
### Data Minimization 
> I did not collect passwords, OTPs, banking information, or any personal information. I only asked what is needed for the club registration, protecting others’ privacy and decreasing the chances of risk happening
--- 
# Part E - Testing and Reflection 
## Testing 
| Test | Input Situation | Expected Output | Actual Output | Result | 
|---:|---|---|---|---| 
| 1 | All data valid | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED |PASS| 
| 2 | Blank student name | Student name is required. & REGISTRATION NOT ACCEPTED|Student name is required. & REGISTRATION NOT ACCEPTED |PASS | 
| 3 | Invalid section |Please pick a valid section. & REGISTRATION NOT ACCEPTED | Please pick a valid section. & REGISTRATION NOT ACCEPTED| PASS|
| 4 | Invalid club choice | Please choose a valid club. & REGISTRATION NOT ACCEPTED| Please choose a valid club. & REGISTRATION NOT ACCEPTED| PASS| 
| 5 | Email missing `@` |Please put a proper email. & REGISTRATION NOT ACCEPTED | Please put a proper email. & REGISTRATION NOT ACCEPTED| | 
| 6 | Email missing `.` |Please put a proper email. & REGISTRATION NOT ACCEPTED | Please put a proper email. & REGISTRATION NOT ACCEPTED|PASS | 
| 7 | Invalid attendance status | Please choose a proper status. & REGISTRATION NOT ACCEPTED| Please choose a proper status. & REGISTRATION NOT ACCEPTED|PASS | 
| 8 | Different valid inputs | REGISTRATION NOT ACCEPTED| REGISTRATION NOT ACCEPTED|PASS | 
Use: 
- **PASS** if the actual result matches the expected result. 
- **FAIL** if it does not. 
--- 
# Reflection 
### 1. What is one cybersecurity threat that can affect an application or user? 
> Phishing can affect a user or application. Fake information or login pages tricks users to enter their personal information .
### 2. How can users reduce the risk of phishing or suspicious messages? 
> Users shouldn’t click any link they see, should check if an email is from a valid organization and never share information like a password through emails.
### 3. How can validation rules improve the security of user input? 
> Validation rules improve the security because it filters dangerous data before the program processes it. It blocks invalid formats and wrong inputs, preventing incorrect data from entering.
### 4. Why should a program avoid collecting unnecessary personal information? 
> Because extra data means extra risk. The more information stored, the more there is to lose if the system gets leaked or hacked.  
### 5. How did SG7's input validation concepts become security practices in SG8? 
> In SG 7 I learned how to properly put validation rules and in SG 8 I learned that I can put what I’ve learned in SG 7 to create security practices.
--- 

