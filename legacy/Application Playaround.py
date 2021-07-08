import pygame, sys
from pygame.locals import *
import time

#Setting up the window

pygame.init() # intialise pygame

display_width = 800
display_height = 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shootout')
clock = pygame.time.Clock()

# Font, Colours and images

title_font = pygame.font.SysFont(None, 50)
menu_font = pygame.font.SysFont(None, 40)
background = pygame.image.load('background.jpeg') #loading of the background image
shot_selector = pygame.image.load('shot selector.jpeg')
save_with_feet = pygame.image.load('save with feet.gif')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
blue = (0, 0, 255)

click = False
# Functions

#Text appearance:

def draw_text(text, font, colour, surface, x, y): #text is set as a parameter so that i can pass my own arguments in text boxes, keeps it flexible
    textobj = font.render(text, 1, colour) # create a text object which belongs to the font object using render method, supplying 3 arguments.
    textrect = textobj.get_rect() # text to be rendered, anti-aliasing (1 yes, 0 no) and colour of the text
    textrect.center = (x,y) # Creating the rectangle for the text on the x and y coordinate of the rectangle box
    surface.blit(textobj, textrect) # We have only created the game objects, now they have to be blitted. Blitting is copying the pixels belonging
    # to said object onto the screen. So we blit the text object onto the screen and then blit the rectangle of that text object

# Main menu:

def main_menu():

    while True:
        click = False
        screen.blit(background, (0, 0))
        draw_text('Shootout', title_font, black, screen, display_width / 2, 40) #draw_text parameter: (text, font, colour, surface, x, y)

        mx, my = pygame.mouse.get_pos() #this tracks the x and y positions of the mouse

        button_1 = pygame.Rect(display_width/2 - 100, 100, 200, 50) #use rect object to store and manipulate retangular objects, in this case used for buttons. Rect(left, top, width, height) -> Rect
        button_2 = pygame.Rect(display_width/2 - 100, 200, 200, 50) # display_width/2 - 100 centres the option, as I have to account for the width of the text box
        if button_1.collidepoint((mx,my)): # as mx and my are tracking mouse position, now I am checking when the mouse collides with the buttons
            if click:
                game() #One these buttons are clicked, I call the game() function and the game loop runs
        if button_2.collidepoint((mx,my)):
            if click:
                options()

        pygame.draw.rect(screen, red, button_1)
        draw_text('Play', menu_font, black, screen, display_width/2, 125)
        pygame.draw.rect(screen, red, button_2)
        draw_text('Options', menu_font, black, screen, display_width / 2, 225)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT: # this allow the user to quit, pygame.QUIT is a pygame function (hitting the x in the top left)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # This gets any event that is happening on the screen, where is the mouse clicking, keys presses EVERYTHING
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True # click will be true for one frame whenever the mouse button is hit

        pygame.display.update()
        clock.tick(60)

# Game
def game():
    running = True
    while running:
        screen.blit(save_with_feet, (0, 0))
        draw_text('Game', title_font, white, screen, display_width/2, 20)  # screen is gamedisplay
        for event in pygame.event.get():
            while True:
                if clock() > nextFrame:
                    frame = (frame + 1)
                    nextFrame += 50
                changeSpriteImage(testSprite, frame)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
        pygame.display.update()
        clock.tick(60)

def options():
    running = True
    while running:
        screen.fill((black))
        draw_text('Options', title_font, white, screen, display_width/2, 20)  # screen is gamedisplay
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        clock.tick(60)

main_menu()