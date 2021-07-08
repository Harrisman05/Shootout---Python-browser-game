import pygame
import time

#Setting up the window

pygame.init() # intialise pygame

display_width = 800
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Shootout')
clock = pygame.time.Clock()
background = pygame.image.load('background.jpeg') #loading of the background image

# Font and Colours

font = pygame.font.SysFont(None, 20)
background = pygame.image.load('background.jpeg') #loading of the background image

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
blue = (0, 0, 255)

# Functions

def text_objects(text, font):  #definint text and font
    TextSurface = font.render(text, True, red) #True refers to anti-aliasing
    return textSurface, textSurface.get_rect() #return the rectangle around our text so that I can position my text
#Text display
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115) # this is defining the font type and size for largeText variables
    TextSurface, TextRect = text_objects(text, largeText) #text surface puts the text on the game window. Text Rect draws a rectangle on the screen of where the text will pop up similar to Word using a text box. text objects not yet defined
    TextRect.center = ((display_width/2), (display_height/2)) # this will centre the text, relative to the display length and width
    gameDisplay.blit(TextSurface, TextRect) #this brings the message to the foreground so the user can see it. The display still needs updating so it to become visible

    pygame.display.update() #this updates the game and brings the message to the screen
    time.sleep(2) # how long the message is displayed

# Game loop
def game_loop():
    game_over = False #setting game_over to False keeps my game running

    while not game_over: #whilst the game is running
        gameDisplay.blit(background, (0, 0)) #adding the background image. blit method presents images to the screen (they can be loaded in the background, blit brings them to the foreground
        for event in pygame.event.get(): # This gets any event that is happening on the screen, where is the mouse clicking, keys presses EVERYTHING
            if event.type == pygame.QUIT: # this allow the user to quit, pygame.QUIT is a pygame function (hitting the x in the top left)
                game_over = True # Sets the game_over variable to True, so it gets us out of the while loop and ends the game.

        pygame.display.update() # this updates the entire 'surface' as there is nothing specified in the parameter (the game screen window updates)
        clock.tick(60) #frames per second start

game_loop()
