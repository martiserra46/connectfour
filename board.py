class Board():
    def __init__(self, rows, cols, first_player, second_player):
        self.rows = rows
        self.cols = cols
        self.board = [[None for j in range(cols)] for i in range(rows)]
        self.first_player = first_player
        self.second_player = second_player
    
    def print(self):
        for row in self.board:
            row = [' ' if player is None else player.letter for player in row]
            print('| ' + ' | '.join(row) + ' |')
        
    def check_if_valid(self, col_ind):
        if col_ind < 0 or col_ind >= self.cols:
            return False
        if self.board[0][col_ind] is not None:
            return False
        return True

    def insert(self, col_ind, player):
        if not self.check_if_valid(col_ind):
            return False
        for row_ind in range(self.rows - 1, -1, -1):
            if self.board[row_ind][col_ind] is None:
                self.board[row_ind][col_ind] = player
                break
        return True

    def winner(self):
        if self.is_winner(self.first_player):
            return self.first_player
        if self.is_winner(self.second_player):
            return self.second_player
        return None
    
    def is_winner(self, player):
        #check for rows
        for row_ind in range(self.rows):
            found_in_row = 0
            for col_ind in range(self.cols):
                found_in_row = found_in_row + 1 if self.board[row_ind][col_ind] == player else 0
                if found_in_row == 4:
                    return True
        #check for cols
        for col_ind in range(self.cols):
            found_in_col = 0
            for row_ind in range(self.rows):
                found_in_col = found_in_col + 1 if self.board[row_ind][col_ind] == player else 0
                if found_in_col == 4:
                    return True
        #check for diagonals
        for row_ind in range(self.rows - 3):
            for col_ind in range(self.cols - 3):
                i = 0
                player_found = True
                while i < 4 and player_found:
                    if self.board[row_ind+i][col_ind+i] != player:
                        player_found = False
                    i += 1
                if player_found:
                    return True
        for row_ind in range(self.rows - 3):
            for col_ind in range(3, self.cols):
                i = 0
                player_found = True
                while i < 4 and player_found:
                    if self.board[row_ind+i][col_ind-i] != player:
                        player_found = False
                    i += 1
                if player_found:
                    return True
        return False
    
    def is_full(self):
        for row in self.board:
            if None in row:
                return False
        return True