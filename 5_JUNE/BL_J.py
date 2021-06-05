#difficulty = input("difficulty ( N , H, XH, X)")
import random
import blackJack_art
import time
import os
#random.randint(0, 12)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cls():
   os.system('cls' if os.name=='nt' else 'clear')

print(blackJack_art.logo)
player_play = []
players_score = []
player = 1
players = int(input("Number of players: "))
play = players
for player_score in range(players):
    players_score.append(0)
    player_play.append('y')
cls()


while play != 0:
    print(blackJack_art.logo)
    print(f"Number of active players: {play}/{players}")
    print("-----------------------------------------------")
    print("Scores:")
    for player_r in range(players):
        print(f"Player {player_r + 1}: {players_score[player_r]}")
    print("-----------------------------------------------")
    print(f"player :{player} \n Score: {players_score[player - 1]}")
    if(players_score[player - 1] > 21):
        print(f"player {player} LOST")
        player_play[player - 1] = 'n'
        play -= 1
    if(player_play[player - 1] == 'y'):
        deal_chk = input("Should deal (GO or END): \n").lower()
        if (deal_chk == 'end'):
            player_play[player - 1] = 'n'
            play -= 1
        else:
            deal = cards[random.randint(0, 12)]
            if (deal == 11):
                deal = int(input("Ace Value: 1 or 11 \n"))
                if (deal != 1 or deal != 11):
                    deal = 1
            players_score[player - 1] += deal
            print(f"Deal: {deal}")
            deal = 0
    time.sleep(1)
    player += 1
    if(player > players):
        player = 1
    cls()



highest_score = 0
player_win = 0
for player in range(players):
    if (players_score[player] > highest_score):
        if( players_score[player] > 21):
            pass
        else:
            highest_score = players_score[player]
            player_win = player + 1
if (player_win == 0):
    print(f"No winner")
else:
    print(f"The winner is player {player_win}")
time.sleep(4)
