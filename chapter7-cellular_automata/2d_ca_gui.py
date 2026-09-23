import pygame
import random
import math
from enum import Enum
from math import floor

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("2D automata - Game of life - Blinker")

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
    left_x = 0
    left_y = 0
    width = 0
    height = 0
    def __init__(self,screen,canvas_width,canvas_height,cell_count):
        super().__init__()
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        CellBody.width = canvas_width / cell_count
        CellBody.height = canvas_height / cell_count
        self.screen = screen
        self.color = (255,255,255)
        self.left_x = CellBody.left_x
        self.left_y = CellBody.left_y

        CellBody.posshift()
        

    def draw(self,state):
        self.rect = pygame.Rect(self.left_x,self.left_y,CellBody.width,CellBody.height)
        if state == State.Alive:
            self.color = (0,0,0)
        else:
            self.color = (255,255,255)
        pygame.draw.rect(self.screen,self.color,self.rect)

        print(CellBody.left_x,CellBody.left_y,CellBody.width,CellBody.height)
        

    def posshift():
        CellBody.left_x += CellBody.width
        if CellBody.left_x >= width:
            CellBody.left_y += CellBody.height
            CellBody.left_x = 0
        if CellBody.left_y >= height:
            CellBody.left_y = 0



class CellSystem2d():
    def __init__(self,mem_count:int):
        self.mem_count = mem_count
        self.grid_2d = [] # grid_2d[y][x]
        self.curr_grid_2d = []
        #filling up the initial grid
        for i in range(mem_count):
            row = []
            for j in range(mem_count):
                cell = CellBody(screen,width,height,self.mem_count)


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
                cell = CellBody(screen,width,height,self.mem_count)
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
                        if self.grid_2d[j][i].state == State.Dead and (self.count_alivecell(self.grid_2d,j,i) != 3):
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



ca2d = CellSystem2d(72)
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