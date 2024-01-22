# -----------------------
# Title: 
# Date: 
# -----------------------

'''
# Task 1 - For Loop
for i in range(1, 11):
    print(i)

# Task 1 - While Loop
i = 1
while i <= 10:
    print(i)
    i += 1

'''
'''
# Task 2
value = int(input("Enter a value: "))

for i in range(1, value+1):
    if i % 2 != 0:
        print(i)

# Task 2 - Alternative 
value = int(input("Enter a value: "))

for i in range(1, value+1, 2):
    print(i)

'''''
''''
# Task 3
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for letter in sentence:
    if letter in vowels:
        count += 1

print("Number of vowels in the sentence: ", count)

'''
'''
#Task 4
myPhrase = input("Enter a sentence to reverse: ")
reversePhrase = ""

for i in myPhrase:
    reversePhrase = i + reversePhrase  # use Thonny to debug this with class.

print(reversePhrase)

'''

#Task 5
sentence = input("Enter a sentence: ")
letter = input("Enter a single character: ")
count = 0

for i in sentence:
    if i == letter:
        count += 1

print("The character", letter, "appears", count, "times in the sentence.")

