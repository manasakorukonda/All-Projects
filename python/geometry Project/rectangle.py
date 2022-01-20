class Rectangle:

  def __init__(self,lowleft,upright):
    self.lowleft = lowleft
    self.upright = upright
  
  def length_of_rectangle(rect):
    rect.length = max(rect.lowleft.x,rect.upright.x) - min(rect.lowleft.x,rect.upright.x)
    rect.breadth = max(rect.lowleft.y,rect.upright.y)-min(rect.lowleft.y,rect.upright.y)
    #print("The length of the rectangle is {} and the breadth is {}".format(max(rect.lowleft.x,rect.upright.x) - min(rect.lowleft.x,rect.upright.x),max(rect.lowleft.y,rect.upright.y)-min(rect.lowleft.y,rect.upright.y)))
    print("The length of the rectangle is {} and the breadth is {}".format(rect.length,rect.breadth))
  
  def area_of_the_rectangle(rect):
    print("The area of the rectangle is: {}".format(rect.length * rect.breadth))
