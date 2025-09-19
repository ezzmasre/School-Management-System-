class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"\nCourse: {self.name}")
        for student in self.students:
            student.display()
