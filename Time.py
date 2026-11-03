"""
Write a program that accepts seconds from keyboard as integer. Your program should
convert seconds in hours, minutes and seconds. Your output should like this:
Enter seconds: 13400 (Hours: 3 Minutes: 43 Seconds: 20) 
"""
time = int(input("Enter seconds: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print("Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
