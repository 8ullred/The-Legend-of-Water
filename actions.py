from time import sleep
from characters import Player
from constants import Colors


class NoPlayerName(NameError):
    pass


def read_story(scene: str, header: str = None, reading_rate: float = 0.08, player: Player = None):
    start_reading = False

    if header is not None:
        for char in header:
            print(char, end='')
            sleep(reading_rate * 8) if char == ':' else sleep(reading_rate)

        else:
            print()

    try:
        with open('lore.txt', 'r') as file:
            for line in file:
                if line != '\n':
                    line = line.strip('\n')

                if start_reading:
                    if line == '--end':
                        return
                    elif line == '--lineBreak':
                        print()
                    else:
                        check_for_code, pattern_matched = False, False

                        for char in line:
                            match char:
                                case ',' | '.':
                                    sleep_time = reading_rate * 8
                                case ':':
                                    sleep_time = reading_rate * 20
                                case '–':
                                    check_for_code = True
                                    continue
                                case _:
                                    sleep_time = reading_rate

                            if check_for_code:
                                match char:
                                    case '1':
                                        char = Colors.COMMON
                                    case '2':
                                        char = Colors.UNCOMMON
                                    case '3':
                                        char = Colors.RARE
                                    case '4':
                                        char = Colors.EPIC
                                    case '5':
                                        char = Colors.LEGENDARY_B
                                    case 'W':
                                        char = Colors.WATER
                                    case 'E':
                                        char = Colors.END
                                    case 'P':
                                        if player is None:
                                            raise NoPlayerName
                                        else:
                                            char = player.name

                                sleep_time, check_for_code = 0, False

                            print(char, end='')
                            sleep(sleep_time)

                else:
                    if line.split() == ['--scene:', scene]:
                        start_reading = True
        print('No Scene Found')

    except NoPlayerName:
        print('No Player Was Passed - This Scene Requires the Name of a Player')


def print_bracket(stage: int):
    match stage:
        case 1:
            print(f'{Colors.GREEN}You{Colors.END} ------|\n'
                  '          X----------|\n'
                  'Reeco ----|          |\n'
                  '                     X----------|\n'
                  'Andy -----|          |          |\n'
                  '          X----------|          |\n'
                  'Kasra ----|                     |\n'
                  f'                                X----------{Colors.LEGENDARY_B}[Winner]{Colors.END}\n'
                  'Jeremy ---|                     |\n'
                  '          X----------|          |\n'
                  'Felix ----|          |          |\n'
                  '                     X----------|\n'
                  'Carol ----|          |\n'
                  '          X----------|\n'
                  'Bebald ---|')
        case 2:
            print('----------|\n'
                  f'          {Colors.GREEN}You{Colors.END} -------|\n'
                  f'{Colors.STRIKE}Reeco{Colors.END} ----|          |\n'
                  '                     X----------|\n'
                  f'{Colors.STRIKE}Andy{Colors.END} -----|          |          |\n'
                  '          Kasra -----|          |\n'
                  '----------|                     |\n'
                  f'                                X----------{Colors.LEGENDARY_B}[Winner]{Colors.END}\n'
                  '----------|                     |\n'
                  '          Jeremy ----|          |\n'
                  f'{Colors.STRIKE}Felix{Colors.END} ----|          |          |\n'
                  '                     X----------|\n'
                  f'{Colors.STRIKE}Carol{Colors.END} ----|          |\n'
                  '          Felix -----|\n'
                  '----------|')
        case 3:
            print('----------|\n'
                  '          X----------|\n'
                  f'{Colors.STRIKE}Reeco{Colors.END} ----|          |\n'
                  f'                     {Colors.GREEN}You{Colors.END} -------|\n'
                  f'{Colors.STRIKE}Andy{Colors.END} -----|          |          |\n'
                  f'          {Colors.STRIKE}Kasra{Colors.END} -----|          |\n'
                  '----------|                     |\n'
                  f'                                X----------{Colors.LEGENDARY_B}[Winner]{Colors.END}\n'
                  '----------|                     |\n'
                  f'          {Colors.STRIKE}Jeremy{Colors.END} ----|          |\n'
                  f'{Colors.STRIKE}Felix{Colors.END} ----|          |          |\n'
                  '                     Bebald ----|\n'
                  f'{Colors.STRIKE}Carol{Colors.END} ----|          |\n'
                  '          X----------|\n'
                  '----------|')
