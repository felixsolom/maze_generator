from graphics import Window, Line

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.visited = False
        
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self._win is not None:
            if self.has_left_wall:
                line = Line(x1, y1, x1, y2)
                self._win.draw_line(line)
            else:
                line = Line(x1, y1, x1, y2)
                self._win.draw_line(line, "white")
            if self.has_top_wall:
                line = Line(x1, y1, x2, y1)
                self._win.draw_line(line)
            else:
                line = Line(x1, y1, x2, y1)
                self._win.draw_line(line, "white")
            if self.has_right_wall:
                line = Line(x2, y1, x2, y2)
                self._win.draw_line(line)
            else:
                line = Line(x2, y1, x2, y2)
                self._win.draw_line(line, "white")
            if self.has_bottom_wall:
                line = Line(x1, y2, x2, y2)
                self._win.draw_line(line)
            else:
                line = Line(x1, y2, x2, y2)
                self._win.draw_line(line, "white")
            
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "grey"
        start_x = (self._x1 + self._x2) // 2
        start_y = (self._y1 + self._y2) // 2
        
        end_x = (to_cell._x1 + to_cell._x2) // 2
        end_y = (to_cell._y1 + to_cell._y2) // 2
        line = Line(start_x, start_y, end_x, end_y)
        self._win.draw_line(line, fill_color)
        return line
    
     