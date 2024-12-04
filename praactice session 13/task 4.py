class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def modify_name(self, new_name):
        self.name = new_name

    def modify_marks(self, new_marks):
        self.marks = new_marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

obj1 = Student("Ansh", 46)
obj1.display()

obj1.modify_name("aniket")
obj1.modify_marks(90)
obj1.display()
