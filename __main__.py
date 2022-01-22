from characters import *

'''
A Text-Based RPG
The Legend of Water
Very unfinished but it works

By: Ronald && Bill
'''

'''
TODO: 
'''


def main() -> None:
    """
    Main program
    """

    version = '0.1.6'

    # prints some important information about the game
    print(f'{Colors.WATER}The Legend of the Filtered Water{Colors.END} v{version}\n'
          'by: Bill & Ronald')
    sleep(2)

    current_save, player = load_save()

    # checks if a new save has been created
    if player is None:
        # calls corresponding functions for the tutorial
        reading_speed = intro('lore.txt')

        player = tutorial('lore.txt', reading_speed)
    else:
        print('Welcome Back!')

    menu(player, current_save)  # calls the main menu


if __name__ == '__main__':
    main()
