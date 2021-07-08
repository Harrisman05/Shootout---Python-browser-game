import pygame, sys
import moviepy
from pygame import display
from pygame_functions import *
from pygame.locals import *
from moviepy.editor import VideoFileClip

mouse = pygame.mouse.get_pos()

####################################
pygame.init()

clip = VideoFileClip('Pirlo penalty.mp4')
clip = clip.resize((500, 500))
clip.preview()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # this allow the user to quit, pygame.QUIT is a pygame function (hitting the x in the top left)
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:  # This gets any event that is happening on the screen, where is the mouse clicking, keys presses EVERYTHING
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()





