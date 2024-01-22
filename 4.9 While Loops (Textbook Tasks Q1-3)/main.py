# ----------------------------
# Title: Textbook Tasks 1 - 3
# Date:
# ----------------------------



### Task 1
# task 1
'''
counter = 1000
total = 0

while(counter <= 1500):
  print(counter)
  counter+=1
  total = total + counter

print("Total: ", total)



### Task 2
counter = 0
total = 0

while counter < 6:
  numbers = int(input("Enter a number: "))
  counter += 1
  total += numbers

print("The six numbers total: ",total, "the average is: ", total/6)
'''


### Task 3
username = input("Enter Username: ")

while username != "Maureen":
  username = input("Wrong username - re-enter username: ")

print("Thank you ", username)

password = input("Enter Password: ")

while password != "abc123":
  password = input("Wrong password - re-enter password: ")
  
print("Access Granted!")





