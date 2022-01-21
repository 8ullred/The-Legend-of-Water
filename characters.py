import pickle as pk
from math import floor
from os import listdir, rename, path, PathLike
from random import getrandbits, randint
from time import sleep

from actions import print_bracket, get_username, selection_menu
from constants import Colors, ENEMY_TYPES, Items


class Player:  # defining the player class

    def __init__(self, name: str) -> None:  # making the function return None
        self.name = name

        # setting stats for player
        self.max_hp = 15
        self.hp = self.max_hp
        self.defense = 0
        self.atk = 999
        self.crit_rate = 5
        self.crit_damage = 50
        self.speed = 100  # scale by ~5

        # setting player balance
        self.gold, self.primoshard = 0, 0

        # setting player location
        self.location = 'Dorma'

        # setting statuses for player
        self.is_defending = False

        # players items, stored in form of 'item_name': ('amount', 'type')
        self.items = {"Dev's Scythe": (1, 'weapon'), "Star-Woven Cloak": (1, 'armor')}

    def balance(self) -> tuple[tuple[str, int], tuple[str, int]]:
        """
        Returns the players balance

        :return:
            Returns the name of the currency then the amount for each currency
        """
        return ('gold', self.gold), ('primoshard', self.primoshard)

    def stats(self) -> None:
        """
        Prints out the players stats and equipped gear.
        """

        # printing the stats for the player to view
        print(f'{Colors.fill(Colors.HP, f"{self.hp}/{self.max_hp}❤ HP")}\n'
              '----------\n'
              f'{Colors.fill(Colors.DEF, f"{self.defense}✥ DEF")} \n'
              f'{Colors.fill(Colors.ATK, f"{self.atk}⚔ ATK")}\n'
              f'{Colors.fill(Colors.CRIT, f"{self.crit_rate}☣ CR")}\n'
              f'{Colors.fill(Colors.CRIT, f"{self.crit_damage}☠ CD")}\n'
              f'{self.speed}✦ SPD\n')
        _ = input('Hit enter to return to the previous menu.')
        return  # leaves the function

    def inventory(self) -> None:
        """
        Prints out the player's inventory with a selection menu. Player can then choose can choose an item to print
        information about it. The player then may press enter to return to the inventory menu. If the player wishes
        to quit, they may leave the selection blank to quit the menu.
        """

        selection = ' '
        while selection:

            # saves the selection made
            selection = selection_menu(list(self.items.keys()), 'Items')

            print_description(selection, self)

            if selection:
                _ = input('Hit enter to return to the previous menu')

    def update_items(self, values: list[tuple[str, tuple[int, str]]]) -> None:
        """
        Updates the players items.

        :param values:
            A list of tuples containing the name of the item, the amount and which type.
        """

        for item, (count, type_) in values:  # loops through each item

            if item in self.items:  # checks if item already exists
                self.items[item] += count  # adds number of items to current count
            else:
                self.items[item] = (count, type_)  # creates new entry

    def heal(self, amount: float = 1) -> None:
        """
        Heals the player for a percentage of the player's max hp.

        :param amount:
            the percentage of which the player is healed
        """

        self.hp += floor(self.max_hp * amount)
        if self.hp > self.max_hp: self.hp = self.max_hp


class Enemy:
    def __init__(self, name: str, enemy: ENEMY_TYPES) -> None:
        self.name = name

        self.max_hp = enemy['max_hp']
        self.hp = self.max_hp
        self.atk = enemy['atk']
        self.defense = enemy['defense']
        self.crit_rate = enemy['crit_rate']
        self.crit_damage = enemy['crit_damage']
        self.speed = enemy['speed']

        self.is_defending = False


class NoPlayerName(Exception):
    # custom exception
    pass


