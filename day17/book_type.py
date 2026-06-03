class book:
    def __init__(self,author,available,title,pages = None):
        self.author = author
        self.available = available
        self.title = title
        self.pages = pages

    def display_info(self):
        print(f"Book : {self.title} | Author : {self.author} | Available : {self.available} | Pages : {self.pages}")

class ebook(book):
    def __init__(self,size,author,available,title,pages):
        super().__init__(author,available,title,pages)
        self.size = size
    
    def display_info(self):
        print(f"Ebook : {self.title} | Author : {self.author} | Available : {self.available} | Pages : {self.pages} | Size : {self.size}")

class audiobook(book):
    def __init__(self,author,available,title,size,length):
        super().__init__(author,available,title)
        self.size = size
        self.length = length
    
    def display_info(self):
        print(f"Audiobook : {self.title} | Author : {self.author} | Available : {self.available} | Size : {self.size} | Length : {self.length}")
