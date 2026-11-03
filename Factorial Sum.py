"""
Write a Program in Python to find the sum of the following series
S= 1! + 2! + 3! + 4! + . . . . . + N! (Input N)
"""
n = int(input("Enter number of terms : "))
total_sum = 0
if n < 0:
    print("Sum of negative numbers is not possible !!!! ")
else:
    for i in range(1, n + 1):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        total_sum += factorial
    print("The sum of", n, "terms is", total_sum)
    
