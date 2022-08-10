import pygame                   #importing modules
import time
import random
from playsound import playsound

pygame.init()

white = (255, 255, 255)        #RGB codes for colours
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
l = [white,yellow,red,black]   #list of colours
high = [0] #initial score is zero
dis_width = 600 #width of game screen
dis_height = 400#height of game screen

dis = pygame.display.set_mode((dis_width, dis_height))#method of pygame to set screen
pygame.display.set_caption('Snake Game Using Audio')# set game screen title


clock = pygame.time.Clock()

snake_block = 10   #size of snake body initially
snake_speed = 9    #speed of snake

font_style = pygame.font.SysFont("bahnschrift", 25)#font style and size
score_font = pygame.font.SysFont("comicsansms", 35)

#go to line 52
def our_snake(snake_block, snake_list):#Making of Snake #come after line 132
    i = 0
    for x in snake_list:   #different colours of snake blocks added
        if i == len(l):
            i = 0
        pygame.draw.rect(dis, l[i], [x[0], x[1], snake_block, snake_block])
        i = i+1


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 4])
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 3])
def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 2])


def gameLoop():

    game_over = False #when game is going on
    game_close = False #when game is going on

    x1 = dis_width / 2 #position of snake
    y1 = dis_height / 2 #position of snake

    x1_change = 0  #initial change in position is zero
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #position of food
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    j = 0
    #setting sound at starting
    playsound('audio.mp3')
    while not game_over:
        flag = 'y'
        while game_close == True:
            high.append(Length_of_snake) #highest score

            background_image = pygame.image.load("grass.jpg").convert()#adding background image
            dis.blit(background_image, [0, 0])
            m = max(high)#maximum marks till now
            message("You Lost! Your score is : "+str(Length_of_snake), red)#defined in line 41
            message1("Highest Score : "+str(m), yellow)
            message2("Press C-Play Again or Q-Quit", white)
            pygame.display.update()#game screen gets updated
            if flag=='y':#for audio when game ends
                playsound('audio1.wav')
                playsound('audio.mp3')
                flag ='n'#audio ends as we change the value of slag to n instead of y
            flag = 'n'

            for event in pygame.event.get(): #for event when any key is pressed
                if event.type == pygame.KEYDOWN:#if any key is pressed
                    if event.key == pygame.K_q:#if key q is pressed
                        game_over = True #game over is true
                        game_close = False
                    if event.key == pygame.K_c:#if key c is pressed
                        gameLoop() #game restarts

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#if player presses Q and quits
                game_over = True
            if event.type == pygame.KEYDOWN:#if any key is pressed on keyboard
                if event.key == pygame.K_LEFT:#if left key pressed
                    x1_change = -snake_block #change in position of snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # if snake touches boundary it closes game
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change #new position of snake
        y1 += y1_change #new position of snake

        background_image = pygame.image.load("grass.jpg").convert()
        dis.blit(background_image, [0, 0])
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])#making food#color#location#dimensions
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:#moving the snake
            del snake_List[0]

        for x in snake_List[:-1]:# if snake touches itself game is closed
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)#controlling the function our_snake#line 32


        pygame.display.update()
        if x1 == foodx and y1 == foody:  #when snake eats food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0#new position of food
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            if j == len(l)-1:# screen filled with next colour when snake eats food
                dis.fill(l[0])
                j = -1
            else:
                dis.fill(l[j+1])
            j = j+1
            pygame.display.update() #updates the game screen

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
