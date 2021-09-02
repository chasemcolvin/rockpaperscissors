#basic rock paper scissors game

import random
user_selection = input('Enter a choice - (rock, paper, scissors):')
choices_allowed = ['rock','paper','scissors']
computer_selection = random.choice(choices_allowed)

print(f'\nYou chose {user_selection}, the computer chose {computer_selection}.\n')

if user_selection == computer_selection:
    print(f'Both players have selected {user_selection}. Its a tie!')
elif user_selection == 'rock':
    if computer_selection == 'scissors':
        print('Rock smashes scissors, you win!')
    else:
        print('Paper covers rock, you lose! Better luck next time!')
elif user_selection == 'scissors':
    if computer_selection == 'paper':
        print('Scissors cut paper, you win!')
    else:
        print('Rock smashes scissors, you lose! Better luck next time!')
elif user_selection == 'paper':
    if computer_selection == 'rock':
        print('Paper covers rock, you win!')
    else:
        print('Scissors cut paper, you lose! Better luck next time!')
