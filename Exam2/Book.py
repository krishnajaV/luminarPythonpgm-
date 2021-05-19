# Create a Book class with instance Library_name, book_name, author, pages?class Employee():
class Book:
    def details(self ,library_name,book_name,auther,page):
        self.library_name= library_name
        self.book_name= book_name
        self.auther=auther
        self.page=page
        print("libraryname=", self.library_name)
        print("bookname=", self.book_name)
        print("auther=", self.auther)
        print("page=", self.page)


ob=Book()
ob.details("alarvadi", "Mathil","vhgh",125)