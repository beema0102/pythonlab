class Rectangle:
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
 def area(self):
  return self.length*self.breadth
 def perimeter(self):
  return 2*(self.length+self.breadth)
 def compare_area(self, other_rectangle):
  if self.area() > other_rectangle.area():
    return "The first rectangle has a larger area"
  elif self.area() < other_rectangle.area():
    return "The second rectangle has a larger area"
  else:
    return "Both rectangles have the same area"
 def compare_perimeter(self, other_rectangle):
  if self.perimeter() > other_rectangle.perimeter():
    return "The first rectangle has a larger perimeter"
  elif self.perimeter() < other_rectangle.perimeter():
    return "The second rectangle has a larger perimeter"
  else:
    return "Both rectangles have the same perimeter"
   
length=int(input("enter the 1st length:"))
breadth=int(input("enter the 1st breadth:"))
length1=int(input("enter the 2nd length:"))
breadth2=int(input("enter the 2nd breadth:"))
rectangle1=Rectangle(length,breadth)
rectangle2=Rectangle(length1,breadth2)
print("area of 1st rectangle:",rectangle1.area()) 
print("perimeter 1st of rectangle:",rectangle1.perimeter())	
print("Area of 2nd Rectangle :", rectangle2.area())
print("Perimeter of 2nd Rectangle :", rectangle2.perimeter())
comparison_result = rectangle1.compare_area(rectangle2)
print(comparison_result)
comparison_result1 = rectangle1.compare_perimeter(rectangle2)
print(comparison_result1)