# intro, tutorial, read
def intro(story_file: str | PathLike[str]) -> float:
    """
    Starts the introduction to the game. Prints out the story line of the game. Asks user if they want to speed up the
    introduction.

    :return:
        Returns the reading speed
    """

    # introduction to game
    reading_speed = None

    while reading_speed is None:
        # matches the input to the cases and sets the reading speed
        match input('Would you like to speed up the intro (y/n)? '):
            case 'y' | 'Y':
                reading_speed = 0.01
            case 'n' | 'N':
                reading_speed = 0.08
            case '¥':
                reading_speed = 0
            case _:  # wildcard case for an invalid input
                print('Invalid Input - Please Retry\n')

    print('\n' * 10)  # spacing
    sleep(1)
    read_story(story_file, 'startIntro', 'Introduction: ', reading_speed)  # reads the introduction from the lore text

    return reading_speed


def tutorial(story_file: str | PathLike[str], reading_speed: int | float) -> Player:
    """
    Starts the tutorial phase of the game, introduction to fighting mechanics and creating the Player class.

    :param story_file:
        The file which the story is going to be read from
    :param reading_speed:
        Speed at which the story will be played at
    :return:
        Returns the newly created player class
    """

    player = Player(get_username())  # creates a Player class with the selected username

    # reads out the story
    print()
    print_bracket(1)

    read_story(story_file, 'startBattle1', reading_rate=reading_speed)
    print('\n')

    # creates an enemy then starts a battle
    while not start_fight(player, Enemy('Reeco', ENEMY_TYPES['tutorial1']), True):
        print('You Lost! Try again.\n')
        player.heal()

    read_story(story_file, 'endBattle1', reading_rate=reading_speed, player=player)

    print()
    print_bracket(2)

    read_story(story_file, 'startBattle2', reading_rate=reading_speed)
    print('\n')

    # creates an enemy then starts a battle
    while not start_fight(player, Enemy('Kasra', ENEMY_TYPES['tutorial2']), True):
        print('You Lost! Try again.\n')
        player.heal()

    read_story(story_file, 'endBattle2', reading_rate=reading_speed)
    print('\n')

    read_story(story_file, 'conclusion', reading_rate=reading_speed, player=player)

    print('\n')  # formatting
    print(f'Welcome to {Colors.WATER}The Legend of Water{Colors.END}')

    # heals the player and adds items and currency
    player.heal()
    player.update_items([('Bronze Sword', (1, 'weapon')), ('Filtered Water', (1, 'consumable')),
                         ('Holy Water', (1, 'consumable')), ('Childhood Photo', (1, 'special'))])
    player.gold += 50
    player.primoshard += 100

    return player


def read_story(text_file: str | PathLike[str], scene: str,
               header: str = None, reading_rate: float = 0.08, player: Player = None) -> None:
    """
    Reads from the lore text. Has custom indicators for showing line breaks and when to end. Reads through the lore
    and starts printing when it meets the --scene: scene line. Can print a header for the text, default is no
    headerReads at a default speed of 0.08 but can be changed. Optional parameter for a player in case the user's
    name is used in a dialogue.

    :param text_file:
        The file which is going to be read from
    :param scene:
        The name of the scene to start reading at
    :param header:
        Optional parameter for the header of the dialogue
    :param reading_rate:
        Optional parameter of the rate of which the dialogue is being read at
    :param player:
        Optional parameter for when the statistics of a player may be used in a dialogue
    """

    start_reading = False

    if header is not None:
        # prints the header if a header is added
        for char in header:
            # prints out each character individually
            print(char, end='')
            sleep(reading_rate * 8) if char == ':' else sleep(reading_rate)
        else:
            print()

    try:
        # opens the lore text file and starts searching for the starting scene
        with open(text_file, 'r') as file:
            for line in file:
                # cleans up the code for readability by the program
                if line != '\n':
                    line = line.strip('\n')

                if start_reading:
                    # checks for special cases such as ending the current
                    if line == '--end':
                        return
                    elif line == '--lineBreak':
                        print()
                    else:
                        check_for_code, pattern_matched = False, False

                        for char in line:  # loops through every character in a line
                            match char:
                                # adjusts the delay based on the character
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
                                # cases for special actions such as a players name or custom colors for text
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

                                sleep_time, check_for_code = 0, False  # resets the checking

                            # prints the character and sleeps for a certain amount of time
                            print(char, end='')
                            sleep(sleep_time)

                else:
                    # looks for the selected scene
                    if line.split() == ['--scene:', scene]:
                        start_reading = True

        print('No Scene Found')

    except NoPlayerName:  # looks for an error
        print('No Player Was Passed - This Scene Requires the Name of a Player')


