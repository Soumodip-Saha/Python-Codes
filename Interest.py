"""
Write a program in Python to calculate Simple Interest & Compound Interest.
Simple Interest (SI) = (P × R × T)/100  
Where P = Principal Amount, R = Rate per Annum, T = Time (years)  
Compound Interest (CI) CI=P(1+R/100)^T
Where P = Principal Amount, R = Rate per Annum, T = Time (years) 
"""
print("Choose 1 for Simple Interest")
print("Choose 2 for Compound Interest")
choice = int(input("Enter your choice: "))
if choice == 1:
    principal = float(input("Enter Principal Amount (P): "))
    rate = float(input("Enter Rate of Interest (R) in %: "))
    time = float(input("Enter Time (T) in years: "))
    simple_interest = (principal * rate * time) / 100
    print(f"Simple Interest is: {simple_interest:.2f}")
elif choice == 2:
    principal = float(input("Enter Principal Amount (P): "))
    rate = float(input("Enter Rate of Interest (R) in %: "))
    time = float(input("Enter Time (T) in years: "))
    compound_interest = principal * (1 + rate / 100) ** time - principal
    print(f"Compound Interest is: {compound_interest:.2f}")
else:
    print("Invalid choice!")
    
