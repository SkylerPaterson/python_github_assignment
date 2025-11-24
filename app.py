# Welcome message
print("Welcome to my Python program!")

# Ask the user for study hours
hours = input("How many hours did you study today?")

# Convert input to a number with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculate weekly hours
weekly_hours = hours * 7

# Display the result
print(f"You are on track to study {weekly_hours} hours this week.")