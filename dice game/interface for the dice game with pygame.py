import pygame
from pygame.locals import *
import time, random
from sys import exit
from signin import signin
'''import signin
from signin import signin
'''
pygame.init()
pygame.font.init()

dice_1 = [
    (0, 0, 0),
    (0, 1, 0),
    (0, 0, 0)
    ]
dice_2 = [
    (0, 0, 1),
    (0, 0, 0),
    (1, 0, 0)
    ]
dice_3 = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0)
    ]
dice_4 = [
    (1, 0, 1),
    (0, 0, 0),
    (1, 0, 1)
    ]
dice_5 = [
    (1, 0, 1),
    (0, 1, 0),
    (1, 0, 1)
    ]
dice_6 = [
    (1, 0, 1),
    (1, 0, 1),
    (1, 0, 1)
    ]

def message(text, centerx, centery, size = 1):
    font = 'optima'
    if size == 1:
        myfont = pygame.font.SysFont(font, 30)
    elif size == 2:
        myfont = pygame.font.SysFont(font, 15)
    elif size == 3:
        myfont = pygame.font.SysFont(font, 10)
    elif size == 4:
        myfont = pygame.font.SysFont(font, 50) 
    else:
        myfont = pygame.font.SysFont(font, 15)
    ts = myfont.render(text, True, black)
    tsR = ts.get_rect(center=(centerx, centery))
    display.blit(ts, tsR)
   
dis_width = 800
dis_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
blue = (50, 253, 213)
 
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Dice game')
clock = pygame.time.Clock()

def doubleRound(player1, name1):
    time.sleep(2)
    def draw_dice(dice, display):
        cx, cy = (int(dis_width/2),int(dis_height/2))
        points = [[cx-60, cy-60],
                  [cx, cy-60],
                  [cx+60, cy-60],
                  [cx-60, cy],
                  [cx, cy],
                  [cx+60, cy],
                  [cx-60, cy+60],
                  [cx, cy+60],
                  [cx+60, cy+60]]
        for i in range(0, 9):
            if dice[int(i/3)][i%3] == 1:
                circle = pygame.draw.circle(display, black, (points[i][0], points[i][1]), 20)
        
    def animation(display):
        global dice_1, dice_2, dice_3, dice_4, dice_5, dice_6
        choice1 = random.randint(0, 5)
        choices = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]
        draw_dice(choices[choice1], display)

    rect = pygame.draw.rect(display, white, (300, 200, 200, 200), 0, 20)
    dice1,dice2,dice3,dice4,dice5,dice6 = 1, 2, 3, 4, 5, 6
    player = player1
    name = name1
    game_over = False
    newdice = dice_1
    animation_num = 0
    accdice = 0
    displayNum = 1
    ending = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(pygame.mouse.get_pos()) and animation_num == -1 and ending == False:
                    accdice = 0
                    num1 = random.randint(0, 5)
                    list1 = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]
                    list2 = [dice1, dice2, dice3, dice4, dice5, dice6]
                    newdice = list1[num1]
                    accdice = list2[num1]
                    animation_num = 6
                    displayNum = 10
                    ending = True
        
        ''' Initial display
            - displays players and their scores
            - updated after each player has rolled and each round has finished
            - also drawing the dice rectangles
        '''
        if displayNum >= 1:
            display.fill(blue)
            message("EXTRA ROUND", 400, 40, 4)
            message("You rolled a double so you get to roll the dice again!", 400, 100)
            rect = pygame.draw.rect(display, white, (300, 200, 200, 200), 0, 20)
            if ending == True:
                displayNum -= 1

            if animation_num > 0:
                animation_num -= 1
                animation(display)
            else:
                animation_num = -1
                draw_dice(newdice, display)
                
        else:
            display.fill(blue)
            message("You rolled a,", 400, 150, 4)
            message("{}".format(int(accdice)), 400, 275, 4)
            message("You gain +{} score".format(str(accdice)), 400, 400, 4)
            game_over = True
            pygame.display.update()
            time.sleep(3)
            
        pygame.display.update()
        clock.tick(7)
    return accdice

