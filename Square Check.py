"""
WAP to take values of length and breadth 
of a rectangle from user and check if 
it is square or not.
"""
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
if l == b:
    print("The rectangle is a square.")
else:
    print("The rectangle is not a square.")
