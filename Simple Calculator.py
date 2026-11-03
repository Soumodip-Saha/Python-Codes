"""
Write a Program in Python to Make a Simple Calculator 
(Taking two Inputs & calculate their Addition, 
Subtraction, Multiplication, Division, 
Remainder Division, floor division or 
integer division and Power).
"""
# Taking two inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Performing calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"
if num2 != 0:
    remainder_division = num1 % num2
else:
    remainder_division = "undefined (division by zero)"
if num2 != 0:
    floor_division = (int)(num1 // num2)
else:
    floor_division = "undefined (division by zero)"
power = num1 ** num2
# Displaying the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Remainder Division:", remainder_division)
print("Floor Division:", floor_division)
print("Power:", power)