def gameLoop():
    def draw_dice(dice, dice2, display, double = False):
        cx, cy = (int(dis_width/2),int(dis_height/2))
        points = [[cx-60, cy-60],
                  [cx, cy-60],
                  [cx+60, cy-60],
                  [cx-60, cy],
                  [cx, cy],
                  [cx+60, cy],
                  [cx-60, cy+60],
                  [cx, cy+60],
                  [cx+60, cy+60]]
        for i in range(0, 9):
            if dice[int(i/3)][i%3] == 1:
                circle = pygame.draw.circle(display, black, (points[i][0]-150, points[i][1]), 20)
        for i in range(0, 9):
            if dice2[int(i/3)][i%3] == 1:
                circle = pygame.draw.circle(display, black, (points[i][0]+150, points[i][1]), 20)
       
    def animation(display):
        global dice_1, dice_2, dice_3, dice_4, dice_5, dice_6, diceblitted
        choice1 = random.randint(0, 5)
        choice2 = random.randint(0, 5)
        choices = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]
        draw_dice(choices[choice1], choices[choice2], display)
        
    def score(diceRolled):
        score = diceRolled
        if diceRolled %2 == 0:
            score += 10
        else:
            score -= 5
        return score

    minusOrPlus = ''
    p1score = 0
    p2score = 0
    accdice = 0
    dice1,dice2,dice3,dice4,dice5,dice6 = 1, 2, 3, 4, 5, 6
    player = ""
    name = ""
    game_over = False
    newdice = dice_1
    newdice2 = dice_1
    animation_num = 0
    counter = 0
    finished = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (rect.collidepoint(pygame.mouse.get_pos()) or rect2.collidepoint(pygame.mouse.get_pos())) and animation_num == -1:
                    accdice = 0
                    num1 = random.randint(0, 5)
                    num2 = random.randint(0, 5)
                    list1 = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]
                    list2 = [dice1, dice2, dice3, dice4, dice5, dice6]
                    newdice = list1[num1]
                    newdice2 = list1[num2]
                    accdice += list2[num1] + list2[num2]
                    animation_num = 6
                    if num1 == num2:
                        if player == "1":
                            p1score += doubleRound(player, name)
                        else:
                            p2score += doubleRound(player, name)
                        counter += 1
                        if player == "1":
                            player = "2"
                            name = "Jeff"
                        else:
                            player = "1"
                            name = "Will"
                        while num1 != num2:
                            num1 = random.randint(0, 5)
                            num2 = random.randint(0, 5)
                        newdice = list1[num1]
                        newdice2 = list1[num2]
                        accdice += list2[num1] + list2[num2]
                    if player == "1":
                        player = "2"
                        name = "Jeff"
                    else:
                        player = "1"
                        name = "Will"
                    if counter != 0: counter += 1
                    else: counter += 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    finished = False
                    minusOrPlus = ''
                    p1score = 0
                    p2score = 0
                    accdice = 0
                    dice1,dice2,dice3,dice4,dice5,dice6 = 1, 2, 3, 4, 5, 6
                    player = ""
                    name = ""
                    game_over = False
                    newdice = dice_1
                    newdice2 = dice_1
                    animation_num = 0
                    counter = 0
                    finished = False
                elif event.key == pygame.K_q:
                    game_over = True

        ''' Initial display
            - displays players and their scores
            - updated after each player has rolled and each round has finished
            - also drawing the dice rectangles
        '''
                  
        display.fill(blue)
        message("Round {}".format(int(counter/2)), 400, 40)
        message("Will's Score:", 125, 50)
        message("{}".format(p1score), 125, 100)
        message("Jeff's Score:", 675, 50)
        message("{}".format(p2score), 675, 100)
        rect = pygame.draw.rect(display, white, (150, 200, 200, 200), 0, 20)
        rect2 = pygame.draw.rect(display, white, (450, 200, 200, 200), 0, 20)

        ''' This if loop animartes the dice
            - it uses a variable which is set to 6 when the dice is clicked
            - whilst the variable is greater than one, every frame 1 is taken away from the variable
            - when the variable is 0, the actual rolled dice is displayed
        ''' 
        if animation_num > 0:
            animation_num -= 1
            animation(display)
        else:
            animation_num = -1
            draw_dice(newdice, newdice2, display)
            
        ''' This add the score gained in the current round
            - if the total is less than 0, the score is set to 0
            - also checks for the current player
        '''
        if animation_num == 0:
            if player == "1" and p1score + score(accdice) >= 0:
                p1score += score(accdice)
            elif player == "1":
                p1score = 0
            if player == "2" and p2score + score(accdice) >= 0:
                p2score += score(accdice)
            elif player == "2":
                p2score = 0
                
        ''' Just for displaying a minus or a plus on the screen
        '''
        if (score(accdice)-accdice) == 10:
            minusOrPlus = '+'
        else:
            minusOrPlus = ''

        ''' This is the versatile display 
        '''
        if animation_num == -1:
            if name != "": 
                message(('{} rolled a total of {}'.format(name, accdice)), 400, 450)
                message(('{}{} score'.format(minusOrPlus, score(accdice)-accdice)), 400, 530)
                message(('{}{} score'.format("+", accdice)), 400, 490)
                if name == "Will": name = "Jeff"
                elif name == "Jeff": name = "Will"
                message("{}'s turn".format(name), 400, 75)
                if name == "Will": name = "Jeff"
                elif name == "Jeff": name = "Will"

        ''' Checks if it is the last round and if it is
            - finished will be set to True and final scores will be tallied
            - 
        '''
        if counter == 11 and animation_num == -1:
            finished = True
            finalp1score = p1score
            finalp2score = p2score
        if finished == True:
            display.fill(blue)
            message('WELL DONE', 400, 200)
            message(('Player 1 got a score of: {}'.format(finalp1score)), 400, 250)
            message(('Player 2 got a score of: {}'.format(finalp2score)), 400, 300)
            if finalp1score > finalp2score:
                message('PLAYER 1 WINS', 400, 375)
            elif finalp2score > finalp1score:
                message('PLAYER 2 WINS', 400, 375)
            else:
                message('DRAW!', 400, 375)
            message('Press p to play again or q to quit', 400, 450, 2)
        pygame.display.update()

        clock.tick(7)
    pygame.quit()
    quit()

def instructions():
    stop = True
    while stop == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    stop = False
                    gameLoop()

                    
        display.fill(white)
        message('Instructions', 400, 65)
        message('1. Each player takes it in turns to roll 2 dice', 400, 125, 2)
        message('2. If an even number is rolled, you gain an additional 10 points', 400, 175, 2)
        message('3. If an odd number is rolled, you lose 5 points', 400, 225, 2)
        message('4. If a double is rolled, another dice is rolled to determine the points gained', 400, 275, 2)
        message('5. There are 5 rounds and the player with the most score at the end wins', 400, 325, 2)
        message('6. There is a leaderboard with the top 5 scores of all time', 400, 375, 2)
        message('Press S to start', 400, 450)
        
        clock.tick(10)
        pygame.display.update()

stillrunning = True
signin()
instructions()
while stillrunning == True:
    doubleRound()
    gameLoop()
