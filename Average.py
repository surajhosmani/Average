import sys
if len(sys.argv) != 6:
    print("Usage: python student_grade.py <m1> <m2> <m3> <m4> <m5>")
    sys.exit()

m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
m3 = float(sys.argv[3])
m4 = float(sys.argv[4])
m5 = float(sys.argv[5])
average = (m1 + m2 + m3 + m4 + m5) / 5
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
