from cls import Vectorcls
import pygame

pygame.init()

width, height = 1080, 720

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("The Tree fractal")

clock = pygame.time.Clock()
FPS = 60
running = True
segments = []



    
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            segments = koch.generate(segments)
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Black")
    



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()