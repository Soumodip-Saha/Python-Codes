"""
Write a Program in Python to find the sum of the following series
S=1+1/2 + 1/4 + 1/8 + 1/16 + . . . . . + 1/ 2N (Input N).
"""
n = int(input("Enter number of terms : "))
total_sum = 0
if n < 0 :
    print("Sum of negative number is not possible !!!! ")
else :
    for i in range(n):
        total_sum += 1/(2**i)
    print("The sum of ",n,"terms is",total_sum)
