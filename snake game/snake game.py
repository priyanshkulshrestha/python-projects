import pygame
import random
import os
pygame.mixer.init()

x = pygame.init()
# print(x)
# creating game window 
game_window = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("first_python_game")

# background image
bgimg = pygame.image.load("5.jpg")
bgimg = pygame.transform.scale(bgimg, (1000,500)).convert_alpha()

# color defining
white = (255, 255, 255)
red = (255, 0, 0)
green = (10, 255, 0)
blue = (0, 10, 255)
purple = (121, 75, 255)
black = (0, 0, 0)
maroon = (165, 10 ,20)

# plot snake func 
def plot_snake(game_window, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window, red,  (x, y,snake_size ,snake_size))

# clock
clock = pygame.time.Clock()

# defining a function to print score
font = pygame.font.SysFont('Comic Sans MS',50)

def text_screen(text,color,x,y):
    screen_score = font.render(text,True,color)
    game_window.blit(screen_score,(x,y))

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(black)
        game_window.blit(bgimg,(1,1))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # pygame.mixer.music.load('back.mp3')
                    # pygame.mixer.music.play()
                    game_loop()

        pygame.display.update()
        clock.tick(30)


def game_loop():
    # game defining variable
    exit_game = False
    game_over = False
    snake_x = 500
    snake_y = 250
    snake_size = 10
    score = 0
    # making highscore
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore = f.read()
    # velocity variable
    velocity_x = 10
    velocity_y = 10
    # food variable
    food_x = random.randint(20,990)
    food_y = random.randint(55,490)
    # fps
    fps = 30
    snake_list = []
    snake_len = 2
    # creating a game loop
    while not exit_game:
        if game_over:
            # making highscore
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            game_window.fill(maroon)
            text_screen("Do you want to play again?",(240,128,128),200,100)
            text_screen("1. Yes",(240,128,128),400,170)
            text_screen("2. No",(240,128,128),400,240)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1: 
                        welcome()
                    if event.key == pygame.K_2:
                        exit_game = True
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =+ 2
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x =- 2
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y =- 2
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y =+ 2
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<5 and abs(snake_y - food_y)<5:
                score += 10
                pygame.mixer.music.load('beep.wav')
                pygame.mixer.music.play()
                # pygame.mixer.music.load('back.mp3')
                # pygame.mixer.music.play()
                food_x = random.randint(20,990)
                food_y = random.randint(20,490)
                snake_len += 10
                if score> int(highscore):
                    highscore = score
            game_window.fill(black)
            text_screen("score :-  " + str(score) +"    Highscore :- "+ str(highscore),purple,5,5)
            pygame.draw.rect(game_window, blue,  (food_x,food_y ,10,10))
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_len:
                del snake_list[0]
            if snake_x<0 or snake_x>1000 or snake_y<0 or snake_y>500:
                game_over =True
                pygame.mixer.music.load('bomb.mp3')
                pygame.mixer.music.play()
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('bomb.mp3')
                pygame.mixer.music.play()
            # pygame.draw.rect(game_window, red,  (snake_x,snake_y ,snake_size ,snake_size))
            plot_snake(game_window, red,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
