# Symone Bennett
# assignment6.py
# 9/27/22
# CISW24

import sys

lets_play = input('Would you like to play a game? (y/n/q): ')
if lets_play == 'n':
    print('Thank you for playing. Good bye.')
    sys.exit()

game_choice = input('''
Choose a game or quit:
1) Bagles
2) Rock, Paper, Scissors
3) The Game 21
q) to quit

Enter your choice: ''')

while game_choice:
    if game_choice.lower() == 'q':
        print('Thank you for playing. Good bye.')
        sys.exit()
    if game_choice == '1':
        print('You chose bagles! Have a nice game.')
        break
    elif game_choice == '2':
        print('You chose rock, paper, scissors! Have a nice game.')
        break
    elif game_choice == '3':
        print('You chose the game 21! Have a nice game!')
        # 
    else:
        play_again = input('Would you like to play another game?(y/n/q):')
    while play_again != 'y' and play_again != 'n' and play_again != 'q':
        play_again = input('Oops! Please choose 1,2,3, or q.')

    
    
    


    
           




    
    
        
