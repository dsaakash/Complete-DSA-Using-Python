# Python  code to determine grades based on marks

# Given marks
marks = 54

# Determine grade
if marks < 25:
    print("Grade: F")
elif 25 <= marks <= 44:
    print("Grade: E")
elif 45 <= marks <= 49:
    print("Grade: D")
elif 50 <= marks <= 59:
    print("Grade: C")
elif 60 <= marks <= 69:
    print("Grade: B")
elif marks >= 70:
    print("Grade: A")
else:
    print("Invalid marks entered.")
