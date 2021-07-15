
##################### TESTING BRANCH ####################
import pygame, sys
import random
from pygame_functions import *
from pygame.locals import *
import pyinputplus as pyip
from pygame import mixer
import moviepy
from moviepy.editor import VideoFileClip, AudioFileClip
import time

pygame.init() # intialise pygame

def clip():
    clip = VideoFileClip('Pirlo_penalty.mp4')
    clip = clip.resize((800, 800))
    clip.preview()

#clip() # the intro clip

click = False
screenSize(800,800)
setBackgroundImage('gifs/background.jpeg')
background = pygame.image.load('gifs/background.jpeg') #loading of the background image
display_width = 800
display_height = 800
gif_x_coord_top_left_corner = (display_width/2)-130.5
gif_y_coord_top_left_corner = (display_width/2)-180
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.blit(background, (0, 0))
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
nextFrame = clock() #time at which next frame will appear`
frame = 0 #current frame of animation, set to zero as that is the index of the first frame
tick(60)

red_x = pygame.image.load('images/red_x.png').convert()
green_ball = pygame.image.load('images/green_ball.png').convert()

##############################################################################################################################################################################

# bottom left sprite sheets + end frames

bottom_left_goal_1_gif = makeSprite('gifs/bottom_left_gifs/bottom_left_goal_1_gif.png', 8)
bottom_left_goal_1_end_frame = pygame.image.load('gifs/bottom_left_gifs/bottom_left_goal_1_end_frame.png')

bottom_left_save_1_gif = makeSprite('gifs/bottom_left_gifs/bottom_left_save_1_gif.png', 8)
bottom_left_save_1_end_frame = pygame.image.load('gifs/bottom_left_gifs/bottom_left_save_1_end_frame.png')

bottom_left_post_1_gif = makeSprite('gifs/bottom_left_gifs/bottom_left_post_1_gif.png', 8)
bottom_left_post_1_end_frame = pygame.image.load('gifs/bottom_left_gifs/bottom_left_post_1_end_frame.png')

bottom_left_miss_1_gif = makeSprite('gifs/bottom_left_gifs/bottom_left_miss_1_gif.png', 8)
bottom_left_miss_1_end_frame = pygame.image.load('gifs/bottom_left_gifs/bottom_left_miss_1_end_frame.png')

bottom_left_saveparadox_1_gif = makeSprite('gifs/bottom_left_gifs/bottom_left_saveparadox_1_gif.png', 8)
bottom_left_saveparadox_1_end_frame = pygame.image.load('gifs/bottom_left_gifs/bottom_left_saveparadox_1_end_frame.png')

##############################################################################################################################################################################

# top left sprite sheets + end frames

top_left_goal_1_gif = makeSprite('gifs/top_left_gifs/top_left_goal_1_gif.png', 8)
top_left_goal_1_end_frame = pygame.image.load('gifs/top_left_gifs/top_left_goal_1_end_frame.png')

top_left_save_1_gif = makeSprite('gifs/top_left_gifs/top_left_save_1_gif.png', 8)
top_left_save_1_end_frame = pygame.image.load('gifs/top_left_gifs/top_left_save_1_end_frame.png')

top_left_crossbar_1_gif = makeSprite('gifs/top_left_gifs/top_left_crossbar_1_gif.png', 8)
top_left_crossbar_1_end_frame = pygame.image.load('gifs/top_left_gifs/top_left_crossbar_1_end_frame.png')      

#top_left_miss_1_gif = makeSprite('gifs/top_left_gifs/top_left_miss_1_gif.png', 8)                      # missing gif
#top_left_miss_1_end_frame = pygame.image.load('gifs/top_left_gifs/top_left_miss_1_end_frame.png')      # missing gif

#top_left_saveparadox_1_gif = makeSprite('gifs/top_left_gifs/top_left_saveparadox_1_gif.png', 8)        # missing gif
#top_left_saveparadox_1_end_frame = pygame.image.load('gifs/top_left_gifs/top_left_saveparadox_1_end_frame.png') # missing gif

