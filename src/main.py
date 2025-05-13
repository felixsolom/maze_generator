from graphics import Window, Line, Cell


def main(): 
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_bottom_wall = False
    c1.draw(50, 50, 100, 100)
    
    c2 = Cell(win)
    c2.has_top_wall = False
    c2.draw(125, 125, 200, 200)
    
    c1.draw_move(c2)
    
    c3 = Cell(win)
    c3.has_left_wall = False
    c3.draw(225, 225, 250, 250)
    
    c2.draw_move(c3)
    
    c4 = Cell(win)
    c4.has_right_wall = False
    c4.draw(300, 300, 500, 500)
    
    c3.draw_move(c4)
    
    win.wait_for_close()
    
main() 