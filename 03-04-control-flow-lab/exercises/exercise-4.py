# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = None
b = None
c = None
while a != 'quit':
  a = int(input('enter A: '))
  b = int(input('enter B: '))
  c = int(input('enter C: '))
  if(a == b and a == c):
    print(f"A triangle with sides of {a}, {b} & {c} is an equalateral triangle")
  elif(a != b and a != c and b != c):
    print(f"A triangle with sides of {a}, {b} & {c} is an scalene triangle")
  elif(a or b == c and a != b):
    print(f"A triangle with sides of {a}, {b} & {c} is an isosceles triangle")
  else:
    pass

