from math import sqrt

x1 = float(input('Enter x1:'))
y1 = float(input('Enter y1:'))
x2 = float(input('Enter x2:'))
y2 = float(input('Enter y2:'))

difference_x = x2 - x1
difference_y = y2 - y1

squared_x = pow(difference_x, 2)
squared_y = pow(difference_y, 2)

distance = sqrt(squared_x + squared_y)

print(f'The distance between 2 points is:{round(distance, 2)}')

# The math library helped me to not dolve longer problems. 
# It provides ready-to-use functions.
# I have also learned that you can't use sqrt() directly, unless you put from math import sqrt, in cases where you put import math you may use math.sqrt 
