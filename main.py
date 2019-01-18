import pygame
import random

pygame.init()

class Window():
    """
    Window should be a square, so x and y dim are the same
    """
    x = 800

    def __init__(self, x=800):
        self.x = x

    def window_init(self):
        pygame.display.set_caption('Game of life')
        return pygame.display.set_mode((self.x,self.x))

class Cell():
    """
    Single cell definition
    """

    side = 5

    def __init__(self, side = 5, live = False, col_live=(0, 255, 0), col_dead=(128, 128, 128)):
        self.side = side
        self.live = live
        self.col_live = col_live
        self.col_dead = col_dead

def create_cell_table(N):
    """
    Function creates cells table, and randomly create N number of live cells.
    :return:
    """
    cells_num = int(Window.x / (Cell.side + 1))
    cell_table = [[0 for x in range(cells_num)] for y in range(cells_num)]
    for i in range(cells_num):
        for j in range(cells_num):
            cell_table[i][j] = Cell()
    for n in range(N):
        cell_table[random.randint(0, cells_num-1)][random.randint(0, cells_num-1)].live = True

    return cell_table

def draw_cells():
    """
    function draw all the cells on the board
    :return:
    """
    x,y = 0,0
    for i in range(len(cell_table)):
        for j in range(len(cell_table)):
            if cell_table[i][j].live == True:
                color = cell_table[i][j].col_live
            else: color = cell_table[i][j].col_dead
            pygame.draw.rect(win, color, (x, y, Cell.side, Cell.side))
            x += 6
        x = 0
        y += 6

def update_cell_table(cell_table):
    cells_num = int(Window.x / (Cell.side + 1))
    for i in range(cells_num):
        for j in range(cells_num):
            neighbours = 0
            try:
                if cell_table[i-1][j-1].live == True:
                    neighbours += 1
            except: pass
            try:
                if cell_table[i][j-1].live == True:
                    neighbours += 1
            except: pass
            try:
                if cell_table[i+1][j-1].live == True:
                    neighbours += 1
            except: pass
            try:
                if cell_table[i-1][j].live == True:
                    neighbours += 1
            except: pass
            try:
                if cell_table[i+1][j].live == True:
                    neighbours += 1
            except: pass
            try:
                if cell_table[i-1][j+1].live == True:
                    neighbours += 1
            except: pass
            try:
                if cell_table[i][j+1].live == True:
                    neighbours += 1
            except: pass
            try:
                if cell_table[i+1][j+1].live == True:
                    neighbours += 1
            except: pass
            if cell_table[i][j].live == False and neighbours == 3:
                cell_table[i][j].live = True
            elif cell_table[i][j].live == True and (neighbours < 2 or neighbours > 3):
                cell_table[i][j].live = False
            else: pass

    return cell_table


########################################################################################################################
# MAIN LOOP
########################################################################################################################

window = Window(800)
win = window.window_init()

cell_table = create_cell_table(1000)

run = True
while run:

    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    # EXIT CONDITIONS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_ESCAPE]:
        run = False

    draw_cells()
    cell_table = update_cell_table(cell_table)

    pygame.display.update()
