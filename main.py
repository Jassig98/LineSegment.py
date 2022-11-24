# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 23 2022
# Description:

class Point:
    def __init__(self,x,y):
        self._x_coord = x
        self._y_coord = y
    def get_x_coord(self):
        return self._x_coord
    def get_y_coord(self):
        return self._y_coord
    def distance_to(self,p):
        x= (self._x_coord - p.get_x_coord())*(self._x_coord - p.get_x_coord())
        y= (self._y_coord - p.get_y_coord())*(self._y_coord - p.get_y_coord())
        return (x+y)**0.5

class LineSegment:
    def __init__(self,ep1,ep2):
        self._endpoint_1 = ep1
        self._endpoint_2 = ep2
    def length(self):
        return self.endpoint_1.distance_to(self._endpoint_2)
    def slope(self):
        x=self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord()
        y=self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()
        return y/x
    def is_parallel_to(self,line_seg_2):
        if self.slope() == line_seg_2.slope():
            return True
        else:
            return False