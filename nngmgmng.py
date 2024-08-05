import calendar

# Prompt the user for a year and month number
y = int(input("Enter the year: "))
m = int(input("Enter the month number: "))

# Print the calendar for the specified month and year
print(calendar.month(y, m))
