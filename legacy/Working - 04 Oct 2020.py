import pygame, sys
import random
from pygame_functions import *
from pygame.locals import *
import pyinputplus as pyip

pygame.init() # intialise pygame


mouse = pygame.mouse.get_pos()
click = False
screenSize(800,800)
setBackgroundImage('background.jpeg')
alpha_box = pygame.image.load('alpha box.png')
transparent_background = pygame.image.load('transparent background.png')
background = pygame.image.load('background.jpeg') #loading of the background image
display_width = 800
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.blit(background, (0, 0))
black = (0, 0, 0)
red = (255, 0, 0)
white = (255,255,255)
nextFrame = clock() #time at which next frame will appear`
frame = 0 #current frame of animation, set to zero as that is the index of the first frame
tick(120)
Shot_selection_gif = makeSprite('Shot selector - 6 balls - sprite sheet.png', 28)
running = True
font = pygame.font.Font('freesansbold.ttf', 15) # pygame font, parameter are font type and size

########################################################################################################################

game_count = 0
post_count = 0
crossbar_count = 0
goal_count = 0
save_count = 0
miss_count = 0
player_choice = ''

#             0              1             2                3             4             5         6        7           8
areas = ('bottom left', 'top left', 'bottom middle', 'top middle', 'bottom right', 'top right', 'post', 'crossbar', 'miss')

player_history = []  # GOALIE GUESSING TECHNOLOGY

########################################################################################################################
########################################################################################################################

def score_counters():
    global goal_count
    global save_count
    global miss_count
    global crossbar_count
    global post_count
    global game_count

    game_count_counter = font.render('SHOT NUMBER - ' + str(game_count), True, red) #text object rendering, text, True to to take screen, black font colour
    goal_count_counter = font.render('Goal count - ' + str(goal_count), True, black) #text object rendering, text, True to to take screen, black font colour
    save_count_counter = font.render('Save count - ' + str(save_count), True, black)
    miss_count_counter = font.render('Complete Miss count - ' + str(miss_count), True, black)
    post_count_counter = font.render('Post count - ' + str(post_count), True, black)
    crossbar_count_counter = font.render('Crossbar count - ' + str(crossbar_count), True, black)
    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(game_count_counter, (600, 50))
    gameDisplay.blit(goal_count_counter, (600, 200))
    gameDisplay.blit(save_count_counter, (600, 240))
    gameDisplay.blit(miss_count_counter, (600, 280))
    gameDisplay.blit(post_count_counter, (600, 320))
    gameDisplay.blit(crossbar_count_counter, (600, 360))
########################################################################################################################
########################################################################################################################
def game_logic(player_choice):
    global save_count
    global goal_count
    goalie_choice = random.choices(areas, weights=[0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.11, 0.11, 0.06], k=1)
    goalie_choice = goalie_choice[0]

    if goalie_choice == areas[8]: #complete miss
        complete_miss(player_choice)

    elif goalie_choice == areas[7]: #crossbar
        crossbar_hit(player_choice)

    elif goalie_choice == areas[6]: #post
        post_hit(player_choice)

    elif player_choice == areas[0]:  # Goalie diving bottom left
        if goalie_choice == areas[0]:
            print('SAVE! The keeper dives low to the left and saves!')
            save_count += 1
        else:
            print('GOAL! You rifle the ball in the left corner and it nestles in the net. Goal!')
            goal_count += 1
    elif player_choice == areas[1]:  # Goalie diving top left
        if goalie_choice == areas[1]:
            print('SAVE! The keeper leaps to the left corner and punches the ball clear!')
            save_count += 1
        else:
            print('GOAL! You smash the ball into the top left corner!')
            goal_count += 1
    elif player_choice == areas[2]:  # Goalie staying bottom middle
        if goalie_choice == areas[2]:
            print('SAVE! The keeper reads you and blocks the shot coming directly at him!')
            save_count += 1
        else:
            print('GOAL! You double bluff the keeper and dink the ball down the middle!')
            goal_count += 1
    elif player_choice == areas[3]:  # Goalie staying top middle
        if goalie_choice == areas[3]:
            print('SAVE! The keeper reads you palms the ball over the top of the crossbar!')
            save_count += 1
        else:
            print('GOAL! You let fly and rocket the ball into the roof of the net!')
            goal_count += 1
    elif player_choice == areas[4]:  # Goalie diving bottom right
        if goalie_choice == areas[4]:
            print('SAVE! The keeper pounces to the right and deflects the ball away!')
            save_count += 1
        else:
            print('GOAL! You arrow the ball into the bottom right corner, keeper stood no chance!')
            goal_count += 1
    elif player_choice == areas[5]:  # Goalie diving top right
        if goalie_choice == areas[5]:
            print('SAVE! The keeper reaches high and manages to redirect the ball over the crossbar!')
            save_count += 1
        else:
            print('GOAL! You crack the ball into the top right corner of the goal!')
            goal_count += 1


