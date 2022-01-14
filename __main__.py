"""
¥
Text Based RPG Thing
Ronald + Bill
"""
from actions import *
from characters import *

"""
TODO: 
"""


def main():
    version = '0.1.3'

    # prints some important information about the game
    print(f'{Colors.WATER}The Legend of the Filtered Water{Colors.END} v{version}\n'
          'by: Bill & Ronald')
    sleep(2)

    current_save, player = load_save()

    # checks if a new save has been created
    if player is None:
        reading_speed = intro()

        player = tutorial(reading_speed)
    else:
        print('Welcome Back!')

    menu(player, current_save)


if __name__ == '__main__':
    main()
