"""
Write a Program in Python to Swap the values of two Variables.
(Using a 3rd Variable & without Using a 3rd Variable).
"""
# Using a 3rd Variable
print("Swapping values using a 3rd variable:")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Before swapping: a =", a, "b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)
# Without Using a 3rd Variable
print("Swapping values without using a 3rd variable:")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("Before swapping: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)