########################################################################################################################
########################################################################################################################

def complete_miss(player_choice):
    global miss_count
    global save_count
    if player_choice == areas[0]:  # complete miss
        print('MISS! You drag your shot wide of the post!')  # missing the left post low - bottom low
        miss_count += 1
    elif player_choice == areas[1]:
        print('MISS! You sky your shot wayward of the post!')  # missing the left post high - top left
        miss_count += 1
    elif player_choice == areas[2]:
        print('SAVE! Your shot is easily gathered by the goalie!')  # 'missing' bottom low paradox - keeper gathers the shot - bottom low
        save_count += 1
    elif player_choice == areas[3]:
        print('MISS! Your shot is blazed over the crossbar!')  # missing over the crossbar - top middle
        miss_count += 1
    elif player_choice == areas[4]:
        print('MISS! Your shot trickles passed the post!')  # missing the right post low - bottom right
        miss_count += 1
    elif player_choice == areas[5]:
        print('MISS! Your shot flys high passed the post!')  # missing the right post high - top right
        miss_count += 1

########################################################################################################################

def crossbar_hit(player_choice):
    global crossbar_count
    global save_count
    if player_choice == areas[0]:
        print('SAVE! The keeper manages to drop low and tip the ball around the left post!')  # bottom left and post paradox
        save_count += 1
    elif player_choice == areas[2]:  # bottom middle and crossbar paradox
        print('SAVE! The keeper stays rooted to the spot and denys the ball an introduction to the net!')
        save_count += 1
    elif player_choice == areas[4]:  # bottom right and crossbar paradox
        print('SAVE! The keeper gets a fingertip on the ball and nudges it around the post!')
        save_count += 1
    elif player_choice == areas[1]:  # hitting the left part of the crossbar
        print('CROSSBAR! The ball flys high and to the left but clips the crossbar and soars into the fans!')
        crossbar_count = + 1
    elif player_choice == areas[2]:  # hitting the middle of the crossbar
        print('CROSSBAR! The ball is smashed down the middle and canons off the crossbar!')
        crossbar_count = + 1
    elif player_choice == areas[5]:  # hitting the right part of the crossbar
        print('CROSSBAR! The ball flys high to the right and rattles the top of the crossbar!')
        crossbar_count = + 1

########################################################################################################################

def post_hit(player_choice):
    global post_count
    global save_count
    if player_choice == areas[2]:  # bottom middle and post paradox
        print('SAVE! The keeper began to dive but managed a save with his trailing leg!')
        save_count += 1
    elif player_choice == areas[3]:  # top middle and post paradox
        print('SAVE! The keeper managed to claw the ball away with a finger-tip save!')
        save_count += 1
    elif player_choice == areas[0]:  # hitting the bottom left post
        print('POST! The shot rifles towards the left but thunders off the post!')
        post_count += 1
    elif player_choice == areas[1]:  # hitting the top left post
        print('POST! The shot looks destined for the top left corner but canons off the post!')
        post_count += 1
    elif player_choice == areas[4]:  # hitting the bottom right post
        print('POST! The daisy cutter of a shot looks promising but rockets off the bottom of the post!')
        post_count += 1
    elif player_choice == areas[5]:  # hitting the top right post
        print('POST! The keeper is motionless as he watches the ball ricochet off the post!')
        post_count += 1

########################################################################################################################

########################################################################################################################
########################################################################################################################

def gif_generation(gif, speed):
    moveSprite(gif, 200, 260, True)  # pass Shot_selection_gif thru the function
    showSprite(gif)
    nextFrame = clock()
    frame = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # this allow the user to quit, pygame.QUIT is a pygame function (hitting the x in the top left)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # This gets any event that is happening on the screen, where is the mouse clicking, keys presses EVERYTHING
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True  # click will be true for one frame whenever the mouse button is hit
        if clock() > nextFrame:
            frame = (frame + 1)  # keep increasing the frame by one
            nextFrame += speed  # this controls the speed of the gif
            if frame == 28:
                main_screen()  # ending the gif and calling main_screen to go back to the selection screen
        changeSpriteImage(gif, frame)
