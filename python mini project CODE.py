import pygame, sys, time, random


difficulty=4


# Window size
X = 1050
Y = 750


a=random.randint(1,100)
b=random.randint(1,100)
k=("+")
num=random.randint(1,100)



# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')
font = pygame.font.Font('freesansbold.ttf', 20)



 
# Initialise game window
pygame.display.set_caption('Snake Eater')
display_surface = pygame.display.set_mode((X, Y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255,0)



# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (X//10)) * 10, random.randrange(1, (Y//10)) * 10]
food_spawn = True

var_pos = [random.randrange(1, (X//10)) * 10, random.randrange(1, (Y//10)) * 10]
var_spawn= True

direction = 'RIGHT'
change_to = direction

dingSound = pygame.mixer.Sound('C:\\Users\\sb\\Desktop\\MINI PROJECT\\ding.wav') 
crashSound = pygame.mixer.Sound('C:\\Users\\sb\\Desktop\\MINI PROJECT\\crash.wav') 
music = pygame.mixer.music.load('C:\\Users\\sb\\Desktop\\MINI PROJECT\\bg.mp3')
pygame.mixer.music.play(-1)
score = 0

grass = pygame.image.load('C:\\Users\\sb\Desktop\\MINI PROJECT\\background.jpeg')

level_surface = font.render('Choose the difficulty level from Easy(press e) Medium(press m ) Hard(press h) Impossible(press i)', True, blue)
level_rect = level_surface.get_rect()
level_rect.midtop = (X/2, 10)
    
   
    

# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (X/2, Y/4)
    display_surface.fill(black)
    display_surface.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (X/10, 50)
    else:
        score_rect.midtop = (X/2, Y/1.25)
    display_surface.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == ord('e'):
                difficulty = 4
            if event.key == ord('m'):
                difficulty = 8
            if event.key == ord('h'):
                difficulty = 10    
            if event.key == ord('i'):
                difficulty = 12    
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        dingSound.play()
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        a=random.randint(1,100)
        b=random.randint(1,100)
        k=("+")
        num=random.randint(1,100)


        food_pos = [random.randrange(1, (X//10)) * 10, random.randrange(1, (Y//10)) * 10]
        var_pos = [random.randrange(1, (X//10)) * 10, random.randrange(1, (Y//10)) * 10]

    food_spawn = True

    # GFX
    
    display_surface.fill(black)
    display_surface.blit(grass, (0,0))
    
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(display_surface,yellow, pygame.Rect(pos[0], pos[1], 15, 15))
        #display_surface.blit(snake, (pos[0],pos[1]))
      
    # Snake food
    


    #Equation
    text = font.render('Equation:' + str(a)+str(k)+str(b), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (80,40)



    #food
    food = font.render(str(a+b),True, green, blue)
    foodRect = food.get_rect()
    foodRect.center = (food_pos)

    #Random variable
    var = font.render(str(num), True, green, blue)
    varRect = var.get_rect()
    varRect.center = (var_pos)

  


    display_surface.blit(text, textRect)
    display_surface.blit(food, foodRect)
    display_surface.blit(var, varRect)
    display_surface.blit(level_surface, level_rect)

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > X-10:
        crashSound.play()
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > Y-10:
        crashSound.play()
        game_over()
    if snake_pos[0] == var_pos[0] and snake_pos[1] == var_pos[1]:
        crashSound.play()
        game_over()    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, red, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)
