# Code Academy CS101 Final Project
# BattleShip game inside of terminal using python

from battleship_board import Board
import sys

class BattleShip:
    
    def __init__(self):
        self.name = ""
        self.size = 0
        
        print("Enter your name:")
        self.name = input()
        print("Hello {}, welcome to Battle Ship".format(self.name))
        print("Enter the size of the board (8, 9, 10)")
        self.size = int(input())
        print("\n \n \n")
        self.board = Board(self.name, self.size)

    
def game_start():
    new_game = 0
    print("Battle Ship")
    print("Do you want to start a new game? Y/N")
    ans = input()
    if ans.upper() == "Y":
        new_game = BattleShip()
    else:
        print("Ending Game")
        new_game = 0
    return new_game

def show_game(player, pc):
    print(player_board)
    print(pc_board)

    
# game start
new_game = game_start()
if new_game == 0:
    sys.exit()
player_board = new_game.board
pc_board = Board("Your Shots", new_game.size)
pc_board.auto_populate()

show_game(player_board, pc_board)


