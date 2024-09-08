#Handles the representation and display of the game board.
from tabulate import tabulate

class Board:
    def __init__(self):
        """
        Initialize a new 3x3 Tic-Tac-Toe board.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        """
        Display the board in a nice grid format.
        """
        print(tabulate(self.board, tablefmt="grid"))

    def place_marker(self, row, col, marker):
        """
        Place a marker on the board at the given row and column.

        :param row: The row to place the marker.
        :param col: The column to place the marker.
        :param marker: The marker to place ('X' or 'O').
        """
        self.board[row][col] = marker    
    
    def reset(self):
        """
        Reset the board to its initial empty state.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]




    