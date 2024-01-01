from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid,sphere
# using rectangle module
len1=int(input("enter the length:"))
wid=int(input("enter the width:"))
print ("area of rectangle:",rectangle.area(len1,wid))
print("perimeter of the rectangle:",rectangle.perimeter(len1,wid))
#using circle module
rad=int(input("enter the radius:"))
print("area of circle:",circle.area(rad))
print("perimeter of circle:",circle.perimeter(rad))
#using cuboid module
len2=int(input("enter the length:"))
wid2=int(input("enter the width:"))
hei=int(input("enter the height:"))
print("surfacearea of cuboid:",cuboid.surfacearea(len2,wid2,hei))
print("volume of cuboid:",cuboid.volume(len2,wid2,hei))
#using sphere module
rad2=int(input("enter the radius:"))
print("surfacearea of sphere:",sphere.surfacearea(rad2))
print("volume of sphere:",sphere.volume(rad2))

