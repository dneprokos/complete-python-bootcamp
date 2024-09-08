# The entry point for your game. This file will handle starting the game, displaying the menu, and calling other functions as needed.

from player import Player
from game import TicTacToe

def main():
    print("Welcome to Tic-Tac-Toe!")

    # Create players
    player1_name = input("Enter the name of Player 1 (X): ")
    player2_name = input("Enter the name of Player 2 (O): ")

    player1 = Player(player1_name, 'X')
    player2 = Player(player2_name, 'O')

    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")
    
    # Create game instance
    game = TicTacToe(player1, player2)
    
    # Start the game loop
    game.play()
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()