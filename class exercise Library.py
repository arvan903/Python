class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author


    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    

    def borrow(self):
        print(f"The Book {self.get_title()} by {self.get_author()} has been borrowed")

    def show_details(self):
        print(f"the book name is: {self.get_title()} and author name is: {self.get_author()}")

class Ebook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def show_details(self):
        super().show_details()
        print(f"File Size: {self.file_size} MB")

class AudioBook(Book):
    def __init__(self, title, author,duration):
        super().__init__(title, author)
        self.duration = duration

    def show_details(self):
        print(f"The AudioBook Name is: {self.get_title()}, Author Name is: {self.get_author()}, Duration Name is: {self.duration} Hours")


general_book = Book("Lord of The Ring","Robert JJ")
ebook = Ebook("Cat in Dog World","Mew",2.1)
audiobook=AudioBook("Wild Forest","Donald J Trump",23)

general_book.borrow()
ebook.show_details()
audiobook.show_details()

    




