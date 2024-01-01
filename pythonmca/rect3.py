class Rectangle:
 def __init__(self, length, width):
  self._length = length # Private attribute
  self._width = width # Private attribute
 def area(self):
  return self._length * self._width
 def __lt__(self, other):
  return self.area() < other.area()
length= int (input("enter the number"))
width=int(input("enter a number"))
length1= int (input("enter the number"))
width2=int(input("enter a number"))
if Rectangle < Rectangle:
 print("Area of Rectangle 1 is smaller than the area of Rectangle 2.")
elif Rectangle > Rectangle:
 print("Area of Rectangle 1 is larger than the area of Rectangle 2.")
else:
 print("Both rectangles have the same area.")
