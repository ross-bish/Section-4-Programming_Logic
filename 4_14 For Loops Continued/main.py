# ----------------------------
# Title: For Loop  - Recap
# Date:
# ----------------------------

sentence = input("Enter a sentence: ")
space = " "
count = 0

for letter in sentence:
  if letter == " ":
    count += 1

print("number of spaces = ", count)
