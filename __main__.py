"""
¥
Text Based RPG Thing
Ronald + Bill
"""

import os
from characters import *
from actions import *
from constants import ENEMY_TYPES


def intro():
    # TODO: finish tutorial ****
    # TODO: add sleeps for time spacing **

    # tutorial to game
    # TODO: Error Trapping ***
    while True:
        reading_speed = None

        match input('Would you like to speed up the intro (y/n)? '):
            case 'y' | 'Y':
                reading_speed = 0.01
            case 'n' | 'N':
                reading_speed = 0.08
            case '¥':
                reading_speed = 0
            case _:
                print('Invalid Input - Please Retry\n')

        if reading_speed is not None:
            break

    print('\n' * 10)
    sleep(1)
    read_story('startIntro', 'Introduction: ', reading_speed)

    return reading_speed


def tutorial(reading_speed: float, player: Player):
    print()
    print_bracket(1)

    read_story('startBattle1', reading_rate=reading_speed)
    print('\n')

    while True:
        reeco = Enemy('Reeco', ENEMY_TYPES['tutorial1'])
        if start_fight(player, reeco, True):
            break

    read_story('endBattle1', reading_rate=reading_speed, player=player)

    print()
    print_bracket(2)

    read_story('startBattle2', reading_rate=reading_speed)
    print('\n')

    while True:
        kasra = Enemy('Kasra', ENEMY_TYPES['tutorial2'])
        if start_fight(player, kasra, True):
            break

    read_story('endBattle2', reading_rate=reading_speed)
    print('\n')

    read_story('conclusion', reading_rate=reading_speed, player=player)

    print('\n')
    print(f'Welcome to {Colors.WATER}The Legend of Water{Colors.END}')
    player.__heal__()


def main():
    version = '0.1.2'

    # prints some important information about the game
    print(f'{Colors.WATER}The Legend of the Filtered Water{Colors.END} v{version}\n'
          'by: Bill & Ronald')
    sleep(2)

    print('\n' * 0)

    # TODO: add save functionality *
    # TODO: fix save system **

    # gets all save files
    save_files = os.listdir('saves')
    # TODO: load stats ***

    while True:
        print('Saves: ')
        for i, file in enumerate(save_files):
            print(f'\t{i + 1} {file.strip(".txt")}')
        try:
            selection = int(input('Choose Save: '))

            if selection > 3 or selection < 1:
                print('Invalid Selection - Please Retry')
            else:
                current_save = save_files[selection-1]

                if current_save == 'Empty Save 1.txt' \
                        or current_save == 'Empty Save 2.txt' \
                        or current_save == 'Empty Save 3.txt':
                    print('creating new')
                    new_save = True

                else:
                    print('using old')
                    new_save = False
                    with open(f'saves/{current_save}', 'r'):
                        player = Player(current_save.strip('.txt'))

                break

        except ValueError:
            print('Invalid Input - Please Retry')

    # checks if a new save has been created
    if new_save:
        reading_speed = intro()

        player = Player(input(' '))
        while True:

            if 21 > len(player.name) > 2:
                break
            elif len(player.name) < 3:
                print(f'Player name too short: {len(player.name)} < 3')
            else:
                print(f'Player name too long: {len(player.name)} > 20')

            player = Player(input('Enter Name: '))

        tutorial(reading_speed, player)
    else:
        print('Welcome Back!')

    menu(player, current_save)


if __name__ == '__main__':
    main()
