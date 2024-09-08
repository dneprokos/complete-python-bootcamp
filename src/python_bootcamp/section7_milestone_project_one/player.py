# Contains the logic related to the players, including player input, switching turns, and validating moves.

class Player:
    def __init__(self, name, symbol):
        """
        Initialize a new player.

        :param name: The name of the player.
        :param symbol: The symbol for the player ('X' or 'O').
        """
        self.name = name
        self.symbol = symbol

    def __str__(self):
        """
        Return a string representation of the player.
        """
        return f"Player {self.name} ({self.symbol})"