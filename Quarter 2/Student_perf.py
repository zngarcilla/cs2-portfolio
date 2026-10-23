def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3)/3
  

def get_performance(average):
  if 85 <= average <=100:
    return "Mastery"
  elif 70 <= average < 85:
    return "Developing"
  else:
    return "Needs Review"

def is_eligible(average, completed_tasks):
  return average >= 85 and completed_tasks >= 3


score1 = int(input("Enter score 1:"))
score2 = int(input("Enter score 2:"))
score3 = int(input("Enter score 3:"))
completed_tasks = int(input("Completed tasks(0-5):"))

avg = calculate_average(score1, score2, score3)
performance = get_performance(avg)
eligible = is_eligible(avg, completed_tasks)

print(f"Average: {avg:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")

#1. calculate_average returns a number. get_performance returns a string. is_eligible returns True or False.
#2. calculate_average works out the average and sends it back. The main part of the program stores that value, then passes it to get_performance.
#3. The student is not eligible. Both conditions must be true: average 85 or higher and at least 3 tasks completed. One without the other is not enough.
#4. return sends the actual value back so you can use it anywhere in your program. print only shows text on the screen and the value cannot be used again. return makes functions useful in more than one place.