##############################################################################################################################################################################

# top middle sprite sheets + end frames

top_middle_goal_1_gif = makeSprite('gifs/top_middle_gifs/top_middle_goal_1_gif.png', 8)
top_middle_goal_1_end_frame = pygame.image.load('gifs/top_middle_gifs/top_middle_goal_1_end_frame.png')

# top_middle_save_1_gif = makeSprite('gifs/top_middle_gifs/top_middle_save_1_gif.png', 8)  # missing gif
# top_middle_save_1_end_frame = pygame.image.load('gifs/top_middle_gifs/top_middle_save_1_end_frame.png')  # missing gif

top_middle_crossbar_1_gif = makeSprite('gifs/top_middle_gifs/top_middle_crossbar_1_gif.png', 8)
top_middle_crossbar_1_end_frame = pygame.image.load('gifs/top_middle_gifs/top_middle_crossbar_1_end_frame.png')

top_middle_miss_1_gif = makeSprite('gifs/top_middle_gifs/top_middle_miss_1_gif.jpg', 8)  ### jpg because size conversion can mess up bit depth and then the fade away is not lined up with end frame for some unknown reason
top_middle_miss_1_end_frame = pygame.image.load('gifs/top_middle_gifs/top_middle_miss_1_end_frame.jpg')

#top_middle_saveparadox_1_gif = makeSprite('gifs/top_middle_gifs/top_middle_saveparadox_1_gif.png', 8)        # missing gif
#top_middle_saveparadox_1_end_frame = pygame.image.load('gifs/top_middle_gifs/top_middle_saveparadox_1_end_frame.png') # missing gif

##############################################################################################################################################################################

# bottom middle sprite sheets + end frames

bottom_middle_goal_1_gif = makeSprite('gifs/bottom_middle_gifs/bottom_middle_goal_1_gif.png', 8)
bottom_middle_goal_1_end_frame = pygame.image.load('gifs/bottom_middle_gifs/bottom_middle_goal_1_end_frame.png')

bottom_middle_save_1_gif = makeSprite('gifs/bottom_middle_gifs/bottom_middle_save_1_gif.png', 8)  # missing gif
bottom_middle_save_1_end_frame = pygame.image.load('gifs/bottom_middle_gifs/bottom_middle_save_1_end_frame.png')  # missing gif

bottom_middle_crossbarparadox_2_gif = makeSprite('gifs/bottom_middle_gifs/bottom_middle_crossbarparadox_2_gif.png', 8)
bottom_middle_crossbarparadox_2_end_frame = pygame.image.load('gifs/bottom_middle_gifs/bottom_middle_crossbarparadox_2_end_frame.png')

bottom_middle_miss_3_gif = makeSprite('gifs/bottom_middle_gifs/bottom_middle_miss_3_gif.png', 8)  ### png because size conversion can mess up bit depth and then the fade away is not lined up with end frame for some unknown reason
bottom_middle_miss_3_end_frame = pygame.image.load('gifs/bottom_middle_gifs/bottom_middle_miss_3_end_frame.png')

bottom_middle_postparadox_4_gif = makeSprite('gifs/bottom_middle_gifs/bottom_middle_postparadox_4_gif.png', 8)        # missing gif
bottom_middle_postparadox_4_end_frame = pygame.image.load('gifs/bottom_middle_gifs/bottom_middle_postparadox_4_end_frame.png') # missing gif

##############################################################################################################################################################################

# bottom right sprite sheets + end frames

bottom_right_goal_1_gif = makeSprite('gifs/bottom_right_gifs/bottom_right_goal_1_gif.png', 8)
bottom_right_goal_1_end_frame = pygame.image.load('gifs/bottom_right_gifs/bottom_right_goal_1_end_frame.png')

bottom_right_save_1_gif = makeSprite('gifs/bottom_right_gifs/bottom_right_save_1_gif.png', 8)
bottom_right_save_1_end_frame = pygame.image.load('gifs/bottom_right_gifs/bottom_right_save_1_end_frame.png')

bottom_right_post_1_gif = makeSprite('gifs/bottom_right_gifs/bottom_right_post_1_gif.png', 8)
bottom_right_post_1_end_frame = pygame.image.load('gifs/bottom_right_gifs/bottom_right_post_1_end_frame.png')
#
bottom_right_miss_1_gif = makeSprite('gifs/bottom_right_gifs/bottom_right_miss_1_gif.png', 8)
bottom_right_miss_1_end_frame = pygame.image.load('gifs/bottom_right_gifs/bottom_right_miss_1_end_frame.png')
#
bottom_right_crossbarparadox_2_gif = makeSprite('gifs/bottom_right_gifs/bottom_right_crossbarparadox_2_gif.png', 8)
bottom_right_crossbarparadox_2_end_frame = pygame.image.load('gifs/bottom_right_gifs/bottom_right_crossbarparadox_2_end_frame.png')

##############################################################################################################################################################################

# top right sprite sheets + end frames

top_right_goal_1_gif = makeSprite('gifs/top_right_gifs/top_right_goal_1_gif.png', 8)
top_right_goal_1_end_frame = pygame.image.load('gifs/top_right_gifs/top_right_goal_1_end_frame.png')

top_right_save_1_gif = makeSprite('gifs/top_right_gifs/top_right_save_1_gif.png', 8)
top_right_save_1_end_frame = pygame.image.load('gifs/top_right_gifs/top_right_save_1_end_frame.png')

top_right_crossbar_1_gif = makeSprite('gifs/top_right_gifs/top_right_crossbar_1_gif.png', 8)
top_right_crossbar_1_end_frame = pygame.image.load('gifs/top_right_gifs/top_right_crossbar_1_end_frame.png')

top_right_miss_1_gif = makeSprite('gifs/top_right_gifs/top_right_miss_1_gif.png', 8)                      # similar to crossbar gif, needs redoing
top_right_miss_1_end_frame = pygame.image.load('gifs/top_right_gifs/top_right_miss_1_end_frame.png')      # similar to crossbar gif, needs redoing

#top_right_saveparadox_1_gif = makeSprite('gifs/top_right_gifs/top_right_saveparadox_1_gif.png', 8)        # missing gif
#top_right_saveparadox_1_end_frame = pygame.image.load('gifs/top_right_gifs/top_right_saveparadox_1_end_frame.png') # missing gif

##############################################################################################################################################################################

Shot_selection_gif = makeSprite('gifs/Shot selector - 6 balls - sprite sheet.png', 28) #28 denotes to the makeSprite function that there are 28 different sprites in this image
top_middle_goal_sound = mixer.Sound('what_a_hit_son.wav')
running = True
font = pygame.font.Font('freesansbold.ttf', 15) # pygame font, parameter are font type and size

########################################################################################################################

player_choice = ''
penalty_table_tracker = ['','','','','']

#             0              1             2                3             4             5         6        7           8
areas = ('bottom left', 'top left', 'bottom middle', 'top middle', 'bottom right', 'top right', 'post', 'crossbar', 'miss')

player_history = []  # GOALIE GUESSING TECHNOLOGY


########################################################################################################################
########################################################################################################################

class Counter():
    game_count = 0
    goal_count = 0
    save_count = 0
    post_count = 0
    crossbar_count = 0
    miss_count = 0

    def goal_score(self):
        Counter.game_count += 1
        Counter.goal_count += 1

        return Counter.goal_count

    def save_made(self):
        Counter.game_count += 1
        Counter.save_count += 1

        return Counter.save_count

    def post_hit(self):
        Counter.game_count += 1
        Counter.post_count += 1

        return Counter.post_count

    def crossbar_hit(self):
        Counter.game_count += 1
        Counter.crossbar_count += 1

        return Counter.crossbar_count

    def complete_miss(self):
        Counter.game_count += 1
        Counter.miss_count += 1

        return Counter.miss_count

counters = Counter()

