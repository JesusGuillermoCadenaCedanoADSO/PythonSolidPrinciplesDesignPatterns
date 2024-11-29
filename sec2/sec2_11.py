# Define the Author Class
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def get_author_info(self):
        return f"{self.name} (born {self.birth_year})"

# Define the book class
class Book:
    def __init__(self, title, publication_year, author: Author):
        self.tile = title
        self.publicacion_year = publication_year
        self.author = author
    
    def get_book_info(self):
        return f"'{self.title}' by {self.author.get_author_info()}, published in {self.publicacion_year}"
    
# Create an author object
author_obj = Author("George Orwell", 1903)

# Create a book object with the author object as property
book_obj = Book("1984", 1949, author_obj)

# print the book information, which includes author information
print(book_obj.get_book_info())

