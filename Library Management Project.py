class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"the book {self.title} is borrowed")
        else:
            print(f"sorry! the book {self.title} is already borrowed by another one")


    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print(f"the book {self.title} has been returned")
        else:
            print(f"the book {self.title} is not borrowed")


    def show_details(self):
         status = "Available" if not self.is_borrowed else "borrowed"
         print(f"Title: {self.title} Author: {self.author} Status: {status}")

class Library():
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f"the book {book.title} by {book.author} added to the library.")


    def show_books(self):
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            book.show_details()


    def borrow_book(self,title):
        for book in self.books:
            if book.title==title:
                book.borrow()
                return
            print(f"the book {title} is not available in the library")

    def return_book(self,title):
        for book in self.books:
            if book.title==title:
                book.return_book()
                return
            print(f"the book {title} is not found in the library")

    

            




my_library = Library("City Library")

book1=Book("1984","George Orwell")
book2=Book("To Kill a MochingBird","Harper Lee")
book3=Book("The Great Gatsby","F. Scott Fitzgerald")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.borrow_book("1984")
my_library.show_books()

my_library.borrow_book("1984")


my_library.return_book("1984")
my_library.show_books()

my_library.borrow_book("Moby Dick")