########################################################################################################################
########################################################################################################################


def main_screen():

    global save_count
    global goal_count
    global miss_count
    global crossbar_count
    global post_count
    global game_count
    global running
    click = False

    while game_count < 60:
        game_count += 1

        moveSprite(Shot_selection_gif, 400, 360, True)
        showSprite(Shot_selection_gif)
        nextFrame = clock()
        frame = 0
        mouse = pygame.mouse.get_pos()
        if clock() > nextFrame:
            frame = (frame + 1)  # keep increasing the frame by one
            nextFrame += 30  # this controls the speed of the gif
            if frame == 28:
                frame = 0  # resetting the gif once it reaches the end
        changeSpriteImage(Shot_selection_gif, frame)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:  # this allow the user to quit, pygame.QUIT is a pygame function (hitting the x in the top left)
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:  # This gets any event that is happening on the screen, where is the mouse clicking, keys presses EVERYTHING
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True  # click will be true for one frame whenever the mouse button is hit
                mouse = pygame.mouse.get_pos()  # mouse needs to be in the for event, otherwise it doesn't live update
                print(mouse)

                if 355 + 10 > mouse[0] > 355 and 301 + 10 > mouse[1] > 301:  # bottom left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            player_choice = areas[0]
                            game_logic(player_choice)
                            gif_generation(Shot_selection_gif, 100)

                elif 349 + 10 > mouse[0] > 349 and 275 + 10 > mouse[1] > 275:  # top left setting up code to determine whether the mouse position is within the shooting box, #top left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            player_choice = areas[1]
                            game_logic(player_choice)
                            gif_generation(Shot_selection_gif, 100)

                elif 395 + 10 > mouse[0] > 395 and 300 + 10 > mouse[1] > 300:  # bottom middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            player_choice = areas[2]
                            game_logic(player_choice)
                            gif_generation(Shot_selection_gif, 100)

                elif 396 + 10 > mouse[0] > 396 and 279 + 10 > mouse[1] > 279:  # top middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            player_choice = areas[3]
                            game_logic(player_choice)
                            gif_generation(Shot_selection_gif, 100)

                elif 442 + 10 > mouse[0] > 442 and 302 + 10 > mouse[1] > 302:  # bottom right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            player_choice = areas[4]
                            game_logic(player_choice)
                            gif_generation(Shot_selection_gif, 100)

                elif 442 + 10 > mouse[0] > 442 and 282 + 10 > mouse[1] > 282:  # top right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            player_choice = areas[5]
                            game_logic(player_choice)
                            gif_generation(Shot_selection_gif, 100)

            if 355 + 10 > mouse[0] > 355 and 301 + 10 > mouse[1] > 301:  # bottom left
                drawRect(355, 301, 10, 10, red, 0)

            elif 349 + 10 > mouse[0] > 349 and 275 + 10 > mouse[1] > 275:  # top left
                drawRect(349, 275, 10, 10, red, 0)

            elif 395 + 10 > mouse[0] > 395 and 300 + 10 > mouse[1] > 300:  # bottom middle
                drawRect(395, 300, 10, 10, red, 0)

            elif 396 + 10 > mouse[0] > 396 and 279 + 10 > mouse[1] > 279:  # top middle
                drawRect(396, 279, 10, 10, red, 0)

            elif 442 + 10 > mouse[0] > 442 and 302 + 10 > mouse[1] > 302:  # bottom right
                drawRect(442, 302, 10, 10, red, 0)

            elif 442 + 10 > mouse[0] > 442 and 282 + 10 > mouse[1] > 282:  # top right
                drawRect(442, 282, 10, 10, red, 0)

            if clock() > nextFrame:  #this is constantly looking at the clock and is seeing if enough time has passed to play the next frame
                frame = (frame + 1) #keep increasing the frame by one
                nextFrame += 30 #this controls the speed of the gif
                if frame == 28:
                    frame = 0 #resetting the gif once it reaches the end
            changeSpriteImage(Shot_selection_gif, frame)

            score_counters()

            print(mouse)
            print('Save count =' + str(save_count))
            print('Goal count =' + str(goal_count))
            print('Miss count =' + str(miss_count))
            print('Crossbar count =' + str(crossbar_count))
            print('Post count =' + str(post_count))

########################################################################################################################

main_screen()
