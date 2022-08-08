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
        self.status = {}
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
            item = self.board[i][1]
            if self.name == "Your Shots" and item == "[+]":
                item = "[ ]"
            line += item
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
            while not placed:
                x = random.randint(0, self.size)
                alpha = self.letters[random.randint(0, 9)]
                orientation = random.randint(0, 1)
                placed = self.place_boat(length, orientation, x, alpha)

    # Given a length, orientation (0 = vertical, 1 = horizontal) and coordinates for the top or left most side of the boat
    # Will return true and place boat if the ship fits and does not overlap exsisting ships
    # WIll return false and not place boat if ther are obstructions
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
            self.status[square] = "Boat"
        return True
        
    def user_setup_board(self):
        print(
        '''
        You will now begin placing your ships! There are a total of 7 ships to place.
        You can choose either vertical (0) or horizontal (1) layout for the ship.
        The coordinate you depict will set the topmost or left most point on each ship.
        You can also choose to have a computer generated random setup for the ships as well!
        '''
        )
        print("Would you like to have a computer generated random setup? Y/N")
        rand_setup = input()
        if rand_setup.upper() == "Y":
            self.auto_populate()
        else:
            for ship in self.ships:
                placed = False
                while not placed:
                    print(self)
                    print("This is your {} and it is {} in length".format(ship[0], ship[1]))
                    orientation = input("Please enter 0 for a vertical layout or 1 for a horizontal layout.   ")
                    x = input("Please choose a numerical coordinate for your {}. This ship is {} squares in length.   ".format(ship[0], ship[1]))
                    alpha = input("Please choose a alphabetical coordinate for your {}. This ship is {} squares in length.   ".format(ship[0], ship[1])).upper()
                    placed = self.place_boat(ship[1], orientation, int(x), alpha)
                    if not placed:
                        print("That was an invalid coordinate for the ship. Make sure you are not overlapping with your other boats or falling off the edge of the board!")
                    else:
                        print("Perfect! This is what your board looks like right now")
                        print(self)
            

    def is_alive(self):
        return "Boat" in self.status.values() 
    
    def shot_fired(self, x, alpha):
        square = 0
        y = self.letters.index(alpha)
        square = y * self.size + (x - 1)

        if self.has_boat(square):
            self.board[square][1] = "[X]"
            self.status[square] = "Hit"
            name = self.name
            if name == "Your Shots":
                name = "PC"
            print("{} has been hit at coordinate {}, {}".format(name, x, alpha))
        else:
            self.board[square][1] = "[O]"
            self.status[square] = "Miss"
            print("Shot was fired at coordinate {}, {}. There was no ship there.".format(x, alpha))

