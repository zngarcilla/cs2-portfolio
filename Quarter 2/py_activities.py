# Exercise 1

for i in range (2, 21, 2):
  print (i)

# Exercise 2

number = 10

while number >= 1:
  print(number)
  number -=1

print("Time is up!")

# Exercise 3

for i in range (1,16):
  if i % 3 == 0:
    continue
  print (i)

# Exercise 4

def show_table(number):
  for i in range (1, 11):
    result = num * i
    print (f"{num} x {i} = {result}")

num = int(input("Enter number:"))

show_table(num)
