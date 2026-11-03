"""
S=1 + 2 + 3 + 4 + . . . . . + N (Input N).
"""
n = int(input("Enter a number : "))
sum = 0
if n < 0:
    print("Sum of negative number not possible !!!!")
else:
    for i in range(1, n + 1):
        sum += i
    print("The sum of", n, "is", sum)
