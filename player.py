import random as rd

class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def select_column(self, board):
        pass

class HumanPlayer(Player):
    def select_column(self, board):
        valid = False
        while not valid:
            try:
                col = int(input("col: "))
                if not board.check_if_valid(col):
                    raise ValueError
                valid = True
            except ValueError:
                print("Invalid value")
        return col

class RandomComputerPlayer(Player):
    def select_column(self, board):
        valid = False
        while not valid:
            col = rd.randint(0, board.cols)
            valid = board.check_if_valid(col)
        return col