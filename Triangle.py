"""
Suppose a, b, and c denotes the lengths of the sides of a triangle. Then the area of the
triangle can be calculated using the formula: 
Area = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2
write a program that asks the user to input the length of sides of the triangle and print the
area.
"""
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the triangle:", area)
