# Board Class
class Board:
    ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Cruiser", 3], ["Destroyer", 2], ["Submarine", 1]]

    def __init__(self, name, size=8):
        self.size = size
        self.name = name
        self.alive = True
        self.board = []
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        if self.name is not "PC":
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
            line += self.board[i][1]
            if (i + 1) % self.size == 0:
                final += line + "\n"
                line = ""
            else:
                continue
        return final

    def has_boat(self, square):
        # checks to see if the square has a boat
        if self.board[square] == "[#]":
            return True
        else:
            return False
    
    def auto_populate(self):
        return 0

    def is_alive(self):
        return self.alive
    
    def shot_fired(self, x, alpha):
        square = 0
        y = self.letters.index(alpha)
        square = y * self.size + x

        if self.has_boat(square):
            print("{} has been hit at coordinate {}, {}".format(self.name, x, alpha))
        else:
            print("Shot was fired at coordinate {}, {}. There was no ship there.".format(x, alpha))
    
        
            
            




        

