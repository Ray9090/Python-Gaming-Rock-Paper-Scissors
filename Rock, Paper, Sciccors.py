from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
player1 = t[randint(0,2)]

#set player to False
player2 = False

while player2 == False:
#set player to True
    player2 = input("Rock, Paper, Scissors?")
    if player2 == player1:
        print("Tie!")
    elif player2 == "Rock":
        if player1 == "Paper":
            print("You lose!", player1, "covers", player2)
        else:
            print("You win!", player2, "smashes", player1)
    elif player2 == "Paper":
        if player1 == "Scissors":
            print("You lose!", player1, "cut", player2)
        else:
            print("You win!", player2, "covers", player1)
    elif player2 == "Scissors":
        if player1 == "Rock":
            print("You lose...", player1, "smashes", player2)
        else:
            print("You win!", player2, "cut", player1)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player2 = False
    player1 = t[randint(0,2)]