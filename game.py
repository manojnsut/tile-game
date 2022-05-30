import pygame,os

pygame.init()

display_width =  610
display_height = 650

black = (0,0,0)
green = (200,255,0)

# setting up of game screen
game_screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tile Game")
icon = pygame.image.load('icon2.png')
pygame.display.set_icon(icon)
game_screen.fill(green)
pygame.display.flip()

n=3  # no or rows and column in grid
grid = [
        [1,2,5],
        [4,6,3],
        [7,0,9]
    ]

final = [
         [0,1,2],
         [3,4,5],
         [6,7,9]
    ]

#position of empty tile
empty_X,empty_Y= 2,2

#loading game
game_path = os.path.dirname(__file__)
game_path= game_path.replace('\\','/')

#loading images
tile = pygame.image.load(game_path+"/WHITEBOX.png")
empty_tile = pygame.image.load(game_path+"/BLACKBOX.png")

#check final is reached or not
def isReached(grid,final):
    for i in range(n):
        for j in range(n):
            if(grid[i][j]!=final[i][j]):
                return 0
    return 1

#number generate function
def get_num(grid, y, x, font):
    number = font.render(str(grid[y][x]+1), True, (0,228,0)).convert_alpha()
    return number

# game message
def message(txt,color,x,y):
    screen_message = font.render(txt,True,color)
    game_screen.blit(screen_message,[x,y])

#movement of tiles
def navigate(move,empty_X,empty_Y):
  if(move == "left"):
    if(empty_X-1>=0):
        (grid[empty_Y][empty_X-1], grid[empty_Y][empty_X]) = (grid[empty_Y][empty_X], grid[empty_Y][empty_X-1]) 
        empty_X= empty_X - 1
    else :
         message("Wrong Move ", black, 35, 600)

  elif (move =="right"):
    if(empty_X+1<n):
        (grid[empty_Y][empty_X+1], grid[empty_Y][empty_X]) = (grid[empty_Y][empty_X], grid[empty_Y][empty_X+1])
        empty_X = empty_X + 1
    else :
        message("Wrong Move ", black, 35, 600)

  elif(move=="up"):
    if(empty_Y-1>=0):
        (grid[empty_Y-1][empty_X], grid[empty_Y][empty_X]) = (grid[empty_Y][empty_X], grid[empty_Y-1][empty_X])
        empty_Y = empty_Y - 1
    else :
         message(" Wrong Move ", black, 35, 600)

  elif(move == "down"):
    if(empty_Y+1<n):
        (grid[empty_Y+1][empty_X], grid[empty_Y][empty_X]) = (grid[empty_Y][empty_X], grid[empty_Y+1][empty_X])
        empty_Y = empty_Y + 1 
    else :
        message(" Wrong Move ", black, 35, 600) 
  return empty_X,empty_Y

  

# game loop
run = True

while run == True:
    game_screen.fill(green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if any key is pressed, then run
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    empty_X,empty_Y= navigate("left",empty_X,empty_Y)

                if event.key == pygame.K_RIGHT:
                    empty_X,empty_Y= navigate("right",empty_X,empty_Y)

                if event.key == pygame.K_UP:
                   empty_X,empty_Y=navigate("up",empty_X,empty_Y)

                if event.key == pygame.K_DOWN:
                    empty_X,empty_Y=navigate("down",empty_X,empty_Y)

    # putting numbers in on tiles
    for y in range(0,n):
        for x in range(0,n):
            font = pygame.font.Font(None, 60)
            number = get_num(grid, y, x, font)
            if grid[y][x]==9:
                game_screen.blit(empty_tile, (x*200 +10,y*200+10))
                continue
            else:
                game_screen.blit(tile, (x*200+10,y*200+10))
            game_screen.blit(number,(x*200+80,y*200+80) )
        k = isReached(grid,final)
        if k == 1:
            message("WIN",black,35,600)

    pygame.display.update()