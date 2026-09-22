from enum import Enum
from math import floor
class State(Enum):
    Dead = 0
    Alive = 1

class Cell():
    def __init__(self):
        self.state = State.Dead
    # def stateChange(self):
    #     if self.state == State.Dead:
    #         self.state = State.Alive
    #     else:
    #         self.state = State.Dead

class CellSystem():
    def __init__(self,mem_count:int):
        self.mem_count = mem_count
        self.grid_1d = []
        self.curr_grid_1d = []
        for i in range(mem_count):
            cell = Cell()
            if i == floor(mem_count/2):
                #print(i)
                cell.state = State.Alive
            #print(cell.state.name,end=" ")
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
                # if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Alive:
                #     self.curr_grid_1d[i].state = State.Dead
                # if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Dead:
                #     self.curr_grid_1d[i].state = State.Alive
                # if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Alive:
                #     self.curr_grid_1d[i].state = State.Alive
                # if self.grid_1d[i].state == State.Alive and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Dead:
                #     self.curr_grid_1d[i].state = State.Dead
                # if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Alive:
                #     self.curr_grid_1d[i].state = State.Dead
                # if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Alive and self.grid_1d[i+1].state == State.Dead:
                #     self.curr_grid_1d[i].state = State.Alive   
                # if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Alive:
                #     self.curr_grid_1d[i].state = State.Alive  
                # if self.grid_1d[i].state == State.Dead and self.grid_1d[i-1].state == State.Dead and self.grid_1d[i+1].state == State.Dead:
                #     self.curr_grid_1d[i].state = State.Dead 

                ruleset = [State.Dead,State.Alive,State.Dead,State.Alive,State.Alive,State.Dead,State.Alive,State.Dead]
                def binary_to_decimal(cellgrid,cellIndex):
                    return cellgrid[cellIndex-1].state.value*(2**2)+ cellgrid[cellIndex].state.value*(2**1)+ cellgrid[cellIndex+1].state.value*(2**0)
                index = binary_to_decimal(self.grid_1d,i)
                self.curr_grid_1d[i].state = ruleset[index]
            
        self.curr_grid_1d, self.grid_1d = self.grid_1d, self.curr_grid_1d  

    def current_gen_print(self):
        self.current_gen_update()
        for i in range(self.mem_count):
            print(self.grid_1d[i].state.value,end=" ")   
     
    def gen_print(self,gen_count):
        for i in self.grid_1d: # for gen 0 print
            print(i.state.value,end=" ")
        print()
        # for k in self.curr_grid_1d:
        #     print(k.state.value, end=" ")
        # print()
        for j in range(gen_count-1):
            self.current_gen_print()
            print()


ca = CellSystem(17)
# i = True
# while i:
ca.gen_print(9)
