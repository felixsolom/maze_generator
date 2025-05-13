from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2) 
        
    def draw(self, canvas_obj, fill_color):
        canvas_obj.create_line(
             self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, 
             fill=fill_color, 
             width=2
        )
        
class Cell:
    def __init__(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = True
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        