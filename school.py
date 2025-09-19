class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def show_all(self):
        print(f"\n=== {self.name} School Data ===")
        print("\nStudents:")
        for s in self.students:
            s.display()
        print("\nTeachers:")
        for t in self.teachers:
            t.display()
        print("\nCourses:")
        for c in self.courses:
            c.show_students()
