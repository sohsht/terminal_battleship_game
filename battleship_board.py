# Board Class
import random
import math

class Board:
    ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Destroyer", 2], ["Destroyer", 2], ["Submarine", 1], ["Submarine", 1]]

    def __init__(self, name, size=8):
        self.size = size
        self.name = name
        self.alive = True
        self.board = []
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        if self.name != "Your Shots":
            self.user = True
        else:
            self.user = False
        for i in range(size ** 2):
            self.board.append([i, "[ ]"])
    
    def __repr__(self):
        final = ("{}\n".format(self.name))
        num_line = "   "
        for i in range(self.size):
            num_line += " {} ".format(i + 1)
        final += num_line + "\n"
        line = ""
        for i in range(self.size ** 2):
            if i in range(0, self.size ** 2, self.size):
                line += " {} ".format(self.letters[round(i / self.size)])
            ### Need to hide pc autopopulated slots below
            line += self.board[i][1]
            if (i + 1) % self.size == 0:
                final += line + "\n"
                line = ""
            else:
                continue
        return final

    def has_boat(self, square):
        # checks to see if the square has a boat
        if self.board[square][1] == "[+]":
            return True
        else:
            return False
    
    def auto_populate(self):
        for ship in self.ships:
            length = ship[1]
            placed = False
            try_counter = 1
            while not placed:
                x = random.randint(0, self.size)
                alpha = self.letters[random.randint(0, 9)]
                orientation = random.randint(0, 1)
                placed = self.place_boat(length, orientation, x, alpha)
                try_counter += 1
        print("Auto Populated {}'s board".format(self.name))

    def place_boat(self, length, orientation, x, alpha):
        start = 0
        y = self.letters.index(alpha)
        start = y * self.size + (x - 1)
        boatsquare = []

        if start < self.size ** 2:
            if orientation == 0:
                endpoint = start + (length * self.size)
                if endpoint < self.size ** 2:
                    for i in range(length):
                        boatsquare.append(start + (self.size * i))
                else:
                    return False
            else:
                endpoint = start + length - 1
                past_edge = math.floor(start + 1 / self.size) != math.floor(endpoint + 1 / self.size)
                if not past_edge:
                    for i in range(length):
                        boatsquare.append(start + i)
                else:
                    return False
        
        for square in boatsquare:
            if self.has_boat(square):
                return False

        for square in boatsquare:
            self.board[square][1] = "[+]"
        return True
        
        
        


    def is_alive(self):
        return self.alive
    
    def shot_fired(self, x, alpha):
        square = 0
        y = self.letters.index(alpha)
        square = y * self.size + (x - 1)

        if self.has_boat(square):
            print("{} has been hit at coordinate {}, {}".format(self.name, x, alpha))
        else:
            print("Shot was fired at coordinate {}, {}. There was no ship there.".format(x, alpha))
    
        
            
            




        

