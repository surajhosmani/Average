import sys

# Check if 5 marks are provided
if len(sys.argv) != 6:
    print("Usage: python student_grade.py <m1> <m2> <m3> <m4> <m5>")
    sys.exit()

# Read marks from command line
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
m3 = float(sys.argv[3])
m4 = float(sys.argv[4])
m5 = float(sys.argv[5])

# Calculate average
average = (m1 + m2 + m3 + m4 + m5) / 5

# Grade calculation
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 35:
    grade = "D"
else:
    grade = "Fail"

# Output
print("\n----- Student Result -----")
print("Average Marks:", average)
print("Grade:", grade)
