"""
Text Based RPG Thing
Ronald + Bill
"""

from time import sleep


def menu():
    while True:
        print('1 - Battle\n'
              '2 - Town\n'
              '3 - Stats\n'
              '4 - Bag\n'
              r"'Q' - Quit")

        print()
        cmd = input('> ')

        match cmd.lower():
            case '1':
                pass
            case '2':
                pass
            case '3':
                open_stats(10, 5, 100)
            case '4':
                open_bag(23, 7, 'aaa')
            case 'q':
                print("Thank you!")
                return
            case 'dev':
                pass
            case _:
                print('Invalid Command - Please Retry')


def open_stats(*a):
    print('Stats:')
    for item in a:
        print(f'\t{item=}')

    print()
    _ = input('Hit enter to return to the previous menu.')
    return


def open_bag(*a):
    print('Balance:\n'
          f'\tCurrency: {_currency}\n'
          f'\tSpecial Currency: {_special_currency}')

    print('\nItems: ')
    print('\t', *a)

    print()
    _ = input('Hit enter to return to the previous menu.')
    return


# Setting the base stats for the player
_atk, _hp, _def, _crit_rate, _crit_damage, _currency, _special_currency, _speed =\
    10, 100, 0, 5, 50, 0, 100, 5

# plays the tutorial if the game is being opened for the first time
is_tutorial_finished = False

if not is_tutorial_finished:
    print('this is an introduction be introduced')
    sleep(2)
    print('Welcome to [City Name]')
    is_tutorial_finished = True
else:
    print('Welcome Back!')

menu()
