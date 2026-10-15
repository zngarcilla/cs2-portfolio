def calculate_total(price, quantity):
  return price * quantity

def calculate_change(payment, total):
  return payment - total

price = float(input("What is the price of your order?:"))
quantity = int(input("How many items did you get of your order?:"))
payment = float(input("How much did you pay?:"))


total = calculate_total(price, quantity)
change = calculate_change(payment, total)

print("Total cost of order in PHP is:", total)

if change >= 0:
  print ("Change in PHP", change)
  
else:
  more = change * -1
  print(" You need to pay", change, " more in PHP")

