"""
Write a Program in Python to Print the Reverse of a Number.
"""
num = int(input("Enter a number : "))
if num < 0:
    print("Reverse of negative number is not possible !!!!")
else:
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = (reverse_num * 10) + digit
        num //= 10
    print("The reverse of the number is", reverse_num)
