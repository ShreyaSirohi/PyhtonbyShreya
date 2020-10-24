class Library:

    def __init__(self, books, name):
        self.books = books
        self.name = name
        self.booksdata = {}
        self.secretkey = 'hi hello'

    def displaybooks(self):
        print(f"Welcome to {self.name}'s Library...We have the following books in our library {self.books}")

    def actiontoperform(self):
        a = 1
        while a == 1:
            ask = input("What do you wanna do...'i' issue book, 'r' return book, 'g' give a book to library, 'd' delete a book")
            a += 1
            if ask == 'i':
                self.issuebook()
            elif ask == 'r':
                self.returnbook()
            elif ask == 'g':
                self.givebook()
            elif ask == 'd':
                self.deletebook()

    def issuebook(self):
        username = input('Enter your name:')
        bookname = input(f"Name the book you wanna take, {username}")
        if bookname in self.books:
            if bookname not in self.booksdata:
                self.booksdata[bookname] = username
                print(f"OK {username}...Here is your book '{bookname}'")
            else:
                print(f'This book has already been taken by {self.booksdata[bookname]}')
        else:
            print(f"Sorry...we don't have this book in our library.")

    def returnbook(self):
        ask = input('Wanna return a book:')
        if ask == 'y':
            name = input("Enter your name")
            bookname = input('Enter the book name:')
            print(f"OK {name}...you have given your book '{bookname}' back to the library")
            del self.booksdata[bookname]

    def givebook(self):
        ask = input('Wanna give a book to library')
        if ask == 'y':
            name = input("Enter your name")
            bookname = input('Enter the book name:')
            self.books.append(bookname)
            print(self.books)

    def deletebook(self):
        ask = input('Wanna delete a book from the library')
        if ask == 'y':
            name = input("Enter your name")
            askkey = input('enter the secret key')
            if askkey == self.secretkey:
                bookname = input('name the book')
                self.books.remove(bookname)
                print(self.books)
            else:
                print('wrong key')


Shreya = Library(['A Christmas Carol', 'Oliver Twist', 'The Secret Garden',
                  'Great Expectations', 'Harry Potter', 'Sherlock Holmes', 'A Tale of Two Cities'], 'Shreya')
Shreya.displaybooks()
Shreya.actiontoperform()
