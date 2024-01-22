# --------------------------------
# Title: CS50 Python - Lecture 1 - Conditionals
# Date: 
# --------------------------------


# 1 - Boolean Expressions (yes / no)
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
  print("x is less than y")
if x > y:
  print("x is greater than y")
if x == y:
  print("x is equal to y")

# 2 - Can we improve upon this??
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
  print("x is less than y")
elif x > y:            # only run this code if statement above is false
  print("x is greater than y")
elif x == y:           # only run this code if statement above is false
  print("x is equal to y")

# 3 - Final improvements (Logically finish the search)
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
  print("x is less than y")
elif x > y:            # only run this code if statement above is false
  print("x is greater than y")
else:           # this must be true if previous statements are false
  print("x is equal to y")



# 4 - Or Statements
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
  print("x is not equal to y")
else:
  print("x is equal to y")


# 5 - Let's improve upon this using - (Not equal to) 
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
  print("x is not equal to y")
else:
  print("x is equal to y")
