# Code Academy CS101 Final Project
# BattleShip game inside of terminal using python

from battleship_board import Board
import sys
import random

class BattleShip:
    
    def __init__(self):
        self.name = ""
        self.size = 0
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        
        print("Enter your name:")
        self.name = input()
        print("Hello {}, welcome to Battle Ship".format(self.name))
        print("Enter the size of the board (8, 9, 10)")
        self.size = int(input())
        print("\n \n \n")
        self.board = Board(self.name, self.size)

    def turn(self, player, pc):
        x = int(input("Please enter the numerical coordinate for your shot:"))
        alpha = input("Please enter the alphabetical coordinate for your shot:").upper()
        pc.shot_fired(x, alpha)

        x = random.randint(0, self.size)
        alpha = self.letters[random.randint(0, 9)]
        player.shot_fired(x, alpha)


    
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

def show_game(player_board, pc_board):
    print(player_board)
    print(pc_board)




    
# game start
new_game = game_start()
if new_game == 0:
    sys.exit()
player_board = new_game.board
player_board.user_setup_board()
pc_board = Board("Your Shots", new_game.size)
pc_board.auto_populate()

show_game(player_board, pc_board)

while player_board.is_alive() and pc_board.is_alive():
    print("Both players active. Turn will begin!")
    new_game.turn(player_board, pc_board)
    show_game(player_board, pc_board)


