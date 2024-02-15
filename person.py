'''
A python program to display book names,authors and title
'''
class Books:

#the constructors for thye class are;bookname,author,title
    def __init__(self,bookname,author):
        self.bookname=bookname
        self.author=author
      
book1=Books("python","silas")
print(book1.bookname,book1.author)    