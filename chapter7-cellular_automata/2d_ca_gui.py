import pygame
import random
import math
from enum import Enum
from math import floor

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("2D automata - Game of life")

clock = pygame.time.Clock()
FPS = 60

#enum for cell state
class State(Enum):
    Dead = 0
    Alive = 1

#cell class
class Cell():
    def __init__(self):
        self.state = State.Dead

class CellBody(Cell):
    def __init__(self, screen, x, y, width, height):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)

    def draw(self, state):
        if state == State.Alive:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)
        pygame.draw.rect(self.screen, self.color, self.rect)


class CellSystem2d():
    def __init__(self,mem_count:int):
        self.mem_count = mem_count
        self.grid_2d = [] # grid_2d[y][x]
        self.curr_grid_2d = []

        # preparing the grid
        # Precompute coordinates for each cell 
        for i in range(mem_count):
            y0 = int(i * height / mem_count)
            y1 = int((i + 1) * height / mem_count)
            h = y1 - y0
            row = []
            curr_row = []
            for j in range(mem_count):
                x0 = int(j * width / mem_count)
                x1 = int((j + 1) * width / mem_count)
                w = x1 - x0

                cell = CellBody(screen, x0, y0, w, h)

                #condition to start the game and get blinker
                # if i == floor(mem_count/2) and j == floor(mem_count/2):
                #     cell.state = State.Alive
                # if i == floor(mem_count/2)+1 and j == floor(mem_count/2):
                #     cell.state = State.Alive
                # if i == floor(mem_count/2)-1 and j == floor(mem_count/2):
                #     cell.state = State.Alive
                
                # random noise alive (30% - 50% probability)
                if random.random() < 0.30:
                    cell.state = State.Alive
                row.append(cell)

                curr_cell = CellBody(screen, x0, y0, w, h)
                curr_row.append(curr_cell)

            self.grid_2d.append(row)
            self.curr_grid_2d.append(curr_row)

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
                        alive_count = self.count_alivecell(self.grid_2d, j, i)
                        # cell dead condition 
                        if self.grid_2d[j][i].state == State.Alive and alive_count != 3:
                            self.curr_grid_2d[j][i].state = State.Dead
                        # cell alive condition
                        if self.grid_2d[j][i].state == State.Dead and alive_count == 3:
                            self.curr_grid_2d[j][i].state = State.Alive
                        # cell staying alive 
                        if self.grid_2d[j][i].state == State.Alive and (alive_count == 3 or alive_count == 2):
                            self.curr_grid_2d[j][i].state = State.Alive
                        # cell staying dead
                        if self.grid_2d[j][i].state == State.Dead and (alive_count != 3):
                            self.curr_grid_2d[j][i].state = State.Dead
                
        self.curr_grid_2d, self.grid_2d = self.grid_2d, self.curr_grid_2d  

    def current_gen_print(self):
        self.current_gen_update()
        for i in range(self.mem_count):
            for j in range(self.mem_count):
                self.grid_2d[i][j].draw(self.grid_2d[i][j].state)   
     
    def gen_0_print(self):
        for i in range(self.mem_count): # for gen 0
            for j in range(self.mem_count):
                self.grid_2d[i][j].draw(self.grid_2d[i][j].state)  



grid_size = 72*2  
ca2d = CellSystem2d(grid_size)
ca2d.gen_0_print()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    ca2d.current_gen_print()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()