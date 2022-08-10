import pygame
import time
import random
import pyaudio
import struct
import pyautogui  # to press a button to play the game
import pvporcupine

# below are the four wake word's path that you have generated earlier
key1 = 'go_down_windows.ppn'
key2 = 'snake_up_windows.ppn'
key3 = 'go_right_windows.ppn'
key4 = 'go_left_windows.ppn'

# this is the library path that you can fnd inside Porcupine -> lib -> system(windows or linux or mac) -> os type( 64 or 32 bit)
library_path = r'C:/Users/anany/porcupine/lib/windows/amd64/libpv_porcupine.dll'

# this is model file path can be find inside Porcupine -> lib -> common
model_file_path = r'C:/Users/anany/porcupine/lib/common/porcupine_params.pv'
keyword_file_paths = [key1, key2, key3, key4]
sensitivities = [0.5,0.5,0.5,0.5]
handle =Porcupine(library_path, model_file_path, keyword_file_paths=keyword_file_paths, sensitivities=sensitivities)

def get_next_audio_frame():
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(rate=handle.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=handle.frame_length,input_device_index=None)
    pcm = audio_stream.read(handle.frame_length)
    pcm = struct.unpack_from("h" * handle.frame_length, pcm)
    return pcm

while True:
    pcm = get_next_audio_frame()
    keyword_index = handle.process(pcm)
    if keyword_index==1:
        print(keyword_index)
        pyautogui.press('up')
    if keyword_index==3:
        print(keyword_index)
        pyautogui.press('left')
    if keyword_index==2:
        print(keyword_index)
        pyautogui.press('right')
    if keyword_index==0:
        print(keyword_index)
        pyautogui.press('down')

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game using Audio')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 5

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)


        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
