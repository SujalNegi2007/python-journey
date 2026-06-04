class book:
    def __init__(self,author,available,title,pages = None):
        self.author = author
        self.available = available
        self.title = title
        self.pages = pages
    def __str__(self):
        return f"Book : {self.title} | Author : {self.author} | Available : {self.available} | Pages : {self.pages}"
    def __repr__(self):
        return f"\n+------------------------------+\nBook : {self.title}\nAuthor : {self.author}\nAvailable : {self.available}\nPages : {self.pages}\n+------------------------------+\n"
    def __lt__(self, other):
        return self.pages > other.pages

class ebook(book):
    def __init__(self,author,available,title,pages,size):
        super().__init__(author,available,title,pages)
        self.size = size 
    def __str__(self):
        return f"Ebook : {self.title} | Author : {self.author} | Available : {self.available} | Pages : {self.pages} | Size : {self.size}"
    def __repr__(self):
        return f"\n+------------------------------+\nEbook : {self.title}\nAuthor : {self.author}\nAvailable : {self.available}\nPages : {self.pages}\nSize : {self.size}\n+------------------------------+\n"
    
class audiobook(book):
    def __init__(self,author,available,title,size,length):
        super().__init__(author,available,title)
        self.size = size
        self.length = length
    def __str__(self):
        return f"Audiobook : {self.title} | Author : {self.author} | Available : {self.available} | Size : {self.size} | Length : {self.length}"
    def __repr__(self):
        return f"\n+------------------------------+\nAudiobook : {self.title}\nAuthor : {self.author}\nAvailable : {self.available}\nSize : {self.size}\nLength : {self.length}\n+------------------------------+\n"
