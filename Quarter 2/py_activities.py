# Exercise 1

for number in range (2, 21, 2):
  print (number)

# The first number in the parameter is the start, so it will start with 2. The 2md number in the paramater is the limit, meaning thr loop will end right before 20. Moreoever, 2 is the increment or step so the numbers will increase by 2 until it reaches 20. Printing (number) outputs each number following the rule.

# Exercise 2

number = 10

while number >= 1:
  print(number)
  number -=1

print("Time is up!")

#  The variable 'number' is 10 so it will start with 10. Then, the while function checkd if 'number' is greater than or equal to 1, as long as it is true, it will print the number and decrease it by 1. If 'number' is lower than 1, the loop stops and it will proceed to the final step which is printing "Time is up!".

# Exercise 3

for number in range (1,16):
  if number % 3 == 0:
    continue
  print (i)

# Similar to exercise 1, it will print the numbers between 1 to 15. However, it will undergo the process wherein if it is a multiple of 3. The number will be skipped because 'continue' tells python to skip that specific number but continuing the other numbers to be printed.

# Exercise 4

def show_table(number):
  for i in range (1, 11):
    result = num * i
    print (f"{num} x {i} = {result}")

num = int(input("Enter number:"))

show_table(num)

# It now involves a def function named show_table that accepts a parameter (number). Under the def function, there is a for loop that runs from 1 to 10, multiplying the given number by i to calculate the result and printing each step as a multiplication equation. Outside the function, the program asks a user to enter a number and calls show_table(num) to run the code and display the multiplication table. 
