"""
Write a Program in Python to find the sum of the following series
S= 1 - 1/3 + 1/9 - 1/27 + 1/81 - 1/243 .... Up to Nth Term.
"""
n = int(input("Enter the number of terms : "))
total_sum = 0
if n < 0:
    print("Sum of negative numbers not possible !!!")
else:
    for i in range(n):
        total_sum += ((-1)**i) * (1 / (3**i))         # (-1)**i automatically handles the alternating + and - signs
    print("The sum of", n, "terms is", total_sum)
