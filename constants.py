from enum import StrEnum


class Player(StrEnum):
    FIRST = "X"
    SECOND = "O"


class UserChoosesTo(StrEnum):
    PLAY_AI = "1"
    PLAY_PVP = "2"
    EXIT = "3"
    PLAY_DUMB_BOT = "1"
    PLAY_SMART_BOT = "2"


INVALID_MOVE_MESSAGE = "Invalid move dumbass."
TAKEN_SQUARE_MESSAGE = "This square is already taken idiot."
DRAW_MESSAGE = "Congrats its a draw, you guys are equally dumb"
POSSIBLE_MOVES = [
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2],
]

HEADER = "================ Welcome to my simple Tic-Tac-Toe Game ================"
OPENING_CHOICES = "\n1. Single Player (Play vs AI)\n2. Two Player\n3. Exit"
EXITING_MESSAGE = "Exiting..."
INVALID_OPENING_CHOICE = "Invalid choice. Enter 1, 2, or 3."
INVALID_AIBOT_CHOICE = "Invalid choice. Enter 1 or 2."
OPENING_CHOICE_PROMPT = "Enter your choice (1-3): "
AIBOT_CHOICE_PROMPT = "Who do you want to play? \nDumb Bot (1) or Smart Bot (2)? : "
