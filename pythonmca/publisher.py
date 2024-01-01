class Publisher:
 def __init__(self, name):
  self.name = "love"
class Book(Publisher):
 def __init__(self, name, title, author):
  super().__init__(name) 
  self.title = "love for ever"
  self.author = "beema"
 def display_info(self):
  print("Publisher:", self.name)
  print("Title:", self.title)
  print("Author:", self.author)
class Python(Book):
 def __init__(self, name, title, author, price, no_of_pages):
  super().__init__("O""Reilly","Python Crash Course","Eric Matthes", 29.99, 544) # Invoking the base class (Book) constructor
  self.price = price
  self.no_of_pages = no_of_pages
def display_info(self): 
 super().display_info() 
 print("Price:", self.price)
 print("Number of Pages:", self.no_of_pages)
