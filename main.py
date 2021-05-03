from connectfour import ConnectFour
from player import HumanPlayer, RandomComputerPlayer

if __name__ == '__main__':
    connectFour = ConnectFour()
    first_player = HumanPlayer('X')
    second_player = RandomComputerPlayer('O')
    connectFour.play(first_player, second_player)