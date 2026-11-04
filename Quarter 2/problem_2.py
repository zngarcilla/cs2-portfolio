day1 = float(input("Enter hours volunteered in day 1:"))
day2 = float(input("Enter hours volunteered in day 2:"))
day3 = float(input("Enter hours volunteered in day 3:"))
quiz_score = int(input("Enter quiz score:"))

def calculate_total_hours(day1, day2, day3):
  return day1 + day2 + day3

total_hours = calculate_total_hours(day1, day2, day3)

 
def get_participation_level(total_hours):
  if 8 <= total_hours :
    return "Highly Active"
  elif 5 <= total_hours < 8:
    return "Active"
  else:
    return "Needs Improvement"

participation_level = get_participation_level(total_hours)

def is_certificate_eligible(total_hours, quiz_score):
  return total_hours >= 8 and quiz_score >= 80

certificate_eligibility = is_certificate_eligible(total_hours, quiz_score)


print(f"Total hours volunteered: {total_hours}")
print(f"Participation Level: {participation_level}")
print(f"Eligible for Certificate of Active Participation: {certificate_eligibility}")
