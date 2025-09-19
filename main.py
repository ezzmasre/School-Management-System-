from student import Student
from teacher import Teacher
from course import Course
from school import School

# ---------------- MAIN PROGRAM ---------------- #
school = School("Green Valley")

# Add Students
while True:
    name = input("\nEnter student name (or 'stop' to finish): ")
    if name.lower() == "stop":
        break
    age = int(input("Enter age: "))
    grade = int(input("Enter grade (0-100): "))
    s = Student(name, age, grade)
    school.add_student(s)

# Add Teachers
school.add_teacher(Teacher("Mr. Smith", "Math"))
school.add_teacher(Teacher("Ms. Johnson", "Science"))

# Create a Course and Assign Students
math_course = Course("Mathematics")
for s in school.students:
    math_course.add_student(s)

school.add_course(math_course)

# Show Data
school.show_all()
