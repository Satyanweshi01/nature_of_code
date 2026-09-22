from enum import Enum
from math import floor
class State(Enum):
    Dead = 0
    Alive = 1

class Cell():
    def __init__(self):
        self.state = State.Dead

class CellSystem2d():
    def __init__(self,mem_count:int):
        self.mem_count = mem_count
        self.grid_2d = [] # grid_2d[y][x]
        self.curr_grid_2d = []
        #filling up the initial grid
        for i in range(mem_count):
            row = []
            for j in range(mem_count):
                cell = Cell()
                #condition to start the game and get blinker
                if i == floor(mem_count/2) and j == floor(mem_count/2):
                    cell.state = State.Alive
                if i == floor(mem_count/2)+1 and j == floor(mem_count/2):
                    cell.state = State.Alive
                if i == floor(mem_count/2)-1 and j == floor(mem_count/2):
                    cell.state = State.Alive
                row.append(cell)
            self.grid_2d.append(row)
        #filling up the initial current grid
        for i in range(mem_count):
            row = []
            for j in range(mem_count):
                cell = Cell()
                row.append(cell)
            self.curr_grid_2d.append(row)
            
    def count_alivecell(self,cellGrid,cell_posy,cell_posx)->int:
        aliveCellcount = 0
        if cellGrid[cell_posy][cell_posx+1].state == State.Alive:
                aliveCellcount += 1
        if cellGrid[cell_posy][cell_posx-1].state == State.Alive:
                aliveCellcount += 1
        if cellGrid[cell_posy+1][cell_posx].state == State.Alive:
                aliveCellcount += 1
        if cellGrid[cell_posy-1][cell_posx].state == State.Alive: 
                aliveCellcount += 1
        if cellGrid[cell_posy+1][cell_posx+1].state == State.Alive:
            aliveCellcount += 1 
        if cellGrid[cell_posy-1][cell_posx-1].state == State.Alive:   
            aliveCellcount += 1
        if cellGrid[cell_posy-1][cell_posx+1].state == State.Alive: 
            aliveCellcount += 1
        if cellGrid[cell_posy+1][cell_posx-1].state == State.Alive:                          
            aliveCellcount += 1
        return aliveCellcount

    def current_gen_update(self):
        for j in self.curr_grid_2d:
            for i in j:
                i.state = State.Dead
        for j in range(self.mem_count):
            for i in range(self.mem_count):
                if j != 0 and j != self.mem_count-1:
                    # if i == 0:
                    #     self.curr_grid_2d[j][i].state = self.grid_2d[j][i+1].state
                    # elif i == self.mem_count-1:
                    #     self.curr_grid_2d[j][self.mem_count-1].state = self.grid_2d[j][i-1].state
                    if i != 0 and i !=self.mem_count-1:
                        # ignoring the edge for now 
                        # cell dead condition 
                        if self.grid_2d[j][i].state == State.Alive and self.count_alivecell(self.grid_2d,j,i) != 3:
                            self.curr_grid_2d[j][i].state = State.Dead
                        # cell alive condition
                        if self.grid_2d[j][i].state == State.Dead and self.count_alivecell(self.grid_2d,j,i) == 3:
                            self.curr_grid_2d[j][i].state = State.Alive
                        # cell staying alife 
                        if self.grid_2d[j][i].state == State.Alive and (self.count_alivecell(self.grid_2d,j,i) ==3 or self.count_alivecell(self.grid_2d,j,i) ==2):
                            self.curr_grid_2d[j][i].state = State.Alive
                        # cell staying dead
                        if self.grid_2d[j][i].state == State.Dead and self.count_alivecell(self.grid_2d,j,i) != 3:
                            self.curr_grid_2d[j][i].state = State.Dead
                
        self.curr_grid_2d, self.grid_2d = self.grid_2d, self.curr_grid_2d  

    def current_gen_print(self):
        self.current_gen_update()
        for i in range(self.mem_count):
            for j in range(self.mem_count):
                print(self.curr_grid_2d[i][j].state.value,end=" ")
            print()   
     
    def gen_print(self,gen_count):
        for i in range(self.mem_count): # for gen 0
            for j in range(self.mem_count):
                print(self.grid_2d[i][j].state.value,end=" ")
            print()   
        print(end="\n\n\n")
        for j in range(gen_count-1):
            self.current_gen_print()
            print(end="\n\n\n")


ca2d = CellSystem2d(10)
ca2d.gen_print(10)

