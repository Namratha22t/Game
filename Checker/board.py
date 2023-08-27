import pygame
from .constants import *
from .piece import Piece
class Board:
    def __init__(self):
        self.board=[]
        self.grey_left=self.white_left=ROWS
        self.grey_kings=self.white_kings=0
        self.create_board()
    def draw_squares(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2,COLS,2):
                pygame.draw.rect(win,RED,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
    def move(self,piece,row,col):
        self.board[piece.row][piece.col],self.board[row][col]=self.board[row][col],self.board[piece.row][piece.col]
        piece.move(row,col)
        if row==ROWS-1 or row==0:
            piece.make_king()
            if piece.color==WHITE:
                self.white_kings+=1
            else:
                self.grey_kings+=1
    def get_piece(self,row,col):
        return self.board[row][col]
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                # if col % 2 == ((row +  1) % 2):
                if row < 1:
                    self.board[row].append(Piece(row, col, WHITE))
                elif row > ROWS-2:
                    self.board[row].append(Piece(row, col, GREY))
                else:
                    self.board[row].append(0)
                
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    # def remove(self, pieces):
    #     for piece in pieces:
    #         self.board[piece.row][piece.col] = 0
    #         if piece != 0:
    #             if piece.color == GREY:
    #                 self.grey_left -= 1
    #             else:
    #                 self.white_left -= 1
    
    def winner(self):
        if self.white_kings == 1:
            return WHITE
        elif self.grey_kings==1:
            return GREY
        
        return None 
    
    def moves1(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        if piece is None:
            return False
        
        dx = end_col - start_col
        dy = end_row - start_row
        
        # Check if it's a valid diagonal move
        if abs(dx) == abs(dy) and abs(dx) == 2:
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2
            
            # Check if there's an opponent's piece to capture
            if self.board[mid_row][mid_col] is None:
                return False
            
            # Move the piece and capture the opponent's piece
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None
            self.board[mid_row][mid_col] = None
            return True
        
        return False