from figure import square,triangle
#using square module
side=int(input("side of the square:"))
print ("area of a square:",square.area(side))
print ("perimeter of a square:",square.perimeter(side))
#using triangle module
breadth=int(input("enter a breadth:"))
height=int(input("enter a height:"))
print ("area of a triangle:",triangle.area(breadth,height))
a=int(input("enter a :"))
b=int(input("enter b:"))
c=int(input("enter c:"))
print ("perimeter of a triangle:",triangle.perimeter(a,b,c))
