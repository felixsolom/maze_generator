from cell import Cell
import time 
import random

class Maze:
    def __init__(
        self, 
        x1, 
        y1, 
        num_rows,  
        num_cols, 
        cell_size_x, 
        cell_size_y,
        win=None,
        seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None: 
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._win)
                row.append(cell)                
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j) 
                
                
    def _draw_cell(self, i, j):
        x1 =  self._x1 + (j * self._cell_size_x)
        y1 = self._y1 + (i * self._cell_size_y) 
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
         
        
    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
            
    def _break_entrance_and_exit(self): 
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)
      
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            dirs = []
            if i > 0 and not self._cells[i - 1][j].visited:
                dirs.append(('N', i - 1, j))
            if i < self._num_rows - 1 and not self._cells[i + 1][j].visited:
                dirs.append(('S', i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                dirs.append(('W', i, j - 1))
            if j < self._num_cols - 1 and not self._cells[i][j + 1].visited:
                dirs.append(('E', i, j + 1))
                
            if not dirs:
                self._draw_cell(i, j)
                return  
            
            direction, ni, nj = random.choice(dirs)
            dirs.remove((direction, ni, nj))
            
            if direction == 'N':
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
                
            if direction == 'S':
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
                
            if direction == 'W':
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
                
            if direction == 'E':
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False
            
            self._break_walls_r(ni, nj)
            
            
                
                
    
        
        
                
            
        
        
        