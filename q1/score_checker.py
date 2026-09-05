#Asking for the student's score and storing it in the variable score
score = int(input("Enter student score:"))

#Stating that if the score is less than 0 or greater than 100 it is an ivalid score.
if 0<score<100:
  print("Invalid")

#Classifications of scores
elif score >=90:
  print("Outsranding")

elif score >=80:
  print("Very Satisfactory")

elif score >=75:
  print("Satisfactory")

#Stating that any score below 75 will be considered as Needs Improvement
else:
  print("Needs Improvement")
