# Board Class
from ssl import AlertDescription


class Board:

    def __init__(self, name, size=8):
        self.size = size
        self.name = name
        self.board = []
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for i in range(size ** 2):
            self.board.append([i, "[ ]"])
    
    def __repr__(self):
        final = ""
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
    

test_board = Board("test", 10)
print(test_board)


            
            




        