def menu(player: Player, current_save: str | PathLike[str]) -> None:
    """
    Main menu for the game. The player can choose different actions or quit the game.

    :param player:
        The player
    :param current_save:
        The current save that this instance of the game is playing on
    """

    print(f'You are currently in {player.location}')

    cmd = str()
    while cmd != 'q':
        print(f'{Colors.fill(Colors.OPTION, 1)} - Map\n'
              f'{Colors.fill(Colors.OPTION, 2)} - Town\n'
              f'{Colors.fill(Colors.OPTION, 3)} - Stats\n'
              f'{Colors.fill(Colors.OPTION, 4)} - Bag\n'
              f'{Colors.fill(Colors.OPTION, 5)} - Save\n'
              f'{Colors.fill(Colors.OPTION, "Q")} - Quit\n')

        cmd = input('> ').lower()

        match cmd:
            case '1':
                pass
            case '2':
                pass
            case '3':
                player.stats()
            case '4':
                player.inventory()
            case '5':
                save_progress(current_save, player)
            case 'q':
                print("Thank You For Playing!")
                save_progress(current_save, player)
            case invalid:
                print(f'Invalid Command [{invalid}] - Please Retry')


def print_description(item: str, player: Player) -> None:
    """
    Takes in the name of the item and a player. Will print out the items name, stats, and description.

    :param item:
        The name of the item which will have its stats and description printed out.
    :param player:
        The player.
    """

    if item != '':  # checks if there is an item.
        match player.items[item][1]:  # matches the items type

            # prints out different information about the item based on its type
            case 'weapon':
                item_name, info = item, Items.WEAPONS[item]

                print(f'\n{Colors.fill(info["rarity"], item_name)} - {info["type"].title()}\n')

                print(f'{info["atk"]:+} ATK\n'
                      f'{info["hp"]:+} Max HP\n'
                      f'{info["cd"]:+} CD\n'
                      f'{info["cr"]:+} CR\n'
                      f'{info["spd"]:+} SPD\n')

                print(f'Description: {info["description"]}\n')

            case 'armor':
                item_name, info = item, Items.ARMOR[item]

                print(f'\n{Colors.fill(info["rarity"], item_name)} - {info["type"].title()}\n')

                print(f'{info["hp"]:+} Max HP\n'
                      f'{info["def"]:+} DEF\n'
                      f'{info["atk"]:+} ATK\n'
                      f'{info["cd"]:+} CD\n'
                      f'{info["cr"]:+} CR\n'
                      f'{info["spd"]:+} SPD\n')

                print(f'Description: {info["description"]}\n')

            case 'consumable':
                selection = item, Items.CONSUMABLE[item]

                print(f'{selection[1]["type"].title()} - {selection[0].title()}\n')
            case _:
                selection = item, Items.OTHER[item]

                print(f'{selection[1]["type"].title()} - {selection[0].title()}\n')


