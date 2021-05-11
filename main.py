# Central Library Project


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("The Books available in this Library are : ")
        for book in self.books:
            print(" * "+book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(
                f"You have been issued {bookname}, remember to return it within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print(
                f"Sorry This book is either not available or it has already been issued by someone else, please wait until book is available ")
            return False

    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning this book, Hope you enjoyed reading it")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow : ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return : ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "dJango", "Clrs", "Python Notes"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\t \n======Welcome to Central Library======
        Please choose an option to continue :
        1. List all the books
        2. Request a book
        3. Add or Return the book
        4. Exit The Library
        '''
        print(welcomeMsg)
        a = int(input("Enter your Choice : "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks For using the Central Library, Have a great day ahead ..!")
            exit()
        else:
            print("Invalid Choice ..!")
