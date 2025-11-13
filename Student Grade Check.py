# -----------------------------------------------------
# Simple Student Check Program
# Purpose: 
#   - Demonstrates boolean values and operators
#   - Uses all six comparison operators (==, !=, >, <, >=, <=)
#   - Uses flow control (if, elif, else)
#   - Decides if a student is doing well based on their grade
# -----------------------------------------------------

# User input
grade = int(input("Enter your current grade (0-100): "))
attendance = int(input("Enter how many classes you missed: "))

# Boolean values and operators
good_attendance = attendance <= 3       # True if student missed 3 or fewer classes
passing_grade = grade >= 60             # True if grade is 60 or higher

# Using comparison operators
print("Grade comparison examples:")
print("Is your grade equal to 100?", grade == 100)
print("Is your grade NOT equal to 0?", grade != 0)
print("Is your grade greater than 70?", grade > 70)
print("Is your grade less than 50?", grade < 50)
print("Is your grade greater than or equal to 90?", grade >= 90)
print("Is your grade less than or equal to 60?", grade <= 60)

# Flow control using if, elif, else
if passing_grade and good_attendance:
    print("You are doing great! Keep it up!")
elif passing_grade and not good_attendance:
    print("Your grade is good, but try to attend more regularly.")
elif not passing_grade and good_attendance:
    print("Your attendance is good, but you need to raise your grade.")
else:
    print("You need to improve both your grade and attendance.")
