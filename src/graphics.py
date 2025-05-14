from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze Solver")
        
        self.__canvas = Canvas(self.__root, bg="White", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False 
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Window closed...")
            
    def close(self):
        self.__running = False
                
    def draw_line(self, line_inst, fill_color="Black"):
        line_inst.draw(self.__canvas, fill_color)
        
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2) 
        
    def draw(self, canvas_obj, fill_color="Black"):
        canvas_obj.create_line(
             self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, 
             fill=fill_color, 
             width=2
        )
        
        
            
                
                
                
        
    
    
    