def start_fight(player: Player, enemy: Enemy, is_tutorial: bool = False) -> bool:  # starting a fight
    """
    Starts a fight sequence with the player and an enemy. Will calculate who goes first based on the speed. On the
    player's turn, they will be able to make different choices. When in tutorial mode, only attack and defend will be
    allowed, in normal mode, the player may also choose to use items or run. When a choice is made, the appropriate
    function will be called then execute. The function will then check the fighter's health and return an appropriate
    boolean based on who won.

    :param player:
        The player.
    :param enemy:
        The enemy.
    :param is_tutorial:
        Conditional argument for if the battle is a tutorial. If so, options will be limited to attack and defend
    :return:
        Returns a bool based on who wins the fight. True if the play wins, False if they lose. In case of a tie, the
        player will receive the win.
    """

    print(f'Starting fight between {player.name} and {enemy.name}\n')
    sleep(0.5)

    # calculates the first move based on the fighter's speed
    if player.speed > enemy.speed:
        print(f"You go first! Your speed is {player.speed}, is faster than {enemy.name}'s speed of {enemy.speed}")
        player_turn = True

    elif enemy.speed > player.speed:
        print("The opponent goes first! "
              f"Your speed of {player.speed} is slower than {enemy.name}'s speed of {enemy.speed}")
        player_turn = False

    else:
        # generates a random speed in case of a tie
        print(f"{player.name}'s speed is the same as {enemy.name}'s speed. ", end='')
        sleep(0.5)
        print(f'By the randomness of surprise, ', end='')
        player_turn = bool(getrandbits(1))

        print(f'{player.name} is going first') if player_turn else print(f'{enemy.name} is going first')

    print()
    sleep(1.5)

    while player.hp > 0 and enemy.hp > 0:
        if player_turn:  # printing out the player's choices in battle
            print_health(player, enemy)

            print(f'{Colors.UNDERLINE}Your Turn{Colors.END}')
            sleep(0.65)

            action = 0
            if is_tutorial:  # changing the battle system for tutorial only
                while not 0 < action < 3:
                    print('Actions:\n'
                          f'\t{Colors.OPTION}1{Colors.END} Attack\n'
                          f'\t{Colors.OPTION}2{Colors.END} Defend')
                    sleep(0.5)

                    try:
                        action = int(input('Enter action: '))
                        if action < 1 or action > 2:
                            print("Please Enter 1 or 2")
                    except ValueError:
                        print("Invalid Input - Please Retry")

            else:
                while not 0 < action < 5:  # actual battle choices
                    print('Actions:\n'
                          f'\t{Colors.OPTION}1{Colors.END} Attack\n'
                          f'\t{Colors.OPTION}2{Colors.END} Defend\n'
                          f'\t{Colors.OPTION}3{Colors.END} Use Item\n'
                          f'\t{Colors.OPTION}4{Colors.END} Run')
                    sleep(0.5)

                    try:
                        action = int(input('Enter action: '))
                        if action < 1 or action > 2:
                            print("Invalid Choice")
                    except ValueError:
                        print("Invalid Input - Please Retry")

            sleep(1)
            match action:  # choosing the action to go through
                case 1:
                    attack(player, enemy)
                case 2:
                    defend(player)
                case 3:
                    pass  # call use item function
                case 4:
                    pass  # call run function
            sleep(1)

        else:
            # prints out enemy's turn
            print(f"{Colors.UNDERLINE}{enemy.name}'s Turn{Colors.END}")
            sleep(1)

            attack(enemy, player)
            sleep(1)

        player_turn = not player_turn  # swaps the players turn\

    else:
        # case if you win
        if enemy.hp <= 0:
            print(f'Congratulations! You Defeated {enemy.name}!')
            return True

        # case if you lose
        if player.hp <= 0:
            print('You lost')
            return False


def print_health(player: Player, enemy: Enemy) -> None:
    """
    Prints the health of the player and enemy

    :param player:
        The player
    :param enemy:
        The enemy that the player is fighting
    """

    print(f'You: {player.hp}/{player.max_hp} HP')
    print(f'{enemy.name}: {enemy.hp}/{enemy.max_hp} HP')
    print()
    sleep(1.5)


