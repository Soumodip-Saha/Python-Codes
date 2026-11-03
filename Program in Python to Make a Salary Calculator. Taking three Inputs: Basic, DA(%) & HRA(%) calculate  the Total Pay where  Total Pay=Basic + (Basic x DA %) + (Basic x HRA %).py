"""
Write a Program in Python to Make a Salary Calculator.
Taking three Inputs: Basic, DA(%) & HRA(%) calculate 
the Total Pay where 
Total Pay=Basic + (Basic x DA %) + (Basic x HRA %).
"""
basic = float(input("Enter Basic Salary: "))
da_percentage = float(input("Enter DA percentage: "))
hra_percentage = float(input("Enter HRA percentage: "))
da_amount = (basic * da_percentage) / 100
hra_amount = (basic * hra_percentage) / 100
total_pay = basic + da_amount + hra_amount
print(f"Total Pay is: {total_pay:.2f}")
