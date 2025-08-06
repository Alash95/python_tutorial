import random 

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

EMOJIS = {ROCK: '🪨', PAPER: '📃', SCISSORS: '✂️'}
CHOICES = tuple(EMOJIS.keys())
CONTINUE_CHOICES = ['y', 'n']

def get_valid_input(prompt, valid_options):
    while True:
        choice = input(prompt).lower()
        # player_choice = input(f"Player {player_number} Rock, Paper, or Scissors? (r/p/s): ").lower()
        if choice in valid_options:
            return choice
        print('😡Invalid choice! Try again')

def determine_winner(player, opponent):
    if player == opponent:
        return 'tie'
    elif (
        (player == ROCK and opponent == SCISSORS) or
        (player == SCISSORS and opponent == PAPER) or
        (player == PAPER and opponent == ROCK)):
        return 'win'
    return 'lose'

def print_choices(player_label, player_choice, opponent_label, opponent_choice):
    print(f'{player_label} chose {EMOJIS[player_choice]}')
    print(f'{opponent_label} chose {EMOJIS[opponent_choice]}')

def play_round(player1_label='You', player2_label='Computer', is_two_player=False, player_number=1):
    player1 = get_valid_input(f'{player1_label} - Rock, Paper, or Scissors? (r/p/s): ', CHOICES)

    if is_two_player:
        print("\n" * 50)
        player2 = get_valid_input(f'{player2_label} - Rock, Paper, or Scissors? (r/p/s): ', CHOICES)
    else:
        player2 = random.choice(CHOICES)

    print_choices(player1_label, player1, player2_label, player2)

    result = determine_winner(player1, player2)
    if result == 'tie':
        print("🤝 It's a tie")
    elif result == 'win':
        print(f"🎉 {player1_label} wins!")
    else:
        print(f'🎉 {player2_label} wins!')
    return result

def play_single_player():
    stats = {'wins': 0, 'losses': 0, 'ties': 0}
    
    while True:
        result = play_round()
        if result == 'win':
            stats['wins'] += 1
        elif result == 'lose':
            stats['losses'] += 1
        else:
            stats['ties'] += 1

        continue_game = get_valid_input('Continue? (y/n): ', CONTINUE_CHOICES)
        if continue_game == 'n':
            print('\n📊 Final Stats:')
            print(f'Wins: {stats["wins"]} | Losses: {stats["losses"]} | Ties: {stats["ties"]}')
            break

def play_best_of_three():
    user_score = 0
    computer_score = 0

    while user_score < 2 and computer_score < 2:
        result = play_round()
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        print(f'Score → You: {user_score}, Computer: {computer_score}\n')

    if user_score == 2:
        print('🏆 You are the overall winner!')
    else:
        print('🤖 Computer wins the game!')

def play_two_player():
    while True:
        result = play_round(player1_label='Player 1', player2_label='Player 2', is_two_player=True)

        again = get_valid_input('Play again? (y/n): ', CONTINUE_CHOICES)
        if again != 'y':
            break

def play_game():
    print('🎮 Welcome to Rock, Paper, Scissors!')
    while True:
        print('\nChoose a mode:')
        print('1. Single Player')
        print('2. Best of 3 vs Computer')
        print('3. Two Player')
        print('4. Quit')

        mode = get_valid_input('Enter choice (1-4): ', ['1', '2', '3', '4'])

        if mode == '1':
            play_single_player()
        elif mode == '2':
            play_best_of_three()
        elif mode == '3':
            play_two_player()
        elif mode == '4':
            print('👋 Thanks for playing!')
            break

play_game()