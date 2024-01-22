# ------------------------
# Title: Guessing Game
# Date: 
# ------------------------

import random

number = random.randint(1,10)
guess = 0

guess = int(input("Pick a number: "))

while guess != number:
  if guess < number:
    print("Too low")
   
  elif guess > number:
    print("Too high")
    
  else:
    print("Correct")
    break
  guess = int(input("Pick a number: "))

print("The number was", number) # shows random number selected