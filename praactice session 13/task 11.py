class Library:
    def __init__(self):
        self.books = []

    def add_new(self, title, author):
        book = {"title": title, "author": author, "borrowed": False}
        self.books.append(book)
        print(f"'{title}' by {author} has been added to the library.")

    def borrow(self, title):
        for book in self.books:
            if book['title'] == title and not book['borrowed']:
                book['borrowed'] = True
                print(f"You have borrowed '{title}'.")
                return
        print(f"'{title}' is not available or already borrowed.")

    def display(self):
        available_books = [book for book in self.books if not book['borrowed']]
        if not available_books:
            print("No books are available in the library right now.")
        else:
            print("Available books in the library:")
            for book in available_books:
                print(f"- '{book['title']}' by {book['author']}")


obj = Library()


obj.add_new("The Great Gatsby", "F. Scott Fitzgerald")
obj.add_new("1984", "George Orwell")



obj.display()
obj.borrow("1984")
obj.display()
