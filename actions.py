from os import listdir

from constants import Colors


def color_table():
    for i in range(256):
        if i % 16 == 0:
            print()
        print(f'\t\u001b[38;5;{i}m{i}\033[0m', end='')


def get_username() -> str:

    name = input(' ')

    while True:
        if 21 > len(name) > 2:
            return name
        elif len(name) < 3:
            print(f'Player name too short: {len(name)} < 3')
        else:
            print(f'Player name too long: {len(name)} > 20')

        name = input('Enter Name: ')


def get_saves() -> tuple[str, bool]:
    # TODO: add save functionality *
    # TODO: fix save system **

    # gets all save files
    save_files = listdir('saves')
    # TODO: load stats ***

    while True:
        print('Saves: ')
        for i, file in enumerate(save_files):
            print(f'\t{i + 1} {file.strip(".txt")}')

        try:
            selection = int(input('Choose Save: '))

            if 4 > selection > 0:
                save = save_files[selection - 1]

                match save.split():
                    case ['Empty', 'Save', '1.txt' | '2.txt' | '3.txt']:
                        is_new_save = True
                    case _:
                        is_new_save = False
                return save, is_new_save

            else:
                print('Invalid Selection - Please Retry')

        except ValueError:
            print('Invalid Input - Please Retry')


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
                  '          Bebald ----|\n'
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


def display_menu(selections: list, title: str) -> str:
    selections = [selections[i:i+6] for i in range(0, len(selections), 6)]

    pages = len(selections)
    current_page = 1

    while True:
        print(f'\n{title}: ')

        [print(f'\t{Colors.fill(Colors.OPTION, i + 1)} {item}') for i, item in enumerate(selections[current_page - 1])]
        [print() for _ in range(6 - len(selections[current_page-1]))]

        print(f"{Colors.fill(Colors.OPTION, '<')} Back "
              f"| {Colors.fill(Colors.OPTION, 'Page')} {Colors.fill(Colors.OPTION, current_page)} of {pages} "
              f"| Next {Colors.fill(Colors.OPTION, '>')}")

        selection = [char for char in input('Enter Selection (Leave Blank to Quit): ')]

        try:
            match selection:
                case ['<']:
                    current_page -= 1 if current_page > 1 else 1
                case ['>']:
                    current_page += 1 if current_page < pages else pages
                case ['<', '<']:
                    if (current_page - int(pages / 10)) > 1:
                        current_page -= int(pages / 10)
                    else:
                        current_page = 1
                case ['>', '>']:
                    if (current_page + int(pages / 10)) < pages:
                        current_page += int(pages / 10)
                    else:
                        current_page = pages
                case ['<', '<', '<']:
                    current_page = 1
                case ['>', '>', '>']:
                    current_page = pages
                case [('P' | 'p'), ('A' | 'a'), ('G' | 'g'), ('E' | 'e'), *page] | \
                     [('P' | 'p'), ('A' | 'a'), ('G' | 'g'), ('E' | 'e'), ' ', *page] | \
                     [('P' | 'p'), ('G' | 'g'), *page] | [('P' | 'p'), ('G' | 'g'), ' ', *page] | \
                     [('P' | 'p'), *page] | [('P' | 'p'), ' ', *page]:
                    page = int(''.join(page))
                    if pages >= page > 0:
                        current_page = page
                    else:
                        print(f'Page {page} Not Found - Please Retry')
                case [item]:
                    item = int(item)
                    if len(selections[current_page-1]) >= item > 0:
                        return selections[current_page-1][item-1]
                    else:
                        print('Invalid Selection - Please Retry')
                case []:
                    return ''
                case _:
                    print('Invalid Input - Please Retry')

        except ValueError:
            print('Invalid Input Error- Please Retry')
