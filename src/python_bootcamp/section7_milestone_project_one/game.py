# Contains the core game logic, including checking for a winner, handling player moves, and managing the game board.
from board import Board

class TicTacToe:
    def __init__(self, player, player2):
        """
        Initialize a new game of Tic-Tac-Toe.

        :param player: The first player.
        :param player2: The second player.
        """
        self.player = player
        self.player2 = player2
        self.board = Board()
        self.current_player = player
        self.is_game_over = False


    def play(self):
        """
        Start the main game loop.
        """
        while self.is_game_over == False:
            self.board.display()
            self.handle_turn()

            if self.check_winner() or self.check_tie():
                break
            self.switch_players()

    def handle_turn(self):
        """
        Handle a player's turn.
        """
        print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")
        is_valid_path = False

        input_row = int(input("Enter row (0-2): "))
        input_col = int(input("Enter column (0-2): "))

        # TODO: Check if the input is valid

        self.board.place_marker(input_row, input_col, self.current_player.symbol)

    def check_winner(self):
        """
        Check if a player has won the game.
        """
        # Check rows
        for row in self.board.board:
            if row[0] == row[1] == row[2] == self.current_player.symbol:
                self.board.display()
                print(f"{self.current_player.name} wins!")
                self.is_game_over = True
                return True

        # Check columns
        for col in range(3):
            if self.board.board[0][col] == self.board.board[1][col] == self.board.board[2][col] == self.current_player.symbol:
                self.board.display()
                print(f"{self.current_player.name} wins!")
                self.is_game_over = True
                return True

        # Check diagonals
        if self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] == self.current_player.symbol:
            self.board.display()
            print(f"{self.current_player.name} wins!")
            self.is_game_over = True
            return True
        if self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0] == self.current_player.symbol:
            self.board.display()
            print(f"{self.current_player.name} wins!")
            self.is_game_over = True
            return True

        return False
    
    def check_tie(self):
        """
        Check if the game is a tie.
        """
        if all([cell != ' ' for row in self.board.board for cell in row]):
            self.board.display()
            print("It's a tie!")
            self.is_game_over = True
            return True

        return False
    
    def switch_players(self):
        """
        Switch to the other player.
        """
        if self.current_player == self.player:
            self.current_player = self.player2
        else:
            self.current_player = self.player

    def validate_input(self, row, col):
        """
        Validate the input row and column.
        """
        pass
        