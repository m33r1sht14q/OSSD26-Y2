print("Enter marks of 10 students")

total_marks=0
passed_students=0
failed_students=0
highest_marks = -1

for i in range(1,11):
     while True:
       marks = int(input(f"Enter marks of student {i}: "))

       if 0<=marks<=100:
           break

       else:
           print("Enter marks again betweem (0-100)")

           total_marks+=marks
     if marks>highest_marks:
         highest_marks=marks

     if 90 <= marks <= 100:
         grade = "A"
     elif 80 <= marks <= 89:
         grade = "B"
     elif 70 <= marks <= 79:
         grade = "C"
     elif 60 <= marks <= 69:
         grade = "D"
     else:
         grade = "F"

     if marks >= 50:
         passed_students += 1
     else:
         failed_students += 1

     print(f"Student {i} Grade: {grade}\n")

class_average = total_marks / 10

print("--- Final Class Summary ---")
print(f"Passed Students (>= 50): {passed_students}")
print(f"Failed Students (< 50): {failed_students}")
print(f"Highest Mark in Class: {highest_marks}")
print(f"Class Average Mark: {class_average:.2f}")

