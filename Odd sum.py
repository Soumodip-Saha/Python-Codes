"""
Write a Program in Python to find the sum of the following series
S=1 + 3 + 5 + 7 + . . . . . + Up to Nth Term (Input N).
"""
n = int(input("Enter a number : "))
total_sum = 0
if n < 0:
    print("Sum of negative number not possible !!!!")
else:
    for i in range(1, 2 * n, 2):
        total_sum += i
    print("The sum of", n, "terms is", total_sum)
