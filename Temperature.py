"""
Write a Program in Python to convert temperature from Fahrenheit to Celsius & Vice Versa.
"""
print("Choose 1 for Fahrenheit to Celsius")
print("Choose 2 for Celsius to Fahrenheit")
choice = int(input("Enter your choice: "))
if choice == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
else:
    print("Invalid choice!")
