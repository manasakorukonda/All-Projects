from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if min(rect.lowleft.x, rect.upright.x) < self.x < max(rect.lowleft.x, rect.upright.x) and min(rect.lowleft.y,
                                                                                                      rect.upright.y) < self.y < max(
            rect.lowleft.y, rect.upright.y):
            return 0
        elif rect.lowleft.x == self.x or rect.upright.x == self.x or rect.lowleft.y == self.y or rect.upright.y == self.y:
            return 1
        else:
            return -1

    def distance_from_point(self, point):
        dist = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) * 0.5
        print("The distance from ({},{}) to ({},{}) is {}".format(self.x, self.y, point.x, point.y, dist))


class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright
        self.breadth = max(self.lowleft.x, self.upright.x) - min(self.lowleft.x, self.upright.x)
        self.length = max(self.lowleft.y, self.upright.y) - min(self.lowleft.y, self.upright.y)

    def length_of_rectangle(rect):
        # print("The length of the rectangle is {} and the breadth is {}".format(max(rect.lowleft.x,rect.upright.x) - min(rect.lowleft.x,rect.upright.x),max(rect.lowleft.y,rect.upright.y)-min(rect.lowleft.y,rect.upright.y)))
        print("The length of the rectangle is {} and the breadth is {}".format(rect.length, rect.breadth))

    def area_of_the_rectangle(rect):
        print("The area of the rectangle is: {}".format(rect.length * rect.breadth))


class GuiRectangle(Rectangle):

    def draw(self, canvas):

        canvas.penup()
        if min(self.lowleft.x, self.upright.x) == self.lowleft.x:
            canvas.goto(self.lowleft.x, self.lowleft.y)
        else:
            canvas.goto(self.upright.x, self.upright.y)
        canvas.pendown()
        canvas.forward(self.breadth)
        canvas.left(90)
        canvas.forward(self.length)
        canvas.left(90)
        canvas.forward(self.breadth)
        canvas.left(90)
        canvas.forward(self.length)

class Guipoint(Point):

    def draw(self, canvas,size = 5,color ='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.dot(size,color)

# Create GUI Rectangle object
rectanglex = GuiRectangle(Point(randint(0,400), randint(0, 400)), Point(randint(0, 400), randint(0, 400)))

# Print the Cordinates of Rectangle
print("The rectangle coordinates are: ({},{}),({},{})".format(rectanglex.lowleft.x, rectanglex.lowleft.y,
                                                             rectanglex.upright.x, rectanglex.upright.y))
# Print the dimensions of rectangle
rectanglex.length_of_rectangle()

# Print the area of rectangle
rectanglex.area_of_the_rectangle()

# User point initializing
x, y = input("Please provide a point x and y: ").split()

# Create GUI point object
point = Guipoint(int(x), int(y))

# Check if point falls inside or outside or on the rectangle
if point.falls_in_rectangle(rectanglex) == 0:
    print("The point:({},{}) is inside the rectangle".format(point.x, point.y))
elif point.falls_in_rectangle(rectanglex) == 1:
    print("The point:({},{}) is on the rectangle".format(point.x, point.y))
else:
    print("The point:({},{}) is outside the rectangle".format(point.x, point.y))

# Setting the canvas Size and color
turtle.screensize(-0,0,'white')

# Creating the turtle object for drawing the graphics
my_turtle = turtle.Turtle()

# Drawing the Rectangle
rectanglex.draw(canvas = my_turtle)

# Drawing the Point
point.draw(canvas = my_turtle)

# This is used to keep the screen for display
turtle.done()