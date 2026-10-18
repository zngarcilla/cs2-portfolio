def calculate_total(price, quantity):
  return price * quantity

def calculate_change(payment, total):
  return payment - total

price = float(input("What is the price of your order?:"))
quantity = int(input("Enter quantity:"))
payment = float(input("How much did you pay?:"))


total = calculate_total(price, quantity)
change = calculate_change(payment, total)

print("Total cost: PHP", total)

if change >= 0:
  print ("Change: PHP", change)
  
else:
  more = change * -1
  print(" You need to pay PHP", more, " more")

#1. What does each function do?
#    - `calculate_total()` finds the total price by multiplying the cost per item by how many items were bought.
#    - `calculate_change()` figures out how much money to give back by subtracting the total cost from the cash paid.

# 2. What is the difference between parameters and arguments?
#    - Parameters are placeholders written in the function setup line. They tell the function what kind of data it needs to receive.
#    - Arguments are the real numbers entered by the user that get sent into the function when it actually runs.
#
# 3. Where is the returned total stored, and how is it reused?
#    - The total is stored in a variable called `total`.
#    - I reuse it to calculate the customer's change and to print the final message on the screen.
#
# 4. Why use two separate functions instead of one?
#    - It keeps the code more organized. Each function has exactly one job. 
#    - This makes the program much easier to fix if something goes wrong, or to change more things later.
