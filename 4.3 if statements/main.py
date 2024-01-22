# -----------------------------
# Title: 4.3 - If statements
# Date:
# -----------------------------
"""

# Challenge 1
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
if num1 > num2:
  print(num2, num1)
else:
  print(num1, num2)
  

  
# Challenge 2
num = int(input("Enter a number less than 20: "))

if num > 20:
  print("Too High")
else: 
  print("Thank you.")


# Challenge 3

# Version 1
number = int(input("Please enter a number between 10 and 20: "))

if number > 20:
  print("Incorrect answer")
elif number < 10:
  print("Incorrect answer")
else:
  print("Thank You.")

# Version 2
number = int(input("Please enter a number between 10 and 20: "))

if number >=10 and number <= 20:
  print("Thank You.")
else: 
  print("Incorrect Answer")


"""
  
  
# Challenge 4
fav_colour = input("Enter your favourite colour: ")

if fav_colour == "red" or fav_colour == "RED" or fav_colour == "Red":
 print("I like red too.")
else:
  print("I dont like", fav_colour, "I prefer red.")





# Challenge 5
raining = input("Is it raining? ")
raining = str.lower(raining)

if raining == "yes":
  windy = input("Is it windy? ")
  windy = str.lower(windy)
  if windy == "yes":
    print("It is too windy for an umbrella!")
  else: