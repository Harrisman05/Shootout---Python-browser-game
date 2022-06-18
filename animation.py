
##################### TESTING BRANCH ####################
import pygame, sys
import random
from pygame_functions import *
from pygame.locals import *
import pyinputplus as pyip
from pygame import mixer
import time
pygame.init() # intialise pygame


screenSize(800, 800)
setBackgroundImage('gifs/background.jpeg')
background = pygame.image.load('gifs/background.jpeg')  # loading of the background image
display_width = 800
display_height = 800
gif_x_coord_top_left_corner = (display_width / 2) - 130.5
gif_y_coord_top_left_corner = (display_width / 2) - 180
gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.blit(background, (0, 0))
click = False
gif_speed = 5

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = 	(0,0,255)
violet = (127, 0, 255)
dark_green = (0,100,0)
nextFrame = clock() #time at which next frame will appear`
frame = 0 #current frame of animation, set to zero as that is the index of the first frame
tick(60)

##############################################################################################################################################################################

Shot_selection_gif = makeSprite('gifs/Shot selector - 6 balls - sprite sheet.png', 28) #28 denotes to the makeSprite function that there are 28 different sprites in this image
top_middle_goal_sound = mixer.Sound('what_a_hit_son.wav')
running = True
font = pygame.font.Font('freesansbold.ttf', 15) # pygame font, parameter are font type and size
header_font = pygame.font.Font('freesansbold.ttf', 30)

choice_evaluator = ''
single_player_choice = ''
head_to_head_player_1_choice = ''
head_to_head_player_2_choice = ''
single_player_penalty_table_tracker = ['', '', '', '', '']

#             0              1             2                3             4             5         6        7           8
areas = ('bottom left', 'top left', 'bottom middle', 'top middle', 'bottom right', 'top right', 'post', 'crossbar', 'miss')

player_history = []  # GOALIE GUESSING TECHNOLOGY

##############################################################################################################################################################################

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

########################################################################################################################
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 35)
            text = font.render(self.text, 1, black)
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, mouse):
        # Mouse is the mouse position or a tuple of (x,y) coordinates
        if mouse[0] > self.x and mouse[0] < self.x + self.width:
            if mouse[1] > self.y and mouse[1] < self.y + self.height:
                return True

        return False

class Counter():

    head_to_head_game_count = 0
    single_player_game_count = 0
    sudden_death = False

    def __init__(self, player):

        self.player = player
        self.goal_count = 0
        self.save_count = 0
        self. post_count = 0
        self.crossbar_count = 0
        self.miss_count = 0
        self.player_game_count = 0
        self.goal_tracker = ['','','','','']
        self.gif_table = ['', '', '', '', '']


    def reset(self, player):
        self.__init__(player)
        Counter.head_to_head_game_count = 0
        Counter.sudden_death = False

    def goal_score(self):
        self.goal_count += 1
        self.player_game_count += 1

        return self.goal_count

    def save_made(self):
        self.save_count += 1
        self.player_game_count += 1

        return self.save_count

    def post_hit(self):
        self.post_count += 1
        self.player_game_count += 1

        return self.post_count

    def crossbar_hit(self):
        self.crossbar_count += 1
        self.player_game_count += 1

        return self.crossbar_count

    def complete_miss(self):
        self.miss_count += 1
        self.player_game_count += 1

        return self.miss_count

    def goal_tracker_reset(self):

        self.player_game_count = 0
        self.goal_tracker = ['','','','','']
        self.gif_table = ['', '', '', '', '']
        Counter.reset_head_to_head_game_counter()


    def __str__(self):
        return f'I am the counter of {self.player}'

    @classmethod
    def increase_head_to_head_game_counter(cls):
        cls.head_to_head_game_count += 1

    @classmethod
    def increase_single_player_game_counter(cls):
        cls.single_player_game_count += 1

    @classmethod
    def sudden_death_initiate(cls):
        cls.sudden_death = True

    @classmethod
    def reset_head_to_head_game_counter(cls):
        cls.head_to_head_game_count = 0


single_player_counters = Counter('single player mode')
head_to_head_player_1_counters = Counter('player_1')
head_to_head_player_2_counters = Counter('player_2')

