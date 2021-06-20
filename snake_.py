import pygame
import random
import os
# Note: You can learn about all these functions from the pygame documentation

# Initialize the sound library
pygame.mixer.init()

# initialize all modules of pygame into variable x
pygame.init()

# Colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

# Decide the width and height of game window
screen_width=1200
screen_height=600

# Make game window of width 1200 and height 500
game_window=pygame.display.set_mode((screen_width,screen_height))

# For background image
bgimg=pygame.image.load("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\snake.png")
game_bg=pygame.image.load("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\game_bg.jpg")
# You can use convert_alpha() and they will improve game performance, as they convert the image to draw it faster.
bgimg=pygame.transform.scale(bgimg,(500,500)).convert_alpha()

# One of the things you can use convert_alpha() for is pixel perfect collision
game_bg=pygame.transform.scale(game_bg,(screen_width,screen_height)).convert_alpha()



# Now we give title to the game window
pygame.display.set_caption("The Serpent King")
pygame.display.update()
clock=pygame.time.Clock()
# font is used to display on game window
font=pygame.font.SysFont(None,55)


# Text_screen func prints on game window
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])


# Plotting the snake
def plot_snake(game_window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])


# Welcome Screen
def welcome():
    pygame.mixer.music.load("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\welcome_screen.mp3")
    pygame.mixer.music.play()
    exit_game=False
    while not exit_game:
        game_window.fill((203,233,229))
        game_window.blit(bgimg,(360,50))
        # bgimg is background image
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    # Now we load background music
                    pygame.mixer.music.load("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\music.mp3")
                    # Now we play the music using play function
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(20)


# Game Loop
def game_loop():
    # Game specific variables
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=10
    fps=20
    velocity_x=0
    velocity_y=0
    score=0
    # food is the location of apple
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_height/2)
    # We define snake list and snake length
    snake_list=[]
    snake_length=1


    # The highscore 
    with open("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\highscore.txt","r") as f:
        hs=f.read()


    while exit_game is not True:
        # Game-Over Functionality
        if game_over is True:
            # The highscore 
            with open("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\highscore.txt","w") as f:
                f.write(str(hs))
            game_window.fill((203,233,229))
            text_screen("Game Over!!!! Press ENTER To Try Again",red,250,250)
            for event in pygame.event.get():
                # event.type checks if the type of event is quit.....This line will hrlp exit the game window by clicking on X(Cross symbol in red)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        # Now we load game over music
                        pygame.mixer.music.load("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\music.mp3")
                        # Now we play the music using play function
                        pygame.mixer.music.play()
                        game_loop()

        else:

            # The following for loop gets all events during game for example our mouse movements and button clicks and whereever we click
            for event in pygame.event.get():
                # event.type checks if the type of event is quit.....This line will hrlp exit the game window by clicking on X(Cross symbol in red)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    # Whenever we give right or left value then we give velocity of y to 0
                    # Whenever we give up or down value then we give velocity of x to 0
                    if event.key==pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=10
                        velocity_x=0
            snake_y=snake_y+velocity_y
            snake_x=snake_x+velocity_x
            if abs(snake_x-food_x)<12 and abs(snake_y - food_y)<12:
                score=score+10
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)    
                snake_length=snake_length+5 
                if score>int(hs):
                    hs=score
                    
            game_window.fill((203,233,229))
            game_window.blit(game_bg,(0,0))


            # We call the function to display score
            text_screen("Score : "+str(score)+"  Highscore: "+str(hs),red,5,5)
            # Now we make the snake head using rectangle
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            # Now we delete the head of snake so that it does not grow indefinitely
            if len(snake_list)>snake_length:
                del snake_list[0]
            
            # Now we do game over for snake colliding with itself
            if head in snake_list[:-1]:
                game_over=True
                # Now we load game over music
                pygame.mixer.music.load("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\boom.mp3")
                # Now we play the music using play function
                pygame.mixer.music.play()
            # Now we create the game over handling code and collisions with wall 
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                # Now we load game over music
                pygame.mixer.music.load("C:\\Users\\sauny\\Desktop\\sad\\Python Game Dev\\Snake Game\\boom.mp3")
                # Now we play the music using play function
                pygame.mixer.music.play()
            # Now we make the food apple here 
            plot_snake(game_window,black,snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()
    # pygame quit function is used to quit the game

welcome()
