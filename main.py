import pygame
from settings import *
from sprites import *

grid = []

generations = 0

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
ALIVE = False
def create_grid():
    temp = []
    for x in range(0,WIDTH,BOX):
        for y in range(0,HEIGHT,BOX):
            temp.append([pygame.Rect(x, y, BOX, BOX),False,True])
        grid.append(temp)
        temp = []

def draw_grid():
    for x in range(0,WIDTH,BOX):
        pygame.draw.line(WIN, WHITE, (x,0), (x,HEIGHT))
    for y in range(0,HEIGHT,BOX):
        pygame.draw.line(WIN, WHITE, (0,y), (WIDTH,y))
    for i in grid:
        for j in i:
            if j[1] == True:
                pygame.draw.rect(WIN, WHITE, j[0])
            else:
                pygame.draw.rect(WIN, (0,0,0), j[0])
def draw_screen():
    draw_grid()
    pygame.display.update()


def alive_sprite(x,y):
    x = x//BOX
    y = y // BOX
    grid[x][y][1] = not grid[x][y][1]
    grid[x][y][2] = not grid[x][y][2]
    
    
def is_alive(x,y):
    
    return grid[x][y][1]




def in_grid(x,y,realx,realy):
    if x==realx and y == realy:
        return False
    elif 0<=x <=ROWS-1 and 0<= y<= COL -1:
        return True
            

def check_neighbour(x,y):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if  in_grid(x+i,y+j,x,y):
                if not grid[x+i][y+j][2]:
                    count+=1
           
    if  count <2 or count>3:
        grid[x][y][1] = False
    if not is_alive(x, y) and count == 3:
        grid[x][y][1] = True
    


def algorithm():
    global generations
    generations += 1
    print(generations)
    for cells in grid:
        
        
        ind = grid.index(cells)
        for cell in cells:
                neighbours = check_neighbour(ind,cells.index(cell))          

    for row in grid:
        for cell in row:
            if cell[1]:
                cell[2] = False
            else:
                cell[2] = True
                           
                    
                    
def main(): 
    clock = pygame.time.Clock()
    run = True
    create_grid()
    games = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                alive_sprite( x, y)
                print("alive:",grid[x//BOX][y//BOX][1],"dead:",grid[x//BOX][y//BOX][2])
                
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    games = not games
        if games:
            algorithm()
        draw_screen()
    pygame.quit()


if __name__ == "__main__":
    main()