def score_counters(*args):

    if args[0] == single_player_counters:

        game_count_render = font.render('SHOT NUMBER - ' + str(args[0].head_to_head_game_count), True, red)
        goal_count_render = font.render('Goal count - ' + str(args[0].goal_count), True, black)
        save_count_render = font.render('Save count - ' + str(args[0].save_count), True, black)
        miss_count_render = font.render('Complete Miss count - ' + str(args[0].miss_count), True, black)
        post_count_render = font.render('Post count - ' + str(args[0].post_count), True, black)
        crossbar_count_render = font.render('Crossbar count - ' + str(args[0].crossbar_count), True, black)

        gameDisplay.blit(background, (0, 0))
        pygame.draw.rect(gameDisplay, white, pygame.Rect(587, 192, 200, 190))

        gameDisplay.blit(game_count_render, (600, 50))
        gameDisplay.blit(goal_count_render, (600, 200))
        gameDisplay.blit(save_count_render, (600, 240))
        gameDisplay.blit(miss_count_render, (600, 280))
        gameDisplay.blit(post_count_render, (600, 320))
        gameDisplay.blit(crossbar_count_render, (600, 360))

    elif args[0] == head_to_head_player_1_counters and args[1] == head_to_head_player_2_counters:

        player_1and2_game_count_render = font.render('SHOT NUMBER - ' + str(args[0].head_to_head_game_count), True,red)  # text object rendering, text, True to to take screen, black font colour

        player_1_menu_render = font.render('PLAYER 1 COUNTERS', True, violet)
        player_1_goal_count_render = font.render('Goal count - ' + str(args[0].goal_count), True,black)  # text object rendering, text, True to to take screen, black font colour
        player_1_save_count_render = font.render('Save count - ' + str(args[0].save_count), True, black)
        player_1_miss_count_render = font.render('Complete Miss count - ' + str(args[0].miss_count), True, black)
        player_1_post_count_render = font.render('Post count - ' + str(args[0].post_count), True, black)
        player_1_crossbar_count_render = font.render('Crossbar count - ' + str(args[0].crossbar_count), True, black)

        player_2_menu_render = font.render('PLAYER 2 COUNTERS', True, violet)
        player_2_goal_count_render = font.render('Goal count - ' + str(args[1].goal_count), True,black)  # text object rendering, text, True to to take screen, black font colour
        player_2_save_count_render = font.render('Save count - ' + str(args[1].save_count), True, black)
        player_2_miss_count_render = font.render('Complete Miss count - ' + str(args[1].miss_count), True, black)
        player_2_post_count_render = font.render('Post count - ' + str(args[1].post_count), True, black)
        player_2_crossbar_count_render = font.render('Crossbar count - ' + str(args[1].crossbar_count), True, black)

        gameDisplay.blit(background, (0, 0))
        pygame.draw.rect(gameDisplay, white, pygame.Rect(587, 192, 200, 190))
        pygame.draw.rect(gameDisplay, white, pygame.Rect(15, 192, 200, 190))

        gameDisplay.blit(player_1and2_game_count_render, (600, 50))

        gameDisplay.blit(player_1_menu_render, (600, 160))
        gameDisplay.blit(player_1_goal_count_render, (600, 200))
        gameDisplay.blit(player_1_save_count_render, (600, 240))
        gameDisplay.blit(player_1_miss_count_render, (600, 280))
        gameDisplay.blit(player_1_post_count_render, (600, 320))
        gameDisplay.blit(player_1_crossbar_count_render, (600, 360))

        gameDisplay.blit(player_2_menu_render, (20, 160))
        gameDisplay.blit(player_2_goal_count_render, (20, 200))
        gameDisplay.blit(player_2_save_count_render, (20, 240))
        gameDisplay.blit(player_2_miss_count_render, (20, 280))
        gameDisplay.blit(player_2_post_count_render, (20, 320))
        gameDisplay.blit(player_2_crossbar_count_render, (20, 360))

