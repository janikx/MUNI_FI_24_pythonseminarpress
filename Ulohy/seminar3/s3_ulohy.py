import random
from sys import exit

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
ALLSHAPES = ('donut', 'square', 'diamond', 'lines', 'oval')


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
            main()
        else:
            self.game_ended = False

    def __str__(self):
        board_state = ""
        print()
        for row in self.board:
            for card in row:
                if card.face_up:
                    board_state += str(card) + " | "
                else:
                    board_state += "XXXXX XXXXX | "
            board_state += "\n"
        return board_state


def main():
    game_board = Board()
    game_board.prepare_board()
    print("Game start!")
    while True:
        first_card = card_pick(game_board, 'first')
        second_card = card_pick(game_board, 'second')
        if first_card == second_card:
            print("It is a match!")
            game_board.pairs_found += 1
            print(f"You found {game_board.pairs_found} out of {game_board.number_of_pairs}")
        else:
            print("Oh no. You missed!")
            first_card.face_up = False
            second_card.face_up = False
        if game_board.game_ended:
            new_game(game_board)

def new_game(game_board):
    response = input("Want to play another one? ('y' = yes, 'n' = no): ")
    response.strip()
    if response == "y":
        game_board.prepare_board()
        return
    elif response == "n":
        end_game()
    else:
        print("I don't understand that. Please try again.")
        new_game(game_board)


def card_pick(game_board, order):
    pick = input(f"Pick your {order} card. (format is 'row column', enter 'end' to end the game, enter 'board' to see current board view): ")
    pick = pick.strip()
    if pick == 'end':
        end_game()
    if pick == 'board':
        print(game_board)
        return card_pick(game_board, order)
    row, column = check_input(game_board, pick)
    if row is None:
        return card_pick(game_board, order)
    print(f"Picture is {game_board.board[row][column]} (coordinates: {row} - {column}).")
    game_board.board[row][column].face_up = True
    return game_board.board[row][column]


def check_input(game_board, pick):
    pick = pick.split()
    if len(pick) != 2 or not pick[0].isnumeric() or not pick[1].isnumeric():
        print("Sorry, I don't understand. Try again.")
        return None, None
    row = int(pick[0])
    if row < 0 or row >= game_board.boardwidth:
        print("Row you entered is not on the game board. Please try again.")
        return None, None
    column = int(pick[1])
    if column < 0 or column >= game_board.boardwidth:
        print("Column you entered is not on the game board. Please try again.")
        return None, None
    if game_board.board[row][column].face_up:
        print("Seems that this card is already revealed. Please try again.")
        return None, None
    return row, column
    

def end_game():
    print("Thanks for playing! Have a great day!")
    exit()


if __name__ == '__main__':
    main()