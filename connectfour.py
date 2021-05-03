from board import Board
from player import Player

class ConnectFour():
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols

    def play(self, first_player, second_player):
        board = Board(self.rows, self.cols, first_player, second_player)
        players = [first_player, second_player]
        turn = 0
        while board.winner() is None and not board.is_full():
            turn += 1
            player = players[(turn - 1) % 2]
            board.print()
            col = player.select_column(board)
            board.insert(col, player)
            print("\n")
        winner = board.winner()
        if winner is not None:
            board.print()
            print(f"Winner is {winner.letter}")
        else:
            board.print()
            print("It is a tie")
    