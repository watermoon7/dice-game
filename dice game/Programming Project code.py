import random
import a
from a import display, topscores

def signin(user1, user1password, user2, user2password): #defining the procedure with correct parameters
    signedin1 = False                                   #changing the signed in variables to false
    signedin2 = False
    temptryuser = ""                                    #creating a variable for temporary user name entries
    temptrypass = ""
    while signedin1 == False or signedin2 == False:     #starts the while loop to ensure both players are eventually signed in
        tempuser = input("Username: ")                  #asks the user to input their username
        if tempuser == user1:                           #checks is the username is correct
            temppass = input("Password: ")              #asks the user to input their password
            if temppass == user1password:               #if both are correct, then user1 is signed in
                signedin1 = True
                print("... Signed in")
        elif tempuser == user2:                         #repeats the process for user 2
            temppass = input("Password: ")
            if temppass == user2password:
                signedin2 = True
                print("... Signed in")

def instructions():
    print("--- Instructions ---")
    print("1. Each player takes it in turns to roll 2 dice")
    print("2. If the score rolled by the dice is even then you gain 10 points")
    print("3. If the score rolled by the dice is odd then you lose 5 points")
    print("4. After 5 rounds scores are added up and the winner is announced")
    print("5. If your score is high enough to be in the top 5 you get on the leaderboards")


def diceroll():                     #defines the dice roll
    global dice1                    #takes variables from global so that they can be edited permenantly
    global dice2
    dice1 = random.randint(1, 6)    #rolls a random number from 1 - 6 for dice1
    dice2 = random.randint(1, 6)    #rolls a random number from 1 - 6 for dice2

def score(x):                                   #defining the score function
    scoreround = 0                              #defining the score gained in this round
    if (x % 2) == 0:                            #calculations using DIV function - if the score is even
        scoreround = 10
        print("Even + 10 score")
    elif (x % 2) == 1:                          #calculations using DIV function - if the score is odd
        scoreround = -5
        print(" O D D  -5 score")
    return scoreround                           # returning the score gained in the round


user1score = 0                  #defining total scores
user2score = 0
dice1 = 0                       #defining the die
dice2 = 0
user1 = "william"               #usernames and passwords(more can be added)
user1password = "playsroblox"
user2 = "freddo"
user2password = "m"

#signin(user1, user1password, user2, user2password)  # calling the sign in function

q1 = input("Would you like to see the top scores?(y/n)")
if q1 == "y":
    display()
q2 = input("Would you like to see the instructions?(y/n)")
if q2 == "y":
    instructions()

for i in range(1, 6):                                       #beggining the main sequence of the game by setting a loop that will repeat 5 times for each round
    print("")
    print("-==- R O U N D : {} -==-".format(i))             #printing the round
    for o in range(1, 3):                                   #each player will have a turn in each round and there are 2 players hence the twice repeating loop
        if o == 1:                                          #obtaining the player playing the round
            a = user1
        else:
            a = user2
        print("")
        print("-==-==-==-==-==-==-==-==-==-")
        print("{}'s turn to roll".format(a))                #announcing the player whose turn it is
        input("Press enter to roll")
        print("")
        diceroll()                                          #rolling the dice
        print("You rolled: {} and {}".format(dice1, dice2)) #showing the user their dice that they rolled
        print("-==-==-==-==-==-==-==-==-==-")
        print("")
        if a == user1:                                                      #bonus round
            if dice1 == dice2:                                              #checking that both dice are the same
                diceroll()                                                  #rolling another dice
                print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟")
                print("BONUS ROUND FOR ROLLING A DOUBLE")                   #fancy text
                print(" You get to roll 1 extra dice!! ")
                print("         YOU ROLLED: {}         ".format(dice1) )    #the score you got
                print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟")
                user1score = user1score + dice1                             #adding the score onto your total score
            else:
                user1score = user1score + dice1 + dice2                     #calculating total score after the round
                user1score = user1score + score(user1score)
            if user1score < 0:                                              #making sure the score doesn't go below 0
                user1score = 0
            print("")
            print("Your TOTAL score is: ", user1score)
        else:                                                               #repeating the previous steps but for user2 instead
            if dice1 == dice2:
                diceroll()
                print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟")
                print("BONUS ROUND FOR ROLLING A DOUBLE")
                print(" You get to roll 1 extra dice!! ")
                print("         YOU ROLLED: {}         ".format(dice1))
                print("⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟⍟")
                user2score = user2score + dice1
            else:
                user2score = user2score + dice1 + dice2
                user2score = user2score + score(user2score)
            if user2score < 0:
                user2score = 0
            print("")
            print("Your TOTAL score is: ", user2score)
        if i == 5 and o == 2:
            print("")
            print(" --- FINAL SCORES --- ")                             #if it is the final round and both users have had their turn then
            print("{}'s total score is : {}".format(user1, user1score)) #printing both final total scores
            print("")
            print("{}'s total score is : {}".format(user2, user2score))
            print("")
            topscores(user1, user1score)
            topscores(user2, user2score)
            display()
            if user1score == user2score:                                #if the scores are the same then
                dice1 = 0                                               #sets both dice to 0 so they are the same
                dice2 = 0
                while dice1 == dice2:                                   #both users will roll another dice until one rolles a larger number
                    print("OH NO ITS A DRAW - BETTER ROLL ANOTHER DICE")
                    dice1 = random.randint(1, 6)
                    input("Press enter {}: ".format(user1))
                    print(dice1)
                    dice2 = random.randint(1, 6)
                    input("Press enter {}: ".format(user2))
                    print(dice2)
                    if dice1 > dice2:
                        print("★★★★★", user1, "wins! ★★★★★")    #depending on the dice roll, either user1 or user2 will win
                    else:
                        print("★★★★★", user2, "wins! ★★★★★")
            if user1score > user2score:
                print("★★★★★", user1, "wins! ★★★★★")            #if the dice roll hasn't gone ahead, then the winner will also be printed
            elif user1score < user2score:
                print("★★★★★", user2, "wins! ★★★★★")
