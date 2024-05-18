class library:
    def __init__(self):
        self.no_of_books = 0
        self.books =[]
    def addbook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    
    def result(self):
        print(f"\nlibrary has {self.no_of_books} books and those books are - \n")
        
        for book in self.books:
         print(book)
    
number = library()
number.addbook("atomic habits")
number.addbook("Healthy habits")
number.addbook("Unhealthy habits")


 
     
number.result()