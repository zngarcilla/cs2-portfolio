# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Zoe Naomi G. Arcilla
**Section:** 8 Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements

| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error |Message |
|---|---|---|---|---|---|----|
| Student Name | Any non-empty text | Presence| “”| must not be empty| Student name is required.|
| Age | 11, 12, 13, 14, 15, 16, 17, 18 | Data type + Range |”twenty”, 19 | between range 11 to 18|Integers between 11 and 18 | Age must be a number and a number between 11 to 18.
| Grade Level | 7, 8, 9, 10, 11, 12 | Acceptable value | 78, N | between range 7 to 12 and must be an integer | Invalid grade level | The workshop is designed exclusively for those grade levels. Limiting to exact values prevents typos and entries for grades that do not participate.|
| Email Address | Any text with @ symbol | Singular pattern | studentyes, whatddddd| 
text containing the @ symbol | Must contain the symbol @| Email must contain @ |
| Registration Code | Exactl 6 characters | length | 239054384848, what | Must have exactly 6 characters of code | Registration code must have 6 digits |
---
## Validation Questions
### 1. Why should the student name not be blank?
> So every registration can be linked to a specific student, we can’t identify who’s registering.
### 2. Why should age be checked for both data type and range?
> First we must ensure it is actually a number so further checks work. Then we check the range because this workshop is only for ages 11–18; anyone outside that range is not eligible.
### 3. Why should grade level only accept specific values?
> The design is exclusively for g7 to 12 students.
### 4. What format requirements did you use for the email address?
> The email must contain @ symbol.
### 5. What length requirement did you use for the registration code?
> Exactly 6 characters.
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Flowchart
Insert your flowchart below.
![Workshop Validator Flowchart](workshop_validator_flowchart.png)
OR
## Pseudocode

START

 
  DISPLAY "Enter student name:"
  
  READ name
  
  IF name IS EMPTY THEN
  
    DISPLAY "Student name is required."
    
    name_valid = FALSE
    
  ELSE
  
    name_valid = TRUE
    
  END IF
 
  DISPLAY "Enter age:"

  READ age_text

  IF age_text IS A NUMBER THEN

    age_number = CONVERT age_text TO INTEGER

    IF age_number >= 11 AND age_number <= 18 THEN

      age_valid = TRUE
 
   ELSE
   
      DISPLAY "Age must be from 11 to 18."
      
      age_valid = FALSE
      
    END IF
    
  ELSE
  
    DISPLAY "Age must be a number."
    
    age_valid = FALSE
    
  END IF

 
  DISPLAY 
  “Enter grade level:"
  
  READ grade
  
  IF grade IS ONE OF: 7, 8, 9, 10, 11, 12 THEN
  
    grade_valid = TRUE
    
  ELSE
    DISPLAY "Invalid grade level."
    
    grade_valid = FALSE
    
  END IF

 
  DISPLAY "Enter email:"
  
  READ email
  IF email CONTAINS "@" THEN
  
    email_valid = TRUE
    
  ELSE
    email_valid = FALSE
    
  END IF

 
  DISPLAY "Enter registration code:"

  READ code
  
  IF LENGTH(code) == 6 THEN
  
    code_valid = TRUE
    
  ELSE
    DISPLAY "The registration code must contain exactly 6 characters."
    
    code_valid = FALSE
    
  END IF

 
  IF name_valid AND age_valid AND grade_valid AND email_valid AND code_valid THEN
  
    DISPLAY "REGISTRATION ACCEPTED"
    
    DISPLAY "Student: " + name
    
    DISPLAY "Age: " + age_number
    
    DISPLAY "Grade Level: " + grade
    
    DISPLAY "Email: " + email
    
    DISPLAY "Registration Code: " + code
    
  ELSE
  
    DISPLAY "REGISTRATION NOT ACCEPTED"
    
  END IF

END


# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
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
---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> Write your answer here.
### Data Type Validation
Explain where you used data type validation.
> Write your answer here.
### Range Validation
Explain where you used range validation.
> Write your answer here.

### Acceptable Value Validation
Explain where you used acceptable value validation.
> Write your answer here.
### Pattern Validation
Explain the simple pattern rule you used.
> Write your answer here.
### Length Validation
Explain the length rule you used.
> Write your answer here.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---|---|---|---|---|---|
| 1 | All inputs valid | Normal case | REGISTRATION ACCEPTED + details| Registration accepted + details| PASS|
| 2 | Blank student name | Presence |Student name is required. REGISTRATION  NOT ACCEPTED |Student name is required. REGISTRATION  NOT ACCEPTED|PASS |
| 3 | Age = `fourteen` | Data type | Age must be a number. REGISTRATION  NOT ACCEPTED|Age must be a number. REGISTRATION  NOT ACCEPTED |PASS |
| 4 | Age = `11` | Minimum boundary |REGISTRATION  ACCEPTED |REGISTRATION ACCEPTED |PASS |
| 5 | Age = `18` | Maximum boundary |REGISTRATION ACCEPTED |REGISTRATION ACCEPTED | PASS|
| 6 | Age = `10` | Range | Age must be from 11 to 18. REGISTRATION NOT ACCEPTED| Age must be from 11 to 18. REGISTRATION NOT ACCEPTED|PASS |
| 7 | Grade Level = `13` | Acceptable value | Invalid grade level. REGISTRATION NOT ACCEPTED| Invalid grade level. REGISTRATION NOT ACCEPTED| PASS|
| 8 | Email = `studentpshs.edu.ph` | Pattern | No @ symbol. REGISTRATION NOT ACCEPTED|No @ symbol. REGISTRATION NOT ACCEPTED | PASS|
| 9 | Registration Code = `ABC` | Length | Registration code must be exactly 6 characters. REGISTRATION NOT ACCEPTED| Registration code must be exactly 6 characters. REGISTRATION NOT ACCEPTED |PASS |
| 10 | Registration Code = `CS2026` | Valid length | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED| PASS|
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.

```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 2
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
