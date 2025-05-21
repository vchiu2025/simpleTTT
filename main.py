from GameMode import DumbBotGame, SmartBotGame, PvPGame
from constants import (
    HEADER,
    OPENING_CHOICES,
    EXITING_MESSAGE,
    INVALID_AIBOT_CHOICE,
    INVALID_OPENING_CHOICE,
    OPENING_CHOICE_PROMPT,
    AIBOT_CHOICE_PROMPT,
    NOW_PLAYING_DUMB_BOT,
    NOW_PLAYING_SMART_BOT
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
                print(NOW_PLAYING_DUMB_BOT)
                DumbBotGame().play()
            elif play_dumb_or_smart == UserChoosesTo.PLAY_SMART_BOT:
                print(NOW_PLAYING_SMART_BOT)
                SmartBotGame().play()
            else:
                print(INVALID_AIBOT_CHOICE)

        elif choice == UserChoosesTo.PLAY_PVP:
            PvPGame().play()
        elif choice == UserChoosesTo.EXIT:
            print(EXITING_MESSAGE)
            break
        else:
            print(INVALID_OPENING_CHOICE)


if __name__ == "__main__":
    main()
