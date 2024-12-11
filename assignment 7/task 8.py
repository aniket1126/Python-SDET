class Book:
    def __init__(self, title):
        self.title = title
    def __del__(self):
        print(f"The book '{self.title}' is being deleted.")


obj = Book("Python Programming")
del obj
