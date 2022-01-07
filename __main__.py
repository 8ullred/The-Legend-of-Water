"""
Text Based RPG Thing
Ronald + Bill
"""

import os
from characters import *
from actions import *


def main():
    version = '0.1.2'

    # prints some important information about the game
    print(f'{Colors.WATER}The Legend of the Filtered Water{Colors.END} v{version}\n'
          'by: Bill & Ronald')
    sleep(2)

    print('\n' * 0)

    # TODO: add save functionality
    # looks for a save file
    save_files = os.listdir('saves')

    # checks if there's a save file
    if save_files:
        # TODO: have all saves files be printed
        print('Saves: ')
        # [print(f'{i+1}. {save}') for i, save in enumerate(save_files)]
        #
        # print()
        # # TODO: Error Trapping
        # # TODO: allow selection of save file
        # selection = int(input('Select save file: '))
        #
        # # TODo: open save file and load stats
        # with open(save_files[selection - 1], 'r') as save:
        #     player = pk.load(save)
        #
        # print('Welcome Back!')

    else:
        # TODO: add sleeps for time spacing
        # TODO: finish tutorial

        # tutorial to game
        # TODO: Error Trapping
        while True:
            do_speedup = input('Would you like to speed up the intro (y/n)? ')

            match do_speedup:
                case 'y' | 'Y':
                    reading_speed = 0.01
                case 'n' | 'N':
                    reading_speed = 0.08
                case '¥':
                    reading_speed = 0
                case _:
                    print('Invalid Input - Please Retry\n')
                    continue

            print('\n' * 10)
            sleep(1)
            read_story('startIntro', 'Introduction: ', reading_speed)

            break

        # TODO: Error Trapping (no longer than 20 chars)
        player = Player(input(' '))

        print()
        print_bracket(1)

        read_story('startBattle1')
        print('\n')

        # TODO: tutorial fights
        while True:
            reeco = Enemy('Reeco')
            if start_fight(player, reeco, True):
                break

        read_story('endBattle1', player=player)

        # print()
        # print('Welcome to The Legend of Water')

    # menu(player)


if __name__ == '__main__':
    main()
