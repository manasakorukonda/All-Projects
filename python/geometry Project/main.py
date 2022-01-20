from point import *
from random import randint
from rectangle import *

rectanglex = Rectangle(Point(randint(0,9),randint(0,9)),Point(randint(0,9),randint(0,9)))
print("The rectangle coordinates are: ({},{}),({},{})".format(rectanglex.lowleft.x,rectanglex.lowleft.y,rectanglex.upright.x,rectanglex.upright.y))
rectanglex.length_of_rectangle()
rectanglex.area_of_the_rectangle()
x,y = input("Please provide a point x and y: ").split()
point = Point(int(x),int(y))
if point.falls_in_rectangle(rectanglex):
  print("The point:({},{}) is inside the rectangle".format(point.x,point.y))
else:
  print("The point:({},{}) is outside the rectangle".format(point.x,point.y))