def score_counters():

    game_count_counter = font.render('SHOT NUMBER - ' + str(counters.game_count), True, red) #text object rendering, text, True to to take screen, black font colour
    goal_count_render = font.render('Goal count - ' + str(counters.goal_count), True, black) #text object rendering, text, True to to take screen, black font colour
    save_count_render = font.render('Save count - ' + str(counters.save_count), True, black)
    miss_count_render = font.render('Complete Miss count - ' + str(counters.miss_count), True, black)
    post_count_render = font.render('Post count - ' + str(counters.post_count), True, black)
    crossbar_count_render = font.render('Crossbar count - ' + str(counters.crossbar_count), True, black)

    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(game_count_counter, (600, 50))
    gameDisplay.blit(goal_count_render, (600, 200))
    gameDisplay.blit(save_count_render, (600, 240))
    gameDisplay.blit(miss_count_render, (600, 280))
    gameDisplay.blit(post_count_render, (600, 320))
    gameDisplay.blit(crossbar_count_render, (600, 360))

def penalty_tracker_box():

    penalty_tracker_box_x_coord = 291
    penalty_tracker_box_y_coord = 686
    icon_x_coord_offset = [6, 55, 104, 153, 202]

    penalty_tracker_box = pygame.image.load('images/new_shootout_indicator_cleaned.png').convert()
    penalty_tracker_box.set_alpha(200)
    gameDisplay.blit(penalty_tracker_box, (penalty_tracker_box_x_coord, penalty_tracker_box_y_coord))

    if counters.game_count == 1:
        gameDisplay.blit(penalty_table_tracker[0], (penalty_tracker_box_x_coord + icon_x_coord_offset[0], penalty_tracker_box_y_coord + 25))
    elif counters.game_count == 2:
        gameDisplay.blit(penalty_table_tracker[0],(penalty_tracker_box_x_coord + icon_x_coord_offset[0], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[1],(penalty_tracker_box_x_coord + icon_x_coord_offset[1], penalty_tracker_box_y_coord + 25))
    elif counters.game_count == 3:
        gameDisplay.blit(penalty_table_tracker[0],(penalty_tracker_box_x_coord + icon_x_coord_offset[0], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[1],(penalty_tracker_box_x_coord + icon_x_coord_offset[1], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[2],(penalty_tracker_box_x_coord + icon_x_coord_offset[2], penalty_tracker_box_y_coord + 25))
    elif counters.game_count == 4:
        gameDisplay.blit(penalty_table_tracker[0],(penalty_tracker_box_x_coord + icon_x_coord_offset[0], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[1],(penalty_tracker_box_x_coord + icon_x_coord_offset[1], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[2],(penalty_tracker_box_x_coord + icon_x_coord_offset[2], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[3],(penalty_tracker_box_x_coord + icon_x_coord_offset[3], penalty_tracker_box_y_coord + 25))
    elif counters.game_count == 5:
        gameDisplay.blit(penalty_table_tracker[0],(penalty_tracker_box_x_coord + icon_x_coord_offset[0], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[1],(penalty_tracker_box_x_coord + icon_x_coord_offset[1], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[2],(penalty_tracker_box_x_coord + icon_x_coord_offset[2], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[3],(penalty_tracker_box_x_coord + icon_x_coord_offset[3], penalty_tracker_box_y_coord + 25))
        gameDisplay.blit(penalty_table_tracker[4],(penalty_tracker_box_x_coord + icon_x_coord_offset[4], penalty_tracker_box_y_coord + 25))

    #print(penalty_table_tracker)
def penalty_tracker_box_updater(outcome):

    if outcome == 'goal':
        penalty_table_tracker[counters.game_count - 1] = green_ball
    elif outcome == 'no_goal':
        penalty_table_tracker[counters.game_count - 1] = red_x

def fade(gif_end_frame_sprite, width, height):

    pygame.time.delay(700)
    gameDisplay.blit(gif_end_frame_sprite, (width, height))
    fade = pygame.Surface((279, 360))
    fade.fill((black))
    for alpha in range(0, 50):
        fade.set_alpha(alpha)
        gameDisplay.blit(fade, (gif_x_coord_top_left_corner, gif_y_coord_top_left_corner))
        pygame.display.update()
        pygame.time.delay(50)

########################################################################################################################
########################################################################################################################
def game_logic(player_choice):
#                                                   bl    tl    bm    tm    br    tr   post  cbar  miss
    goalie_choice = random.choices(areas, weights=[0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.11, 0.11, 0.06], k=1)
    goalie_choice = goalie_choice[0]
    killSprite(Shot_selection_gif)

    if goalie_choice == areas[8]: #complete miss
        complete_miss(player_choice)

    elif goalie_choice == areas[7]: #crossbar
        crossbar_hit(player_choice)

    elif goalie_choice == areas[6]: #post
        post_hit(player_choice)

    elif player_choice == areas[0]:  # Goalie diving bottom left
        if goalie_choice == areas[0]:
            print('SAVE! The keeper dives low to the left and saves!')
            counters.save_made()
            gif_generation(bottom_left_save_1_gif, 300, 8, bottom_left_save_1_end_frame, 'no_goal')
            main_screen()
        else:
            print('GOAL! You rifle the ball in the left corner and it nestles in the net. Goal!')
            counters.goal_score() # if goal is scored, pass all bottom left goal outcomes thru random number generator function and output on of the goal outcomes
            gif_generation(bottom_left_goal_1_gif, 300, 8, bottom_left_goal_1_end_frame, 'goal')
            main_screen()
    elif player_choice == areas[1]:  # Goalie diving top left
        if goalie_choice == areas[1]:
            print('SAVE! The keeper leaps to the left corner and punches the ball clear!')
            counters.save_made()
            gif_generation(top_left_save_1_gif, 300, 8, top_left_save_1_end_frame, 'no_goal')
            main_screen()
        else:
            print('GOAL! You smash the ball into the top left corner!')
            counters.goal_score()
            gif_generation(top_left_goal_1_gif, 300, 8, top_left_goal_1_end_frame, 'goal')
            main_screen()
    elif player_choice == areas[2]:  # Goalie staying bottom middle
        if goalie_choice == areas[2]:
            print('SAVE! The keeper reads you and blocks the shot coming directly at him!')
            counters.save_made()
            gif_generation(bottom_middle_save_1_gif, 300, 8, bottom_middle_save_1_end_frame, 'no_goal')
            main_screen()
        else:
            print('GOAL! You double bluff the keeper and dink the ball down the middle!')
            counters.goal_score()
            gif_generation(bottom_middle_goal_1_gif, 300, 8, bottom_middle_goal_1_end_frame, 'goal')
            main_screen()
    elif player_choice == areas[3]:  # Goalie staying top middle
        if goalie_choice == areas[3]:
            print('SAVE! The keeper reads you palms the ball over the top of the crossbar!')
            counters.save_made()
            gif_generation(bottom_middle_save_1_gif, 300, 8, bottom_middle_save_1_end_frame, 'no_goal')  ####native gif doesn't exist
            main_screen()
        else:
            print('GOAL! You let fly and rocket the ball into the roof of the net!')
            counters.goal_score()
            gif_generation(top_middle_goal_1_gif, 300, 8, top_middle_goal_1_end_frame, 'goal')  #### black box slightly misaligned
            main_screen()
    elif player_choice == areas[4]:  # Goalie diving bottom right
        if goalie_choice == areas[4]:
            print('SAVE! The keeper pounces to the right and deflects the ball away!')
            counters.save_made()
            gif_generation(bottom_right_save_1_gif, 300, 8, bottom_right_save_1_end_frame, 'no_goal')
            main_screen()
        else:
            print('GOAL! You arrow the ball into the bottom right corner, keeper stood no chance!')
            counters.goal_score()
            gif_generation(bottom_right_goal_1_gif, 300, 8, bottom_right_goal_1_end_frame, 'goal')
            main_screen()
    elif player_choice == areas[5]:  # Goalie diving top right
        if goalie_choice == areas[5]:
            print('SAVE! The keeper reaches high and manages to redirect the ball over the crossbar!')
            counters.save_made()
            gif_generation(top_right_save_1_gif, 300, 8, top_right_save_1_end_frame, 'no_goal')
            main_screen()
        else:
            print('GOAL! You crack the ball into the top right corner of the goal!')
            counters.goal_score()
            gif_generation(top_right_goal_1_gif, 300, 8, top_right_goal_1_end_frame, 'goal')
            main_screen()

########################################################################################################################
########################################################################################################################

def complete_miss(player_choice):

    if player_choice == areas[0]:  # complete miss
        print('MISS! You drag your shot wide of the post!')  # missing the left post low - bottom low
        counters.complete_miss()
        gif_generation(bottom_left_miss_1_gif, 300, 8, bottom_left_miss_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[1]:
        print('MISS! You sky your shot wayward of the post!')  # missing the left post high - top left
        counters.complete_miss()
        gif_generation(bottom_left_post_1_gif, 300, 8, bottom_left_post_1_end_frame, 'no_goal')                          ### no gif
        main_screen()
    elif player_choice == areas[2]:
        print('SAVE! Your shot is easily gathered by the goalie!')  # 'missing' bottom low paradox - keeper gathers the shot - bottom low
        counters.save_made()
        gif_generation(bottom_middle_miss_3_gif, 300, 8, bottom_middle_miss_3_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[3]:
        print('MISS! Your shot is blazed over the crossbar!')  # missing over the crossbar - top middle
        counters.complete_miss()
        gif_generation(top_middle_miss_1_gif, 300, 8, top_middle_miss_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[4]:
        print('MISS! Your shot trickles passed the post!')  # missing the right post low - bottom right
        counters.complete_miss()
        gif_generation(bottom_right_miss_1_gif, 300, 8, bottom_right_miss_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[5]:
        print('MISS! Your shot flys high passed the post!')  # missing the right post high - top right
        counters.complete_miss()
        gif_generation(top_right_miss_1_gif, 300, 8, top_right_miss_1_end_frame, 'no_goal')
        main_screen()

########################################################################################################################

def crossbar_hit(player_choice):

    if player_choice == areas[0]:
        print('SAVE! The keeper manages to drop low and tip the ball around the left post!')  # bottom left and post paradox
        counters.save_made()
        gif_generation(bottom_left_saveparadox_1_gif, 300, 8, bottom_left_saveparadox_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[2]:  # bottom middle and crossbar paradox
        print('SAVE! The keeper stays rooted to the spot and denys the ball an introduction to the net!')
        counters.save_made()
        gif_generation(bottom_middle_crossbarparadox_2_gif, 300, 8, bottom_middle_crossbarparadox_2_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[4]:  # bottom right and crossbar paradox
        print('SAVE! The keeper gets a fingertip on the ball and nudges it around the post!')
        counters.save_made()
        gif_generation(bottom_right_crossbarparadox_2_gif, 300, 8, bottom_right_crossbarparadox_2_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[1]:  # hitting the left part of the crossbar
        print('CROSSBAR! The ball flys high and to the left but clips the crossbar and soars into the fans!')
        counters.crossbar_hit()
        gif_generation(top_left_crossbar_1_gif, 300, 8, top_left_crossbar_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[3]:  # hitting the middle of the crossbar
        print('CROSSBAR! The ball is smashed down the middle and canons off the crossbar!')
        counters.crossbar_hit()
        gif_generation(top_middle_crossbar_1_gif, 300, 8, top_middle_crossbar_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[5]:  # hitting the right part of the crossbar
        print('CROSSBAR! The ball flys high to the right and rattles the top of the crossbar!')
        counters.crossbar_hit()
        gif_generation(top_right_crossbar_1_gif, 300, 8, top_right_crossbar_1_end_frame, 'no_goal')
        main_screen()

########################################################################################################################

def post_hit(player_choice):

    if player_choice == areas[2]:  # bottom middle and post paradox
        print('SAVE! The keeper began to dive but managed a save with his trailing leg!')
        counters.save_made()
        gif_generation(bottom_middle_postparadox_4_gif, 300, 8, bottom_middle_postparadox_4_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[3]:  # top middle and post paradox
        print('SAVE! The keeper managed to claw the ball away with a finger-tip save!')
        counters.save_made()                                                                                            ###no gif
        gif_generation(bottom_left_post_1_gif, 300, 8, bottom_left_post_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[0]:  # hitting the bottom left post
        print('POST! The shot rifles towards the left but thunders off the post!')
        counters.post_hit()
        gif_generation(bottom_left_post_1_gif, 300, 8, bottom_left_post_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[1]:  # hitting the top left post
        print('POST! The shot looks destined for the top left corner but canons off the post!')
        counters.post_hit()                                                                                             ###no gif
        gif_generation(bottom_left_post_1_gif, 300, 8, bottom_left_post_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[4]:  # hitting the bottom right post
        print('POST! The daisy cutter of a shot looks promising but rockets off the bottom of the post!')
        counters.post_hit()
        gif_generation(bottom_right_post_1_gif, 300, 8, bottom_right_post_1_end_frame, 'no_goal')
        main_screen()
    elif player_choice == areas[5]:  # hitting the top right post
        print('POST! The keeper is motionless as he watches the ball ricochet off the post!')
        counters.post_hit()                                                                                             ###no gif
        gif_generation(bottom_left_post_1_gif, 300, 8, bottom_left_post_1_end_frame, 'no_goal')
        main_screen()

########################################################################################################################

########################################################################################################################
########################################################################################################################

def gif_generation(gif, speed, gif_end_frame, gif_end_frame_sprite, goal = 0, sound = 0):


    moveSprite(gif, gif_x_coord_top_left_corner, gif_y_coord_top_left_corner)  # pass gif thru the function, true references the centre of the sprite, so it appears at the coordinate at the middle of the sprite, no true means sprite is placed at top left corner
    showSprite(gif)
    nextFrame = clock()
    frame = 0 #current frame of animation

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:  # this allow the user to quit, pygame.QUIT is a pygame function (hitting the x in the top right)
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # This gets any event that is happening on the screen, where is the mouse clicking, keys presses EVERYTHING
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if clock() > nextFrame:
            frame = (frame + 1)  # keep increasing the frame by one
            nextFrame += speed  # this controls the speed of the gif
            if frame == 3:
                if sound == 0:
                    pass
                else:
                    sound.play()
            if frame == gif_end_frame:
                fade(gif_end_frame_sprite, gif_x_coord_top_left_corner, gif_y_coord_top_left_corner)
                killSprite(gif)
                penalty_tracker_box_updater(goal)
                main_screen()  # ending the gif and calling main_screen to go back to the selection screen
        changeSpriteImage(gif, frame)

########################################################################################################################
########################################################################################################################

def main_screen():

    #background_music = mixer.music.load('champions_league_anthem.mp3')
    #mixer.music.play(-1) #runs music in a loop
    click = False
    while counters.game_count < 10:

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
                            mixer.music.stop()
                            player_choice = areas[0]
                            game_logic(player_choice)


                elif 349 + 10 > mouse[0] > 349 and 275 + 10 > mouse[1] > 275:  # top left setting up code to determine whether the mouse position is within the shooting box, #top left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            player_choice = areas[1]
                            game_logic(player_choice)


                elif 395 + 10 > mouse[0] > 395 and 300 + 10 > mouse[1] > 300:  # bottom middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            player_choice = areas[2]
                            game_logic(player_choice)


                elif 396 + 10 > mouse[0] > 396 and 279 + 10 > mouse[1] > 279:  # top middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            player_choice = areas[3]
                            game_logic(player_choice)


                elif 442 + 10 > mouse[0] > 442 and 302 + 10 > mouse[1] > 302:  # bottom right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            player_choice = areas[4]
                            game_logic(player_choice)


                elif 442 + 10 > mouse[0] > 442 and 282 + 10 > mouse[1] > 282:  # top right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            player_choice = areas[5]
                            game_logic(player_choice)


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
            penalty_tracker_box()


########################################################################################################################


main_screen()