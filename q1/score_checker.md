# **Improvised Student Score Checker**

## *Name: Zoe Naomi G. Arcilla*
## *Grade & Section: 8 Dahlia*

### **Activity Overview:**
 In this activity I learned how to improve a program by making it more organized and efficient. I also added necessary restrictions that were missing in the original code.
 The program is a Student Score Checker classifies grades as follows: a score of 90-100 is ‘Outstanding’, 80-89 is ‘Very Satisfactory’, 75-79 is ‘Satisfactory’. Any score below 75 (but greater or equal to 0) is classified as ‘Needs Improvement’.
 The acceptable input must be between 0-100, otherwise, the score is be classified as ‘Invalid’.

 ### **Part 1: Analyzing Logic**
 **Input:** What information does the program need?
>The numerical score number entered by the user.

**Boundaries:**
 
 What is the minimum valid score?
>The minimum valid score is 0.

What is the maximum valid score?
>The maximum valid score is 100.

**Possible Outputs:** What outcomes can the program produce?
>“Outstanding” for scores 90-100.
>“Very Satisfactory” for scores 80-89.
>“Satisfactory” for scores 75-19.
>“Needs Improvement” for scores lower than 75 that is greater or equal to 0.
>“Invalid” for scores greater than 100 and lower than 0.

**Selection Patterns:**

Which part uses a boundary condition?
>The part that makes sure the score is between 0-100.

Which part uses multiple decision paths?
>The step that picks the classification based on the score.

### **Part 2: Flowchart**
I created a flowchart that shows the logic of my program.
Here is the flowchart I made: [score_checker_flowchart.png](q1/score_checker_flowchart.png)
