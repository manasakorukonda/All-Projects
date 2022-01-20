class Point:

  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def falls_in_rectangle(self,rect):
    if min(rect.lowleft.x,rect.upright.x) < self.x < max(rect.lowleft.x,rect.upright.x) and min(rect.lowleft.y,rect.upright.y) < self.y < max(rect.lowleft.y,rect.upright.y):
      return True;
    else:
      return False;
  
  def distance_from_point(self,point):
    dist = ((self.x - point.x)**2 + (self.y - point.y)**2 )*0.5
    print("The distance from ({},{}) to ({},{}) is {}".format(self.x , self.y,point.x,point.y,dist))
  
  
