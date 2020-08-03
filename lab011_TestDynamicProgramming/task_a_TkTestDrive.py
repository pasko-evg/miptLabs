from tkinter import *

root = Tk()
root.title("Chess board")

CHESSBOARD_SIZE = 8
CELL_SIZE = 50


class ChessCell():
    def __init__(self, board):
        self.board = board
    
    def fill_color(self, x, y, color):
        self.board.canvas.create_rectangle(
            0 + x, 0 + y, CELL_SIZE + x, CELL_SIZE + y, fill='#fff', outline='#000')
    def __repr__(self):
        return str(id(self))


class ChessBoard:
    def __init__(self, master):
        self.canvas = Canvas(master, width=CELL_SIZE * CHESSBOARD_SIZE * 2, height=CELL_SIZE * CHESSBOARD_SIZE * 2)
        self.cells = [[ChessCell(self)] * CHESSBOARD_SIZE for i in range(CHESSBOARD_SIZE)]

        self.canvas.pack()

        x = 0
        y = 0
        color = '#fff'
        for i in range(CHESSBOARD_SIZE):
            y = 0
            for j in range(CHESSBOARD_SIZE):
                self.cells[i][j].fill_color(x, y, color)
                y += CELL_SIZE
            x += CELL_SIZE


chess_board = ChessBoard(root)
root.mainloop()


# Печать ячеек
# for item in chess_board.cells:
#     print(item)
