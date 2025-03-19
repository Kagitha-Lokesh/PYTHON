player_1 = input('Player 1 : ')
player_2 = input('player 2 : ')
game = ['rock','paper','scissor']
if(player_1 and player_2 in game):
    if(player_1==player_2):
        print('Tie')
    elif(player_1=='rock' and player_2 == 'paper'):
        print('player 2 wins')
    elif(player_1=='rock' and player_2 == 'scissor'):
        print('player 1 wins')
    elif(player_1=='paper' and player_2 == 'rock'):
        print('player 1 wins')
    elif(player_1=='paper' and player_2 == 'scissor'):
        print('player 2 wins')
    elif(player_1=='scissor' and player_2 == 'paper'):
        print('player 1 wins')
    elif(player_1=='scissor' and player_2 == 'rock'):
        print('player 2 wins')
else:
    print('Give only valid input')