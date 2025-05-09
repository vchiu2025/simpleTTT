from simpleTTT import Board
from run_game import play_dumb_bot, play_smart_bot, play_pvp
from constants import (
    HEADER,
    OPENING_CHOICES,
    EXITING_MESSAGE,
    INVALID_AIBOT_CHOICE,
    INVALID_OPENING_CHOICE,
    OPENING_CHOICE_PROMPT,
    AIBOT_CHOICE_PROMPT,
)
from constants import UserChoosesTo


def main():
    print(HEADER)
    while True:
        print(OPENING_CHOICES)
        choice = input(OPENING_CHOICE_PROMPT)
        if choice == UserChoosesTo.PLAY_AI:
            play_dumb_or_smart = input(AIBOT_CHOICE_PROMPT)
            if play_dumb_or_smart == UserChoosesTo.PLAY_DUMB_BOT:
                play_dumb_bot()
            elif play_dumb_or_smart == UserChoosesTo.PLAY_SMART_BOT:
                play_smart_bot()
            else:
                print(INVALID_AIBOT_CHOICE)

        elif choice == UserChoosesTo.PLAY_PVP:
            play_pvp()
        elif choice == UserChoosesTo.EXIT:
            print(EXITING_MESSAGE)
            break
        else:
            print(INVALID_OPENING_CHOICE)


if __name__ == "__main__":
    main()