def penalty_tracker_box(*args):

    icon_x_coord_offset = [6, 55, 104, 153, 202]
    icon_y_coord_offset = 25

    if args[0] == single_player_counters:
        penalty_tracker_box_x_coord = 291
        penalty_tracker_box_y_coord = 686

        penalty_tracker_box = pygame.image.load('images/new_shootout_indicator_cleaned.png').convert()
        gameDisplay.blit(penalty_tracker_box, (penalty_tracker_box_x_coord, penalty_tracker_box_y_coord))

        if args[0].single_player_game_count == 1:
            gameDisplay.blit(single_player_penalty_table_tracker[0], (penalty_tracker_box_x_coord + icon_x_coord_offset[0], penalty_tracker_box_y_coord + icon_y_coord_offset))
        elif args[0].single_player_game_count == 2:
            for index in range(0,2):
                gameDisplay.blit(single_player_penalty_table_tracker[index], (penalty_tracker_box_x_coord + icon_x_coord_offset[index], penalty_tracker_box_y_coord + icon_y_coord_offset))
        elif args[0].single_player_game_count == 3:
            for index in range(0, 3):
                gameDisplay.blit(single_player_penalty_table_tracker[index], (penalty_tracker_box_x_coord + icon_x_coord_offset[index], penalty_tracker_box_y_coord + icon_y_coord_offset))
        elif args[0].single_player_game_count == 4:
            for index in range(0, 4):
                gameDisplay.blit(single_player_penalty_table_tracker[index], (penalty_tracker_box_x_coord + icon_x_coord_offset[index], penalty_tracker_box_y_coord + icon_y_coord_offset))
        elif args[0].single_player_game_count == 5:
            for index in range(0, 5):
                gameDisplay.blit(single_player_penalty_table_tracker[index], (penalty_tracker_box_x_coord + icon_x_coord_offset[index], penalty_tracker_box_y_coord + icon_y_coord_offset))

    elif args[0] == head_to_head_player_1_counters and args[1] == head_to_head_player_2_counters:

        player_1_penalty_tracker_box_x_coord = 555
        player_2_penalty_tracker_box_x_coord = 5
        player_1and2_penalty_tracker_box_y_coord = 392

        penalty_tracker_box_player_1 = pygame.image.load('images/new_shootout_indicator_cleaned.png').convert()
        penalty_tracker_box_player_2 = pygame.image.load('images/new_shootout_indicator_cleaned.png').convert()
        gameDisplay.blit(penalty_tracker_box_player_1, (555, 392))
        gameDisplay.blit(penalty_tracker_box_player_2, (5, 392))

        if args[0].head_to_head_game_count == 1:

            gameDisplay.blit(args[0].gif_table[0], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[0], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 2:

            gameDisplay.blit(args[0].gif_table[0], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[0], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

            gameDisplay.blit(args[1].gif_table[0], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[0], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 3:

            for index in range(0, 2):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

            gameDisplay.blit(args[1].gif_table[0], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[0], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 4:

            for index in range(0, 2):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))
                gameDisplay.blit(args[1].gif_table[index], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 5:

            for index in range(0, 3):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

            for index in range(0, 2):
                gameDisplay.blit(args[1].gif_table[index], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 6:

            for index in range(0, 3):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))
                gameDisplay.blit(args[1].gif_table[index], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 7:

            for index in range(0, 4):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

            for index in range(0, 3):
                gameDisplay.blit(args[1].gif_table[index], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 8:

            for index in range(0, 4):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))
                gameDisplay.blit(args[1].gif_table[index], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 9:

            for index in range(0, 5):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

            for index in range(0, 4):
                gameDisplay.blit(args[1].gif_table[index], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

        elif args[0].head_to_head_game_count == 10:

            for index in range(0, 5):
                gameDisplay.blit(args[0].gif_table[index], (player_1_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

            for index in range(0, 5):
                gameDisplay.blit(args[1].gif_table[index], (player_2_penalty_tracker_box_x_coord + icon_x_coord_offset[index], player_1and2_penalty_tracker_box_y_coord + icon_y_coord_offset))

def penalty_tracker_box_updater(outcome, counter_type):

    if counter_type.player_game_count == 6:
        counter_type.player_game_count = 0
    else:
        pass

    if counter_type == single_player_counters:
        Counter.increase_single_player_game_counter()
        if outcome == 'goal':
            single_player_penalty_table_tracker[counter_type.single_player_game_count - 1] = green_ball
        elif outcome == 'no_goal':
            single_player_penalty_table_tracker[counter_type.single_player_game_count - 1] = red_x

    elif counter_type == head_to_head_player_1_counters:
        Counter.increase_head_to_head_game_counter()
        if outcome == 'goal':
            counter_type.gif_table[counter_type.player_game_count - 1] = green_ball
        elif outcome == 'no_goal':
            counter_type.gif_table[counter_type.player_game_count - 1] = red_x

    elif counter_type == head_to_head_player_2_counters:
        Counter.increase_head_to_head_game_counter()
        if outcome == 'goal':
            counter_type.gif_table[counter_type.player_game_count - 1] = green_ball
        elif outcome == 'no_goal':
            counter_type.gif_table[counter_type.player_game_count - 1] = red_x

def per_shot_table_updater(outcome, counter_type):

    for i in enumerate(counter_type.goal_tracker):
        if i[1] == '':
            counter_type.goal_tracker[i[0]] = outcome
            break

    return None

def outcome_calculator(player1 = None, player2 = None):

    def available_slots_calc(list_table):
        available_slots = 0
        for i in list_table.goal_tracker:
            if i == "":
                available_slots += 1

        return available_slots

    def goals_scored(list_table):
        goals_scored = 0
        for i in list_table.goal_tracker:
            if i == 'goal':
                goals_scored += 1

        return goals_scored

    def shot_counter(list_table):
        shot_counter = 0
        for i in list_table.goal_tracker:
            if i == 'goal' or i == 'no_goal':
                shot_counter += 1
        return shot_counter

    player_1_slots = available_slots_calc(player1)
    player_2_slots = available_slots_calc(player2)
    player_1_goals = goals_scored(player1)
    player_2_goals = goals_scored(player2)
    player_1_shot_counter = shot_counter(player1)
    player_2_shot_counter = shot_counter(player2)

    #print(str(player_1_slots) + ' - player 1 slots\n', str(player_1_goals) + ' - player 1 goals\n', str(player_2_slots) + ' - player 2 slots\n', str(player_2_goals) + ' - player 2 goals\n')

    if Counter.sudden_death == False:
        if player_2_shot_counter == 5:

            pass

            if player_1_goals > player_2_goals:
                print('player 1 wins as he has scored more goals')
                killSprite(Shot_selection_gif)
                pygame.time.wait(2000)
                select_menu()

            elif player_2_goals > player_1_goals:
                print('player 2 wins as he has scored more goals')
                killSprite(Shot_selection_gif)
                pygame.time.wait(2000)
                select_menu()

            elif player_1_goals == player_2_goals or player_1_goals == player_2_goals:

                print('The shootout ends in a draw')

        #if player_1_shot_counter == player_2_shot_counter:
        if player_1_goals > player_2_slots + player_2_goals:
            print('player 1 wins as player 2 does not have enough shots remaining')
            killSprite(Shot_selection_gif)
            pygame.time.wait(2000)
            select_menu()
        elif player_2_goals > player_1_slots + player_1_goals:
            print('player 2 wins as player 1 does not have enough shots remaining')
            killSprite(Shot_selection_gif)
            pygame.time.wait(2000)
            select_menu()

    elif Counter.sudden_death == True:

        if player_1_shot_counter == player_2_shot_counter:

            if player_1_goals > player_2_goals:
                print('Sudden death, player 1 wins')

            elif player_2_goals > player_1_goals:
                print('Sudden death, player 2 wins')

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


def game_type_assessor(single_player_choice = None, head_to_head_player_1_choice = None, head_to_head_player_2_choice = None):

    if head_to_head_player_1_choice == None and head_to_head_player_2_choice == None: # not playing head to head, only single player
        return single_player_choice
    elif single_player_choice == None and head_to_head_player_2_choice == None: # playing head to head, player 1 choice
        return head_to_head_player_1_choice
    elif single_player_choice == None and head_to_head_player_1_choice == None: # playing head to head, player 2 choice
        return head_to_head_player_2_choice

########################################################################################################################
########################################################################################################################
def game_logic(counter_type, single_player_choice = None, head_to_head_player_1_choice = None, head_to_head_player_2_choice = None):

    global gif_speed
    choice_evaluator = game_type_assessor(single_player_choice, head_to_head_player_1_choice, head_to_head_player_2_choice)
#                                                   bl    tl    bm    tm    br    tr   post  cbar  miss
    goalie_choice = random.choices(areas, weights = [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.11, 0.11, 0.06], k=1)
    goalie_choice = goalie_choice[0]
    killSprite(Shot_selection_gif)

    if goalie_choice == areas[8]: #complete miss
        complete_miss(counter_type, choice_evaluator)

    elif goalie_choice == areas[7]: #crossbar
        crossbar_hit(counter_type, choice_evaluator)

    elif goalie_choice == areas[6]: #post
        post_hit(counter_type, choice_evaluator)

    elif choice_evaluator == areas[0]:  # Goalie diving bottom left
        if goalie_choice == areas[0]:
            print('SAVE! The keeper dives low to the left and saves!')
            counter_type.save_made()
            gif_generation(bottom_left_save_1_gif, gif_speed, 8, bottom_left_save_1_end_frame, counter_type, 'no_goal')
        else:
            print('GOAL! You rifle the ball in the left corner and it nestles in the net. Goal!')
            counter_type.goal_score() # if goal is scored, pass all bottom left goal outcomes thru random number generator function and output on of the goal outcomes
            gif_generation(bottom_left_goal_1_gif, gif_speed, 8, bottom_left_goal_1_end_frame, counter_type, 'goal')

    elif choice_evaluator == areas[1]:  # Goalie diving top left
        if goalie_choice == areas[1]:
            print('SAVE! The keeper leaps to the left corner and punches the ball clear!')
            counter_type.save_made()
            gif_generation(top_left_save_1_gif, gif_speed, 8, top_left_save_1_end_frame, counter_type, 'no_goal')
        else:
            print('GOAL! You smash the ball into the top left corner!')
            counter_type.goal_score()
            gif_generation(top_left_goal_1_gif, gif_speed, 8, top_left_goal_1_end_frame, counter_type, 'goal')
    elif choice_evaluator == areas[2]:  # Goalie staying bottom middle
        if goalie_choice == areas[2]:
            print('SAVE! The keeper reads you and blocks the shot coming directly at him!')
            counter_type.save_made()
            gif_generation(bottom_middle_save_1_gif, gif_speed, 8, bottom_middle_save_1_end_frame, counter_type, 'no_goal')
        else:
            print('GOAL! You double bluff the keeper and dink the ball down the middle!')
            counter_type.goal_score()
            gif_generation(bottom_middle_goal_1_gif, gif_speed, 8, bottom_middle_goal_1_end_frame, counter_type, 'goal')
    elif choice_evaluator == areas[3]:  # Goalie staying top middle
        if goalie_choice == areas[3]:
            print('SAVE! The keeper reads you palms the ball over the top of the crossbar!')
            counter_type.save_made()
            gif_generation(bottom_middle_save_1_gif, gif_speed, 8, bottom_middle_save_1_end_frame, counter_type, 'no_goal')  ####native gif doesn't exist
        else:
            print('GOAL! You let fly and rocket the ball into the roof of the net!')
            counter_type.goal_score()
            gif_generation(top_middle_goal_1_gif, gif_speed, 8, top_middle_goal_1_end_frame, counter_type, 'goal')  #### black box slightly misaligned
    elif choice_evaluator == areas[4]:  # Goalie diving bottom right
        if goalie_choice == areas[4]:
            print('SAVE! The keeper pounces to the right and deflects the ball away!')
            counter_type.save_made()
            gif_generation(bottom_right_save_1_gif, gif_speed, 8, bottom_right_save_1_end_frame, counter_type, 'no_goal')
        else:
            print('GOAL! You arrow the ball into the bottom right corner, keeper stood no chance!')
            counter_type.goal_score()
            gif_generation(bottom_right_goal_1_gif, gif_speed, 8, bottom_right_goal_1_end_frame, counter_type, 'goal')
    elif choice_evaluator == areas[5]:  # Goalie diving top right
        if goalie_choice == areas[5]:
            print('SAVE! The keeper reaches high and manages to redirect the ball over the crossbar!')
            counter_type.save_made()
            gif_generation(top_right_save_1_gif, gif_speed, 8, top_right_save_1_end_frame, counter_type, 'no_goal')
        else:
            print('GOAL! You crack the ball into the top right corner of the goal!')
            counter_type.goal_score()
            gif_generation(top_right_goal_1_gif, gif_speed, 8, top_right_goal_1_end_frame, counter_type, 'goal')

########################################################################################################################
########################################################################################################################

def complete_miss(counter_type, single_player_choice = None, head_to_head_player_1_choice = None, head_to_head_player_2_choice = None):

    global gif_speed
    choice_evaluator = game_type_assessor(single_player_choice, head_to_head_player_1_choice, head_to_head_player_2_choice)

    if choice_evaluator == areas[0]:  # complete miss
        print('MISS! You drag your shot wide of the post!')  # missing the left post low - bottom low
        counter_type.complete_miss()
        gif_generation(bottom_left_miss_1_gif, gif_speed, 8, bottom_left_miss_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[1]:
        print('MISS! You sky your shot wayward of the post!')  # missing the left post high - top left
        counter_type.complete_miss()
        gif_generation(bottom_left_post_1_gif, gif_speed, 8, bottom_left_post_1_end_frame, counter_type, 'no_goal')                          ### no gif
    elif choice_evaluator == areas[2]:
        print('SAVE! Your shot is easily gathered by the goalie!')  # 'missing' bottom low paradox - keeper gathers the shot - bottom low
        counter_type.save_made()
        gif_generation(bottom_middle_miss_3_gif, gif_speed, 8, bottom_middle_miss_3_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[3]:
        print('MISS! Your shot is blazed over the crossbar!')  # missing over the crossbar - top middle
        counter_type.complete_miss()
        gif_generation(top_middle_miss_1_gif, gif_speed, 8, top_middle_miss_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[4]:
        print('MISS! Your shot trickles passed the post!')  # missing the right post low - bottom right
        counter_type.complete_miss()
        gif_generation(bottom_right_miss_1_gif, gif_speed, 8, bottom_right_miss_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[5]:
        print('MISS! Your shot flys high passed the post!')  # missing the right post high - top right
        counter_type.complete_miss()
        gif_generation(top_right_miss_1_gif, gif_speed, 8, top_right_miss_1_end_frame, counter_type, 'no_goal')

########################################################################################################################

def crossbar_hit(counter_type, single_player_choice = None, head_to_head_player_1_choice = None, head_to_head_player_2_choice = None):

    choice_evaluator = game_type_assessor(single_player_choice, head_to_head_player_1_choice,head_to_head_player_2_choice)

    if choice_evaluator == areas[0]:
        print('SAVE! The keeper manages to drop low and tip the ball around the left post!')  # bottom left and post paradox
        counter_type.save_made()
        gif_generation(bottom_left_saveparadox_1_gif, gif_speed, 8, bottom_left_saveparadox_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[2]:  # bottom middle and crossbar paradox
        print('SAVE! The keeper stays rooted to the spot and denys the ball an introduction to the net!')
        counter_type.save_made()
        gif_generation(bottom_middle_crossbarparadox_2_gif, gif_speed, 8, bottom_middle_crossbarparadox_2_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[4]:  # bottom right and crossbar paradox
        print('SAVE! The keeper gets a fingertip on the ball and nudges it around the post!')
        counter_type.save_made()
        gif_generation(bottom_right_crossbarparadox_2_gif, gif_speed, 8, bottom_right_crossbarparadox_2_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[1]:  # hitting the left part of the crossbar
        print('CROSSBAR! The ball flys high and to the left but clips the crossbar and soars into the fans!')
        counter_type.crossbar_hit()
        gif_generation(top_left_crossbar_1_gif, gif_speed, 8, top_left_crossbar_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[3]:  # hitting the middle of the crossbar
        print('CROSSBAR! The ball is smashed down the middle and canons off the crossbar!')
        counter_type.crossbar_hit()
        gif_generation(top_middle_crossbar_1_gif, gif_speed, 8, top_middle_crossbar_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[5]:  # hitting the right part of the crossbar
        print('CROSSBAR! The ball flys high to the right and rattles the top of the crossbar!')
        counter_type.crossbar_hit()
        gif_generation(top_right_crossbar_1_gif, gif_speed, 8, top_right_crossbar_1_end_frame, counter_type, 'no_goal')

########################################################################################################################

def post_hit(counter_type, single_player_choice = None, head_to_head_player_1_choice = None, head_to_head_player_2_choice = None):

    choice_evaluator = game_type_assessor(single_player_choice, head_to_head_player_1_choice,head_to_head_player_2_choice)

    if choice_evaluator == areas[2]:  # bottom middle and post paradox
        print('SAVE! The keeper began to dive but managed a save with his trailing leg!')
        counter_type.save_made()
        gif_generation(bottom_middle_postparadox_4_gif, gif_speed, 8, bottom_middle_postparadox_4_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[3]:  # top middle and post paradox
        print('SAVE! The keeper managed to claw the ball away with a finger-tip save!')
        counter_type.save_made()                                                                                            ###no gif
        gif_generation(bottom_left_post_1_gif, gif_speed, 8, bottom_left_post_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[0]:  # hitting the bottom left post
        print('POST! The shot rifles towards the left but thunders off the post!')
        counter_type.post_hit()
        gif_generation(bottom_left_post_1_gif, gif_speed, 8, bottom_left_post_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[1]:  # hitting the top left post
        print('POST! The shot looks destined for the top left corner but canons off the post!')
        counter_type.post_hit()                                                                                             ###no gif
        gif_generation(bottom_left_post_1_gif, gif_speed, 8, bottom_left_post_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[4]:  # hitting the bottom right post
        print('POST! The daisy cutter of a shot looks promising but rockets off the bottom of the post!')
        counter_type.post_hit()
        gif_generation(bottom_right_post_1_gif, gif_speed, 8, bottom_right_post_1_end_frame, counter_type, 'no_goal')
    elif choice_evaluator == areas[5]:  # hitting the top right post
        print('POST! The keeper is motionless as he watches the ball ricochet off the post!')
        counter_type.post_hit()                                                                                             ###no gif
        gif_generation(bottom_left_post_1_gif, gif_speed, 8, bottom_left_post_1_end_frame, counter_type, 'no_goal')

########################################################################################################################

########################################################################################################################
########################################################################################################################

def gif_generation(gif, speed, gif_end_frame, gif_end_frame_sprite, counter_type, goal = None, sound = None):

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
                if sound == None:
                    pass
                else:
                    sound.play()
            if frame == gif_end_frame:
                #fade(gif_end_frame_sprite, gif_x_coord_top_left_corner, gif_y_coord_top_left_corner)
                killSprite(gif)
                penalty_tracker_box_updater(goal, counter_type)
                per_shot_table_updater(goal, counter_type)
                if counter_type == single_player_counters:
                    single_player_loop()
                elif counter_type == head_to_head_player_1_counters or head_to_head_player_2_counters:
                    if Counter.sudden_death == False:
                        head_to_head_loop()# ending the gif and calling main_screen to go back to the selection screen
                    elif Counter.sudden_death == True:
                        sudden_death_loop()

        changeSpriteImage(gif, frame)

########################################################################################################################
########################################################################################################################

def single_player_loop():

    return_to_menu_button = button(green, 29, 697, 250, 100, 'Return to menu')
    click = False
    #background_music = mixer.music.load('champions_league_anthem.mp3')
    #mixer.music.play(-1) #runs music in a loop
    while single_player_counters.single_player_game_count < 10:

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
                    if return_to_menu_button.isOver(mouse):
                        select_menu()
                if event.type == MOUSEMOTION:
                    if return_to_menu_button.isOver(mouse):
                        return_to_menu_button.color = (red)
                    else:
                        return_to_menu_button.color = (green)
                mouse = pygame.mouse.get_pos()  # mouse needs to be in the for event, otherwise it doesn't live update
                print(mouse)

                if 355 + 10 > mouse[0] > 355 and 301 + 10 > mouse[1] > 301:  # bottom left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            single_player_choice = areas[0]
                            game_logic(single_player_counters, single_player_choice)


                elif 349 + 10 > mouse[0] > 349 and 275 + 10 > mouse[1] > 275:  # top left setting up code to determine whether the mouse position is within the shooting box, #top left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            single_player_choice = areas[1]
                            game_logic(single_player_counters, single_player_choice)


                elif 395 + 10 > mouse[0] > 395 and 300 + 10 > mouse[1] > 300:  # bottom middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            single_player_choice = areas[2]
                            game_logic(single_player_counters, single_player_choice)


                elif 396 + 10 > mouse[0] > 396 and 279 + 10 > mouse[1] > 279:  # top middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            single_player_choice = areas[3]
                            game_logic(single_player_counters, single_player_choice)


                elif 442 + 10 > mouse[0] > 442 and 302 + 10 > mouse[1] > 302:  # bottom right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            single_player_choice = areas[4]
                            game_logic(single_player_counters, single_player_choice)


                elif 442 + 10 > mouse[0] > 442 and 282 + 10 > mouse[1] > 282:  # top right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            single_player_choice = areas[5]
                            game_logic(single_player_counters, single_player_choice)


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

            score_counters(single_player_counters)
            penalty_tracker_box(single_player_counters)

            return_to_menu_button.draw(background, (0, 0, 0))

            game_type_label = header_font.render('Single Player', True, dark_green)
            gameDisplay.blit(game_type_label, (282, 3))

def head_to_head_loop():
    # background_music = mixer.music.load('champions_league_anthem.mp3')
    # mixer.music.play(-1) #runs music in a loop]
    click = False
    return_to_menu_button = button(green, 29, 697, 250, 100, 'Return to menu')

    if head_to_head_player_1_counters.head_to_head_game_count % 2 == 0: #if game count is odd
        selected_player_counter = head_to_head_player_1_counters
        selected_player_choice = head_to_head_player_1_choice
        player_1_turn = True
    else:
        selected_player_counter = head_to_head_player_2_counters
        selected_player_choice = head_to_head_player_2_choice
        player_1_turn = False

    while head_to_head_player_1_counters.head_to_head_game_count <= 10:

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
                    if return_to_menu_button.isOver(mouse):
                        select_menu()
                if event.type == MOUSEMOTION:
                    if return_to_menu_button.isOver(mouse):
                        return_to_menu_button.color = (red)
                    else:
                        return_to_menu_button.color = (green)

                mouse = pygame.mouse.get_pos()  # mouse needs to be in the for event, otherwise it doesn't live update
                #print(mouse)

                if 355 + 10 > mouse[0] > 355 and 301 + 10 > mouse[1] > 301:  # bottom left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[0]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)

                elif 349 + 10 > mouse[0] > 349 and 275 + 10 > mouse[1] > 275:  # top left setting up code to determine whether the mouse position is within the shooting box, #top left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[1]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)



                elif 395 + 10 > mouse[0] > 395 and 300 + 10 > mouse[1] > 300:  # bottom middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[2]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)


                elif 396 + 10 > mouse[0] > 396 and 279 + 10 > mouse[1] > 279:  # top middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[3]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)


                elif 442 + 10 > mouse[0] > 442 and 302 + 10 > mouse[1] > 302:  # bottom right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[4]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)


                elif 442 + 10 > mouse[0] > 442 and 282 + 10 > mouse[1] > 282:  # top right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[5]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)

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

            if clock() > nextFrame:  # this is constantly looking at the clock and is seeing if enough time has passed to play the next frame
                frame = (frame + 1)  # keep increasing the frame by one
                nextFrame += 30  # this controls the speed of the gif
                if frame == 28:
                    frame = 0  # resetting the gif once it reaches the end

            changeSpriteImage(Shot_selection_gif, frame)

            score_counters(head_to_head_player_1_counters, head_to_head_player_2_counters)
            penalty_tracker_box(head_to_head_player_1_counters, head_to_head_player_2_counters)
            outcome_calculator(head_to_head_player_1_counters, head_to_head_player_2_counters)


            return_to_menu_button.draw(background, (0, 0, 0))

            print(head_to_head_player_1_counters.goal_tracker)
            print('')
            print(head_to_head_player_2_counters.goal_tracker)
            print(head_to_head_player_2_counters.gif_table)
            #print(head_to_head_player_2_counters.
            print('')
            print(Counter.sudden_death)

            if head_to_head_player_2_counters.player_game_count == 5:
                Counter.sudden_death_initiate()
                print('sudden death started within head to head')
                sudden_death_loop()

            game_type_label = header_font.render('Head to Head', True, blue)
            gameDisplay.blit(game_type_label, (282, 3))

########################################################################################################################

def sudden_death_loop():
    # background_music = mixer.music.load('champions_league_anthem.mp3')
    # mixer.music.play(-1) #runs music in a loop]

    click = False
    return_to_menu_button = button(green, 29, 697, 250, 100, 'Return to menu')

    if head_to_head_player_1_counters.head_to_head_game_count % 2 == 0:  # if game count is odd
        selected_player_counter = head_to_head_player_1_counters
        selected_player_choice = head_to_head_player_1_choice
        player_1_turn = True
    else:
        selected_player_counter = head_to_head_player_2_counters
        selected_player_choice = head_to_head_player_2_choice
        player_1_turn = False

    while Counter.head_to_head_game_count <= 15:

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
                    if return_to_menu_button.isOver(mouse):
                        select_menu()
                if event.type == MOUSEMOTION:
                    if return_to_menu_button.isOver(mouse):
                        return_to_menu_button.color = (red)
                    else:
                        return_to_menu_button.color = (green)

                mouse = pygame.mouse.get_pos()  # mouse needs to be in the for event, otherwise it doesn't live update
                # print(mouse)

                if 355 + 10 > mouse[0] > 355 and 301 + 10 > mouse[1] > 301:  # bottom left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[0]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)

                elif 349 + 10 > mouse[0] > 349 and 275 + 10 > mouse[
                    1] > 275:  # top left setting up code to determine whether the mouse position is within the shooting box, #top left
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[1]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)



                elif 395 + 10 > mouse[0] > 395 and 300 + 10 > mouse[1] > 300:  # bottom middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[2]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)


                elif 396 + 10 > mouse[0] > 396 and 279 + 10 > mouse[1] > 279:  # top middle
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[3]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)


                elif 442 + 10 > mouse[0] > 442 and 302 + 10 > mouse[1] > 302:  # bottom right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[4]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)


                elif 442 + 10 > mouse[0] > 442 and 282 + 10 > mouse[1] > 282:  # top right
                    if event.type == MOUSEBUTTONDOWN:
                        if click:
                            mixer.music.stop()
                            selected_player_choice = areas[5]
                            if player_1_turn == True:
                                game_logic(selected_player_counter, None, selected_player_choice)
                            elif player_1_turn == False:
                                game_logic(selected_player_counter, None, None, selected_player_choice)

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

            if clock() > nextFrame:  # this is constantly looking at the clock and is seeing if enough time has passed to play the next frame
                frame = (frame + 1)  # keep increasing the frame by one
                nextFrame += 30  # this controls the speed of the gif
                if frame == 28:
                    frame = 0  # resetting the gif once it reaches the end
            changeSpriteImage(Shot_selection_gif, frame)

            score_counters(head_to_head_player_1_counters, head_to_head_player_2_counters)
            penalty_tracker_box(head_to_head_player_1_counters, head_to_head_player_2_counters)
            outcome_calculator(head_to_head_player_1_counters, head_to_head_player_2_counters)

            return_to_menu_button.draw(background, (0, 0, 0))

            print(Counter.sudden_death)
            print(head_to_head_player_2_counters.goal_tracker)

            game_type_label = header_font.render('Sudden Death', True, blue)
            gameDisplay.blit(game_type_label, (282, 3))

            if Counter.head_to_head_game_count == 10:
                killSprite(Shot_selection_gif) # have to kill sprite in order for last ball to appear in ball 2 outcome box (for some reason?)
                pygame.time.wait(2000)
                head_to_head_player_1_counters.goal_tracker_reset()
                head_to_head_player_2_counters.goal_tracker_reset()
                sudden_death_loop()

########################################################################################################################

########################################### Game type interface ########################################################

def select_menu():

    select_menu_x_coord = 800
    select_menu_y_coord = 800

    head_to_head_player_1_counters.reset('player_1')
    head_to_head_player_2_counters.reset('player_2')

    select_menu = pygame.display.set_mode((select_menu_x_coord,select_menu_y_coord))
    select_menu.fill(white)

    def redraw_select_menu():
        select_menu.fill(white)
        single_player_button.draw(select_menu, (0,0,0))
        head_to_head_button.draw(select_menu, (0,0,0))

    run = True
    single_player_button = button(green, select_menu_x_coord/8, select_menu_y_coord * 0.75, 250, 100, 'Single Player')
    head_to_head_button = button(blue, select_menu_x_coord/4, select_menu_y_coord * 0.5, 250, 100, 'Head to Head')
    while run:
        redraw_select_menu()
        pygame.display.update()
        for event in pygame.event.get():

            mouse = pygame.mouse.get_pos()
            print(mouse)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if single_player_button.isOver(mouse):
                    print('single player game started')
                    single_player_loop()
                elif head_to_head_button.isOver(mouse):
                    print('head to head game started')
                    head_to_head_loop()

            if event.type == pygame.MOUSEMOTION:
                if single_player_button.isOver(mouse):
                    single_player_button.color = (red)
                else:
                    single_player_button.color = (green)

                if head_to_head_button.isOver(mouse):
                    head_to_head_button.color = (violet)
                else:
                    head_to_head_button.color = (blue)

            if event.type == pygame.QUIT:  # this allow the user to quit, pygame.QUIT is a pygame function (hitting the x in the top left)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # This gets any event that is happening on the screen, where is the mouse clicking, keys presses EVERYTHING
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

select_menu()