from enum import Enum
from math import floor
class State(Enum):
    Dead = 0
    Alive = 1

class Cell():
    def __init__(self):
        self.state = State.Dead

class CellSystem():
    def __init__(self,mem_count:int):
        self.mem_count = mem_count
        self.grid_1d = []
        self.curr_grid_1d = []
        for i in range(mem_count):
            cell = Cell()
            if i == floor(mem_count/2):
                cell.state = State.Alive
            self.grid_1d.append(cell)
        for j in range(mem_count):
            cell = Cell()
            self.curr_grid_1d.append(cell)

    def current_gen_update(self):
        for j in self.curr_grid_1d:
            j.state = State.Dead
        for i in range(self.mem_count):
            if i == 0:
                self.curr_grid_1d[i].state = self.grid_1d[i+1].state
            elif i == self.mem_count-1:
                self.curr_grid_1d[self.mem_count-1].state = self.grid_1d[i-1].state
            if i != 0 and i !=self.mem_count-1:
                if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Alive:
                    self.curr_grid_1d[i].state = State.Dead
                if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Dead:
                    self.curr_grid_1d[i].state = State.Alive
                if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Alive:
                    self.curr_grid_1d[i].state = State.Alive
                if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Dead:
                    self.curr_grid_1d[i].state = State.Dead
                if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Alive:
                    self.curr_grid_1d[i].state = State.Dead
                if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Dead:
                    self.curr_grid_1d[i].state = State.Alive   
                if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Alive:
                    self.curr_grid_1d[i].state = State.Alive  
                if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Dead:
                    self.curr_grid_1d[i].state = State.Dead 
            
        self.curr_grid_1d, self.grid_1d = self.grid_1d, self.curr_grid_1d  

    def current_gen_print(self):

        self.current_gen_update()
        for i in range(self.mem_count):
            print(self.curr_grid_1d[i].state.value,end=" ")   
     
    def gen_print(self,gen_count):
        for j in range(gen_count):
            self.current_gen_print()
            print()