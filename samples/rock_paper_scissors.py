# Function to get a valid choice from the player
def get_player_choice(player_name):
    """
    Prompts the player to enter their choice of 'rock', 'paper', or 'scissors'.

    Args:
        player_name (str): The name of the player.

    Returns:
        str: The player's choice.

    """
    while True:
        choice = input(f"{player_name}, enter your choice (rock, paper, or scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Please choose from 'rock', 'paper', or 'scissors'.")

# Function to determine the winner
def determine_winner(player1_choice, player2_choice):
    """
    Determines the winner of a rock-paper-scissors game.

    Args:
        player1_choice (str): The choice of player 1 ('rock', 'paper', or 'scissors').
        player2_choice (str): The choice of player 2 ('rock', 'paper', or 'scissors').

    Returns:
        str: The result of the game. Possible values are:
            - "It's a tie!" if both players make the same choice.
            - "Player 1 wins!" if player 1's choice beats player 2's choice.
            - "Player 2 wins!" if player 2's choice beats player 1's choice.
    """
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if player1_choice == player2_choice:
        return "It's a tie!"
    elif winning_combinations[player1_choice] == player2_choice:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Main game logic
def play_rock_paper_scissors():
    """
    Plays a game of rock-paper-scissors between two players.
    """
    player1_choice = get_player_choice("Player 1")
    player2_choice = get_player_choice("Player 2")

    winner = determine_winner(player1_choice, player2_choice)
    print(winner)

# Play the game
play_rock_paper_scissors()





# def rpsWinner(move1, move2):
# # Check all six possible combinations with a winner and return it:
#     if move1 == 'rock' and move2 == 'paper':
#         return 'player two'

#     elif move1 == 'rock' and move2 == 'scissors':
#         return 'player one'
#     elif move1 == 'paper' and move2 == 'scissors':
#         return 'player two'
#     elif move1 == 'paper' and move2 == 'rock':
#         return 'player one'
#     elif move1 == 'scissors' and move2 == 'rock':
#         return 'player two'
#     elif move1 == 'scissors' and move2 == 'paper':
#         return 'player one'
#     # For all other combinations, it is a tie:
#     else:
#         return 'tie'