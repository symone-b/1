# Symone Bennett
# rock-paper-scissors.py
# 9/17/22
# CISW 24

# Water, Fire, Air.

import random, time, sys

print('Water, Fire, Air. How it works: Water beats Fire, Fire beats Air, and Air beats Water')

# variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:
    while True:
        print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
        print('Enter your move: (W)ater (F)ire (A)ir or (Q)uit')
        playerMove = input('> ').upper()
        if playerMove == 'Q':
            print('Thanks for playing')
            sys.exit()

        if playerMove == 'W' or playerMove == 'F' or playerMove == 'A':
            break
        else:
            print('Type one of R, P, S, or Q.')


    if playerMove == 'W':
        print('WATER versus...')
        playerMove = 'WATER'
    elif playerMove == 'F':
        print('FIRE versus...')
        playerMove = 'FIRE'
    elif playerMove == 'A':
        print('AIR versus...')
        playerMove = 'AIR'

    # Count to three with dramatic pauses:
    time.sleep(0.5)
    print('1...')
    time.sleep(0.25)
    print('2...')
    time.sleep(0.25)
    print('3...')
    time.sleep(0.25)

    # Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'WATER'
    elif randomNumber == 2:
        computerMove = 'FIRE'
    elif randomNumber == 3:
        computerMove = 'AIR'
    print(computerMove)
    time.sleep(0.5)
          
    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'FIRE' and computerMove == 'AIR':
        print('You Win')
        wins = wins + 1
    elif playerMove == 'WATER' and computerMove == 'FIRE':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'AIR' and computerMove == 'WATER':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'FIRE' and computerMove == 'WATER':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'WATER' and computerMove == 'AIR':
        print('You lose')
        losses = losses + 1
    elif playerMove == 'AIR' and computerMove == 'FIRE':
        print('You lose!')
        losses = losses + 1
      
