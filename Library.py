class Library:

    def __init__(self, books, author, name):
        self.books = books
        self.author = author
        self.name = name
        self.booksdata = {}
        self.secretkey1 = 'hi hello'
        self.secretkey2 = 'it is a secret'

    def displaybooks(self):
        print(f"Welcome to {self.name}... We have the following {len(self.books)} books in our library:")

        a = 0
        while a <= len(self.books) - 1:
            print(f"{a + 1}: {self.books[a]} by {self.author[a]}")
            a += 1

        # for i in self.books:
        #    print(i)

    def actiontoperform(self):
        a = 1
        while a == 1:
            ask = input(
                "What do you wanna do...'i' Issue book, 'r' Return book, 'g' Give a book to library, 'd' Delete a book, 'b' Book-User Database:")
            if ask == 'i':
                self.issuebook()
            elif ask == 'r':
                self.returnbook()
            elif ask == 'g':
                self.givebook()
            elif ask == 'd':
                self.deletebook()
            elif ask == 'b':
                self.userbookinfo()

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
            if askkey == self.secretkey1:
                bookname = input('name the book')
                self.books.remove(bookname)
                print(self.books)
            else:
                print('wrong key')

    def userbookinfo(self):
        askkey = input('enter the secret key')
        if askkey == self.secretkey2:
            print(self.booksdata)
        else:
            print('wrong key')


Shreya = Library(['A Christmas Carol', 'Oliver Twist', 'The Secret Garden',
                  'Great Expectations', 'Harry Potter', 'Sherlock Holmes', 'A Tale of Two Cities'],
                 ['Charles Dickens', 'Charles Dickens', 'Frances Hodgson Burnett', 'Charles Dickens', 'J. K. Rowling',
                  'Sir Aurther Conan Doyale', 'Charles Dickens'], "Shreya's Library")

Shreya.displaybooks()
Shreya.actiontoperform()
