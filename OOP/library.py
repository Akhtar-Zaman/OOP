class book:
    def __init__(self):
        self.name = ''
        self.author = ''
        self.available = 0
        self.books = []

    def get_book(self):
        for i in self.available:
            print('Book: ', self.books[i][0])
            print('Author: ', self.books[i][1])
            

    def add_books(self):
        a = input("How many books you want to ADD: ")
        for i in range(1,int(a)+1):
            Book_Name= input('Please Enter Book Name: ')
            Author = input('please Enter Author Name: ')
            self.name = Book_Name
            self.author = Author
            self.books = self.books + [[self.name, self.author]]
            self.available += i
a = book()
a.add_books()
print(a.get_book())
