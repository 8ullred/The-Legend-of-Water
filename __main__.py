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
    version = '0.1.2'

    # prints some important information about the game
    print(f'{Colors.WATER}The Legend of the Filtered Water{Colors.END} v{version}\n'
          'by: Bill & Ronald')
    sleep(2)

    current_save, is_new_save = get_saves()

    # checks if a new save has been created
    if is_new_save:
        reading_speed = intro()

        player = tutorial(reading_speed)
    else:
        player = Player(current_save)

        print('Welcome Back!')

    menu(player, current_save)


if __name__ == '__main__':
    main()
