import random

print('ROCK, PAPER,SCISSORS')
wins = 0
losses = 0
ties = 0

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')
    player_input = input('Enter your move: (r)ock (p)aper, (s)cissors or (q)uit\n')
    player_chose = ''

    if player_input == 'p':
        player_chose = 'PAPER'
    elif player_input == 'r':
        player_chose = 'ROCK'
    elif player_input == 's':
        player_chose = 'SCISSORS'
    elif player_input == 'q':
        break

    computer_input = random.randint(1, 3)
    computer_chose = ''
    if computer_input == 1:
        computer_chose = 'PAPER'
    elif computer_input == 2:
        computer_chose = 'ROCK'
    elif computer_input == 3:
        computer_chose = 'SCISSORS'

    print(f'{player_chose} versus ...')
    print(computer_chose)

    if computer_chose == player_chose:
        print('It is a tie.')
        ties += 1
    elif computer_input == 1 and player_input == 's':
        print('You lose!')
        losses += 1
    elif computer_input == 2 and player_input == 'r':
        print('You lose!')
        losses += 1
    elif computer_input == 3 and player_input == 'p':
        print('You lose!')
        losses += 1
    else:
        print('You win')
        wins += 1
