from constants import Colors


def color_table():
    for i in range(256):
        if i % 16 == 0:
            print()
        print(f'\t\u001b[38;5;{i}m{i}\033[0m', end='')


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


def list_menu(selections: list, title: str) -> str:
    selections = [selections[i:i+6] for i in range(0, len(selections), 6)]

    current_page = 1

    while True:
        print(f'\n{title}: ')

        [print(f'\t{Colors.fill(Colors.OPTION, i + 1)} {item}') for i, item in enumerate(selections[current_page - 1])]
        [print() for _ in range(6 - len(selections[current_page-1]))]

        print(f"{Colors.fill(Colors.OPTION, '<')} Back "
              f"| {Colors.fill(Colors.OPTION, 'Page')} {Colors.fill(Colors.OPTION, current_page)} of {len(selections)} "
              f"| Next {Colors.fill(Colors.OPTION, '>')}")

        selection = [char for char in input('Enter Selection: ')]

        try:
            match selection:
                case ['<']:
                    current_page -= 1 if current_page > 1 else 0
                case ['>']:
                    current_page += 1 if current_page < len(selections) else 0
                case ['P' | 'p', page] | ['P' | 'p', 'A' | 'a', 'G' | 'g', 'E' | 'e', page] | \
                     ['P' | 'p', ' ', page] | ['P' | 'p', 'A' | 'a', 'G' | 'g', 'E' | 'e', ' ', page]:
                    page = int(page)
                    if len(selections) >= page > 0:
                        current_page = page
                    else:
                        print(f'Page {page} Found - Please Retry')
                case [item]:
                    item = int(item)
                    if len(selections[item]) >= item > 0:
                        return selections[current_page-1][item-1]
                    else:
                        print('Invalid Selection - Please Retry')
                case _:
                    print('Invalid Input - Please Retry')

        except ValueError:
            print('Invalid Input - Please Retry')
