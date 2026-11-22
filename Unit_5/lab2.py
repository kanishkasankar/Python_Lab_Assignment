# Lab Exercise 2: Library Management System
class Library:
    def __init__(self):
        self.books = ["Python Basics", "Data Structures", "Machine Learning"]
        self.borrowed = []

    def display_books(self):
        print("Available books:")
        for book in self.books:
            print("-", book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.borrowed.append(book)
            print("Book borrowed.")
        else:
            print("Book is not available.")

    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
            self.books.append(book)
            print("Book returned.")
        else:
            print("This book was not borrowed from this library.")

library = Library()
while True:
    print("\\n1. Display books  2. Borrow  3. Return  4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        library.display_books()
    elif choice == "2":
        library.borrow_book(input("Book name: "))
    elif choice == "3":
        library.return_book(input("Book name: "))
    elif choice == "4":
        break
    else:
        print("Invalid choice")
