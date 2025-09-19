class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passed(self):
        return self.grade >= 50