def attack(attacker: Player | Enemy, defender: Player | Enemy) -> None:
    crit_roll = randint(1, 100)  # generates a number

    do_crit = True if attacker.crit_rate >= crit_roll else False  # calculates if attack should crit based on the roll

    damage_dealt = (attacker.atk * ((attacker.crit_damage / 100) + 1)) if do_crit \
        else (attacker.atk - (defender.defense * 0.5))  # calculates the amount of damage dealt

    # checks if defender is defending
    if defender.is_defending:
        print(f'{defender.name} blocked!')
        sleep(1.5)

        # reduces damage by half
        damage_dealt *= 0.5

        if do_crit:
            print(f'{attacker.name} landed a critical strike!\n')
            sleep(0.5)

        # checks for no damage dealt
        if damage_dealt <= 0:
            print(f"{attacker.name}'s attack did no damage!\n")

        else:
            defender.hp -= damage_dealt
            if defender.hp < 0: defender.hp = 0  # checks if defender hp is lower than 0 and corrects it

            # prints out information
            print(f'{defender.name} blocked for {attacker.atk - damage_dealt} damage ')
            sleep(1)
            print(f'{defender.name} took {damage_dealt} damage instead!')
            sleep(1)
            print(f'{defender.name} has {defender.hp} HP remaining!\n')

        defender.is_defending = False

    else:  # not defending
        if do_crit:
            print(f'{attacker.name} landed a critical strike!\n')
            sleep(0.5)

        # checks for no damage dealt
        if damage_dealt <= 0:
            print(f"{defender.name}'s defense was too strong! ", end='')
            sleep(1.5)
            print(f"{attacker.name}'s attack did nothing!\n")

        else:
            defender.hp -= damage_dealt
            if defender.hp < 0: defender.hp = 0

            print(f'{attacker.name} landed a hit that did {damage_dealt} damage! ', end='')
            sleep(1.5)
            print(f'{defender.name} has {defender.hp} HP remaining!\n')


def defend(defender: Player) -> None:
    """
    Sets the player's defending status to True and tells the user they are defending

    :param defender:
        the player that is going to defend
    """

    print(f'{defender.name} is going to block!\n')
    defender.is_defending = True


def load_save() -> tuple[str, Player | None]:
    """
    Looks up all save files and asks user to choose one. Reads the file and loads the Player class
    which is stored inside. If the class exists, it will be saved then returned, otherwise, None will be saved instead

    :return:
        returns the name of the selected save and the Player class or None as a tuple
    """

    # gets all save files
    save_files = listdir('saves')

    selection = 0
    while not 0 < selection < 4:
        # prints the name of the saves
        print('Saves: ')
        for i, file in enumerate(save_files):
            print(f'\t{i + 1} {file.strip(".txt")}')
        try:
            selection = int(input('Choose Save: '))  # ask user for their selection

            if not 0 < selection < 4:
                print('Invalid Selection - Please Retry')

        except ValueError:  # checks for a value error
            print('Invalid Input - Please Retry')

    else:
        selected_save = save_files[selection - 1]

        try:
            # opens the selected file
            with open(f'saves/{selected_save}', 'rb') as save_file:
                player = pk.load(save_file)  # loads the Player class from the file
        except EOFError:  # checks for an end of file error
            player = None

        return selected_save, player  # returns the name of the save and the Player class


def save_progress(file_name: str | PathLike[str], player: Player) -> None:
    """
    Receives a file and a Player class. Opens the file and saves the player class inside. Then renames the file to the
    name of the player.

    :param file_name:
        Name of the file that is going to be opened
    :param player:
        Player class which is to be saved
    """

    # opens the file
    with open(f'saves/{file_name}', 'wb') as save_file:
        pk.dump(player, save_file)  # saves the info

    # renames the file to the player's name
    while path.exists(f'saves/{player.name}.txt') and player.name != file_name.strip('.txt'):
        print('There is already a save file with that username. Please change your name.')
        player.name = get_username('Enter New Username: ')

    else:
        rename(f'saves/{file_name}', f'saves/{player.name}.txt')
        print('Your Progress Has Been Saved.')
