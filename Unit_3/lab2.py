# Lab Exercise 2: Student Grading System
name = input("Enter student name: ")
marks = []
for subject in range(1, 4):
    marks.append(float(input(f"Enter mark for subject {subject}: ")))

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\\nStudent:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
