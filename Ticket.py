"""
WAP to check movie ticket amount as
per age wise.
"""
age = int(input("Enter your age: "))
if age < 3:
    print("Your ticket is free.")
elif age < 12:
    print("Your ticket is $10.")
else:
    print("Your ticket is $15.")
