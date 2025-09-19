class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")
