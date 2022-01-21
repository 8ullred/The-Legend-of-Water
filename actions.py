from os import path

from constants import Colors


def get_username(initial_prompt: str = ' ') -> str:
    """
    Ask user for their in-game name, requests a new name is inputted name is not within constraints.

    :param initial_prompt:
        The prompt for the first ask of the users name. Default is ' '.
    :return:
        Returns the requested username if accepted
    """

    name = input(initial_prompt)  # ask user for name

    while True:
        # checks if username is allowed
        if ' ' in name:
            print('Spaces Are Not Allowed')  # tells user the name is not allowed
        elif len(name) > 20:
            print(f'Player name too long: {len(name)} > 20')
        elif len(name) < 3:
            print(f'Player name too short: {len(name)} < 3')
        elif path.exists(f'saves/{name}.txt'):
            print(f'The username [{name}] already exists')
        elif name.replace('_', '').isalnum():  # checks if username is alphanumeric or contains an underscore
            print('returned name')
            return name  # returns the name
        else:
            # tells user the name has a non-alphanumeric character/underscore
            print('Your Name Contains a Prohibited Character')

        name = input('Enter Name: ')  # ask user for name again


def print_bracket(stage: int) -> None:
    """
    Prints the tournament bracket based on the selected stage.

    :param stage:
        The state of the tournament
    """

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


def selection_menu(selections: list, title: str) -> str:
    """
    Prints a menu based on a list of selections with a title. The menu will have 6 selections on each page and the
    user can cycle between pages. The user will also be able to make a selection by inputting the number of the
    selection. The function will then return the selection if that selection is valid. User may enter nothing to quit
    the menu.

    :param selections:
        The options which are listed in the menu
    :param title:
        The title of the menu
    :return:
        Returns the selection that was made or an empty string
    """

    # formats the selection into an array with a width of 6
    selections = [selections[i:i+6] for i in range(0, len(selections), 6)]

    pages = len(selections)  # the number of pages in the menu
    current_page = 1  # sets the current page

    while True:
        print(f'\n{title}: ')

        # prints each options on the current selected page
        [print(f'\t{Colors.fill(Colors.OPTION, i + 1)} {item}') for i, item in enumerate(selections[current_page - 1])]
        # prints empty lines is the selected page has less than 6 items
        [print() for _ in range(6 - len(selections[current_page-1]))]

        # prints page selection and information
        print(f"{Colors.fill(Colors.OPTION, '<')} Back "
              f"| {Colors.fill(Colors.OPTION, 'Page')} {Colors.fill(Colors.OPTION, current_page)} of {pages} "
              f"| Next {Colors.fill(Colors.OPTION, '>')}")

        # ask for a selection and parses the input
        selection = [char for char in input('Enter Selection (Leave Blank to Quit): ')]

        try:
            # matches the selection to each case
            match selection:
                case ['<']:
                    # subtracts one from the page if the current page is greater than 1
                    current_page -= 1 if current_page > 1 else 0
                case ['>']:
                    # adds one to the page if the current page is less than the total number of pages
                    current_page += 1 if current_page < pages else 0
                case ['<', '<']:
                    # subtracts 1/10 of the total pages if the action does not result in a page number less than 1
                    if (current_page - int(pages / 10)) > 1:
                        current_page -= int(pages / 10)
                    else:
                        # otherwise, sets the current page to 1
                        current_page = 1
                case ['>', '>']:
                    # adds 1/10 of the total pages if the action does not result in a page number greater than the total
                    # number of pages
                    if (current_page + int(pages / 10)) < pages:
                        current_page += int(pages / 10)
                    else:
                        # otherwise, sets the current page to the total number of pages
                        current_page = pages
                case ['<', '<', '<']:
                    current_page = 1  # go to the first page
                case ['>', '>', '>']:
                    current_page = pages  # go to the last page

                # matches various of a page selection
                case [('P' | 'p'), ('A' | 'a'), ('G' | 'g'), ('E' | 'e'), *page] | \
                     [('P' | 'p'), ('A' | 'a'), ('G' | 'g'), ('E' | 'e'), ' ', *page] | \
                     [('P' | 'p'), ('G' | 'g'), *page] | [('P' | 'p'), ('G' | 'g'), ' ', *page] | \
                     [('P' | 'p'), *page] | [('P' | 'p'), ' ', *page]:

                    page = int(''.join(page))  # joins the page numbers then converts to an int

                    if pages >= page > 0:  # checks if the page is a valid page
                        current_page = page
                    else:
                        print(f'Page {page} Not Found - Please Retry')
                case [item]:
                    item = int(item)

                    # checks if the item is a valid selection
                    if len(selections[current_page-1]) >= item > 0:
                        # returns the name of the item based on the page and the index of where it is on that page
                        return selections[current_page-1][item-1]
                    else:
                        print('Invalid Selection - Please Retry')
                case []:
                    return ''
                case _:
                    print('Invalid Input - Please Retry')

        except ValueError:  # checks for a value error
            print('Invalid Input Error- Please Retry')
