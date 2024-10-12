import random
from sys import exit
import os


NAVYBLUE = "Blue"
WHITE = "White"
RED = "Red"
GREEN = "Green"
BLUE = "Blue"
YELLOW = "Yellow"
ORANGE = "Orange"
PURPLE = "Purple"
CYAN = "Cyan"

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = ('Donut', 'Square', 'Diamond', 'Oval', 'Knife', 'Heart', 'House', 'Book', 'Arrow')


class Picture:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    
    def __str__(self):
        return (f"{self.color} {self.shape}") #TO DO

    def __eq__(self, other):
        if isinstance(other, Picture):
            return self.color == other.color and self.shape == other.shape
        return False


class Card:
    def __init__(self, picture):
        self.picture = picture
        self.face_up = False

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.picture == other.picture
        return False

    def __str__(self):
        return str(self.picture)


class Board:
    def __init__(self):
        self.board = []
        self.boardwidth = 4
        self.boardheight = 4
        self.number_of_pairs = self.boardwidth * self.boardheight // 2
        self.pairs_found = 0
        self.game_ended = False

    def prepare_board(self):
        pictures = [Picture(shape, color) for shape in ALLSHAPES for color in ALLCOLORS]
        random.shuffle(pictures)
        pictures = pictures[:self.number_of_pairs]
        deck = [Card(picture) for picture in pictures for _ in range(2)]
        random.shuffle(deck)
        self.board = [[deck.pop() for _ in range(self.boardwidth)] for _ in range(self.boardheight)]
        self.pairs_found = 0
        self.game_ended = False

    def check_game(self):
        if self.pairs_found == self.number_of_pairs:
            self.game_ended = True
        else:
            self.game_ended = False

    def __str__(self):
        board_state = ""
        print()

        r = 0
        c = 0
        for row in self.board:
            for card in row:
                if card.face_up:
                    board_state += str(card) + "| "
                else:
                    if c == 0:
                        board_state += f"| ____{r}_{c}____| "
                        c += 1
                    else:
                        board_state += f"____{r}_{c}____| "
                        c += 1
            r += 1
            c = 0
            board_state += "\n"
        return board_state


def main():
    game_board = Board()
    game_board.prepare_board()
    print("\n>>> Game start! <<<\n")
    while True:
        game_board.check_game()
        if game_board.game_ended:
            new_game(game_board)
        first_card = card_pick(game_board, 'first')
        second_card = card_pick(game_board, 'second')
        if first_card == second_card:
            print("OO -> It is a match!")
            game_board.pairs_found += 1
            print(f"You found {game_board.pairs_found} out of {game_board.number_of_pairs}.\n")
            game_board.board[firstrow][firstcol].face_up = True
        else:
            print(f"XX -> Oh no. You missed!\n")
            first_card.face_up = False
            second_card.face_up = False


def new_game(game_board):
    response = input(">>> Want to play another one? ('y' = yes, 'n' = no): ")
    response.strip()
    if response == "y":
        game_board.prepare_board()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(">-> THE BOARD <-<\n", game_board)
        return
    elif response == "n":
        end_game()
    else:
        print("\n!! I don't understand that. Please try again.\n")
        new_game(game_board)

firstrow = ""
firstcol = ""
def card_pick(game_board, order):
    pick = input(f"Pick your {order} card. (format is 'row column', enter 'end' to end the game): ")
    pick = pick.strip()
    if pick == 'end':
        end_game()
    row, column = check_input(game_board, pick)
    if row is None:
        return card_pick(game_board, order)
    if order == "first":
        global firstrow, firstcol
        firstrow = row
        firstcol = column
        print(f"> First picture is {game_board.board[firstrow][firstcol]} (coordinates: {firstrow} - {firstcol}).\n")
        game_board.board[firstrow][firstcol].face_up = True
        return game_board.board[firstrow][firstcol]
    if order == "second":
        os.system('cls' if os.name == 'nt' else 'clear')
        game_board.board[row][column].face_up = True
        print(">-> THE BOARD <-<\n", game_board)
        print(f"> First picture is {game_board.board[firstrow][firstcol]} (coordinates: {firstrow} - {firstcol}).")
        print(f"> Second picture is {game_board.board[row][column]} (coordinates: {row} - {column}).")
        game_board.board[firstrow][firstcol].face_up = False
        return game_board.board[row][column]


def check_input(game_board, pick):
    pick = pick.split()
    if len(pick) != 2 or not pick[0].isnumeric() or not pick[1].isnumeric():
        print("\n!! Sorry, I don't understand. Try again.\n")
        return None, None
    row = int(pick[0])
    if row < 0 or row >= game_board.boardwidth:
        print("\n!! Row you entered is not on the game board. Please try again.\n")
        return None, None
    column = int(pick[1])
    if column < 0 or column >= game_board.boardwidth:
        print("\n!! Column you entered is not on the game board. Please try again.\n")
        return None, None
    if game_board.board[row][column].face_up:
        print("\n!! Seems that this card is already revealed. Please try again.\n")
        return None, None
    return row, column
    

def end_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n>>> Thanks for playing! Have a great day! <<<\n")
    exit()


if __name__ == '__main__':
    main()