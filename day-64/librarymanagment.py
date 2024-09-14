class library():
    def __init__(self):
        self.noofbooks=0
        self.books=[]
    def addBooks(self,book):
        self.books.append(book)
        self.noofbooks=len(self.books)
    def show(self):
        print(f"library has {self.noofbooks} books and books are")
        for book in self.books:
            print(book)

l1=library()
l1.addBooks("the mountain")
l1.addBooks("the girnar")
l1.addBooks("mistry of the sea")
l1.show()