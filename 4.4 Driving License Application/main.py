# ----------------------------------
# Title: Drivers License Application
# Date:
# ----------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("You can apply for your test!")
elif age >= 16 and age < 18:
    print("Would you like to apply for your provisonal?")
else:
    print("Stick to the bike kid")
