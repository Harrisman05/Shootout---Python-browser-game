import random
import pyinputplus as pyip

game_count = 0
post_count = 0
crossbar_count = 0
goal_count = 0
save_count = 0
miss_count = 0
#             0              1             2                3             4             5         6        7           8
areas = ('bottom left', 'top left', 'bottom middle', 'top middle', 'bottom right', 'top right', 'post', 'crossbar', 'miss')

player_history = []  # GOALIE GUESSING TECHNOLOGY

while game_count < 20:

    game_count += 1

    player_choice = pyip.inputChoice(areas[0:6]) #Player shot selection

    goalie_choice = random.choices(areas, weights = [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.11, 0.11, 0.06], k=1) #Goalie decision making
    goalie_choice = goalie_choice[0] #converting goalie decision from list data type into a string type

    player_history.append(player_choice) # GOALIE GUESSING TECHNOLOGY
    if len(player_history) > 2: #if the player has had at least 3 shots, the goalie has a chance of predicting the 3rd shot
        while len(player_history) > 3: #this maintains the goalie's memory being 3 shots
            del player_history[0]
        if player_history.count(player_choice) == 3: #if the player guesses 3 shots in a row
            print('SAVE! The keeper taunts you as he easily predicts your shot pattern')
            save_count += 1
            continue # continue allows me to immediately jump back to the start of the while loop game_count < 5

    if goalie_choice == areas[8]: #complete miss
        if player_choice == areas[0]:  # complete miss
            print('MISS! You drag your shot wide of the post!') # missing the left post low - bottom low
            miss_count += 1
        elif player_choice == areas[1]:
            print('MISS! You sky your shot wayward of the post!') # missing the left post high - top left
            miss_count += 1
        elif player_choice == areas[2]:
            print('SAVE! Your shot is easily gathered by the goalie!') # 'missing' bottom low paradox - keeper gathers the shot - bottom low
            save_count += 1
        elif player_choice == areas[3]:
            print('MISS! Your shot is blazed over the crossbar!') # missing over the crossbar - top middle
            miss_count += 1
        elif player_choice == areas[4]:
            print('MISS! Your shot trickles passed the post!') # missing the right post low - bottom right
            miss_count += 1
        elif player_choice == areas[5]:
            print('MISS! Your shot flys high passed the post!') # missing the right post high - top right
            miss_count += 1

    elif goalie_choice == areas[6]: #post
        if player_choice == areas[2]: #bottom middle and post paradox
            print('SAVE! The keeper began to dive but managed a save with his trailing leg!')
            save_count += 1
        elif player_choice == areas[3]: #top middle and post paradox
            print('SAVE! The keeper managed to claw the ball away with a finger-tip save!')
            save_count += 1
        elif player_choice == areas[0]: # hitting the bottom left post
            print('POST! The shot rifles towards the left but thunders off the post!')
            post_count += 1
        elif player_choice == areas[1]: #hitting the top left post
            print('POST! The shot looks destined for the top left corner but canons off the post!')
            post_count += 1
        elif player_choice == areas[4]: #hitting the bottom right post
            print('POST! The daisy cutter of a shot looks promising but rockets off the bottom of the post!')
            post_count += 1
        elif player_choice == areas[5]: #hitting the top right post
            print('POST! The keeper is motionless as he watches the ball ricochet off the post!')
            post_count += 1

    elif goalie_choice == areas[7]: #crossbar
        if player_choice == areas[0]:
            print('SAVE! The keeper manages to drop low and tip the ball around the left post!') #bottom left and post paradox
            save_count += 1
        elif player_choice == areas[2]: #bottom middle and crossbar paradox
            print('SAVE! The keeper stays rooted to the spot and denys the ball an introduction to the net!')
            save_count += 1
        elif player_choice == areas[4]: #bottom right and crossbar paradox
            print('SAVE! The keeper gets a fingertip on the ball and nudges it around the post!')
            save_count += 1
        elif player_choice == areas[1]: #hitting the left part of the crossbar
            print('CROSSBAR! The ball flys high and to the left but clips the crossbar and soars into the fans!')
            crossbar_count =+ 1
        elif player_choice == areas[2]: #hitting the middle of the crossbar
            print('CROSSBAR! The ball is smashed down the middle and canons off the crossbar!')
            crossbar_count = + 1
        elif player_choice == areas[5]: #hitting the right part of the crossbar
            print('CROSSBAR! The ball flys high to the right and rattles the top of the crossbar!')
            crossbar_count = + 1

    elif player_choice == areas[0]: #Goalie diving bottom left
        if goalie_choice == areas[0]:
            print('SAVE! The keeper dives low to the left and saves!')
            save_count += 1
        else:
            print('GOAL! You rifle the ball in the left corner and it nestles in the net. Goal!')
            goal_count += 1
    elif player_choice == areas[1]: #Goalie diving top left
        if goalie_choice == areas[1]:
            print('SAVE! The keeper leaps to the left corner and punches the ball clear!')
            save_count += 1
        else:
            print('GOAL! You smash the ball into the top left corner!')
            goal_count += 1
    elif player_choice == areas[2]: #Goalie staying bottom middle
        if goalie_choice == areas[2]:
            print('SAVE! The keeper reads you and blocks the shot coming directly at him!')
            save_count += 1
        else:
            print('GOAL! You double bluff the keeper and dink the ball down the middle!')
            goal_count += 1
    elif player_choice == areas[3]: #Goalie staying top middle
        if goalie_choice == areas[3]:
            print('SAVE! The keeper reads you palms the ball over the top of the crossbar!')
            save_count += 1
        else:
            print('GOAL! You let fly and rocket the ball into the roof of the net!')
            goal_count += 1
    elif player_choice == areas[4]: #Goalie diving bottom right
        if goalie_choice == areas[4]:
            print('SAVE! The keeper pounces to the right and deflects the ball away!')
            save_count += 1
        else:
            print('GOAL! You arrow the ball into the bottom right corner, keeper stood no chance!')
            goal_count += 1
    elif player_choice == areas[5]: #Goalie diving top right
        if goalie_choice == areas[5]:
            print('SAVE! The keeper reaches high and manages to redirect the ball over the crossbar!')
            save_count += 1
        else:
            print('GOAL! You crack the ball into the top right corner of the goal!')
            goal_count += 1

print('You managed to score ' + str(goal_count) + ' time' + '(' + 's' + ').')
print('The keeper managed to save your shots ' + str(save_count) + ' time' + '(' + 's' + ').')
print('You struck the post ' + str(post_count) + ' time' + '(' + 's' + ').')
print('You struck the crossbar ' + str(crossbar_count) + ' time' + '(' + 's' + ').')
print('You completely missed the target ' + str(miss_count) + ' time' + '(' + 's' + ').')




