"""Write a Python program to convert 
a given string to title case (the first 
letter of each word is capitalized).
Note: Avoid using the title() function"""
s = input("Enter a string: ")
s = s.split()
for i in s:
    print(i.capitalize(), end = " ")
print()
