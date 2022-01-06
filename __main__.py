"""
Text Based RPG Thing
Ronald + Bill
"""

from os import listdir
from characters import *
from actions import *


def main():
    version = 0.1

    # prints some important information about the game
    print(f'The Legend of the Filtered Water v{version}\n'
          'by: Bill & Ronald')
    sleep(2)

    print('\n' * 0)

    # looks for a save file
    save_files = listdir('saves')

    # checks if there's a save file
    if save_files:
        print('Saves: ')
        [print(f'{i+1}. {save}') for i, save in enumerate(save_files)]

        print()
        # TODO: Error Trapping
        selection = int(input('Select save file: '))

        with open(save_files[selection - 1], 'r') as save:
            user = save.read()

        print('Welcome Back!')

    else:
        # TODO: add sleeps for time spacing
        # TODO: finish tutorial

        # tutorial to game
        # TODO: Error Trapping
        do_speedup = input('Would you like to speed up the intro (y/n)? ').lower()

        if do_speedup == 'y':
            read_story('startIntro', 'Introduction: ', 0.001)
        else:
            read_story('startIntro', 'Introduction: ')

        # TODO: Error Trapping
        user = Player(input(' '))

        # TODO: print tournament bracket

        read_story('startBattle1')
        print()

        # TODO: tutorial fights
        reeco = Enemy('Reeco')
        start_fight(user, reeco, True)

        # print()
        # print('Welcome to The Legend of Water')

    # menu(user)


if __name__ == '__main__':
    main()
