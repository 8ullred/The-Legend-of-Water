from os import rename
from random import getrandbits, randint
from time import sleep

from constants import Colors, ENEMY_TYPES
from actions import print_bracket, get_username


# TODO: finish player class ***
class Player:
    def __init__(self, name: str):
        self.name = name

        # setting base stats for player
        self.atk = 999.0
        self.max_hp = 20.0
        self.hp = self.max_hp
        self.defense = 0
        self.crit_rate = 5
        self.crit_damage = 50
        self.speed = 5

        # setting statuses for player
        self.is_defending = False
        self.location = 'Dorma'

        # setting player balance
        self.gold, self.primoshard = 0, 0

    def balance(self):
        return ('gold', self.gold), ('primoshard', self.primoshard)

    def get_stats(self) -> tuple[float, tuple[float, float], int, int, int, int]:
        return self.atk, (self.hp, self.max_hp), self.defense, self.crit_rate, self.crit_damage, self.speed

    def __heal__(self):
        self.hp = self.max_hp
    # TODO: add item equipping **
    # TODO: add inventory *


# TODO: Enemy class ***
class Enemy:
    def __init__(self, name: str, enemy: dict):
        self.name = name

        self.max_hp = enemy['max_hp']
        self.hp = self.max_hp
        self.atk = enemy['atk']
        self.defense = enemy['defense']
        self.speed = enemy['speed']
        self.crit_rate = enemy['crit_rate']
        self.crit_damage = enemy['crit_damage']

        self.is_defending = False

    # TODO: enemy drops **


class NoPlayerName(Exception):
    pass


def intro():
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


def tutorial(reading_speed: int | float) -> Player:
    player = Player(get_username())

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

    return player


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


def menu(player: Player, save: str):
    print(f'You are currently in {player.location}')

    while True:
        print(f'{Colors.fill(Colors.OPTION, 1)} - Map\n'
              f'{Colors.fill(Colors.OPTION, 2)} - Town\n'
              f'{Colors.fill(Colors.OPTION, 3)} - Stats\n'
              f'{Colors.fill(Colors.OPTION, 4)} - Bag\n'
              f'{Colors.fill(Colors.OPTION, 5)} - Save\n'
              f'{Colors.fill(Colors.OPTION, "Q")} - Quit')

        print()
        # TODO: Error Trapping ***
        cmd = input('> ').lower()

        match cmd:
            case '1':
                pass
            case '2':
                pass
            case '3':
                open_stats(player)
            case '4':
                open_bag(player)
            case '5':
                rename(f'saves/{save}', f'saves/{player.name}.txt')
            case 'q':
                print("Thank You For Playing!")
                rename(f'saves/{save}', f'saves/{player.name}.txt')
                print('Your Progress Has Been Saved.')

                return
            case 'dev':
                pass
            case _:
                print('Invalid Command - Please Retry')


# TODO: map zones ****

# TODO: shop menu ***


def open_stats(player: Player):
    print('Stats:')
    # TODO: display all stats **
    for item in player.get_stats():
        # TODO: show current hp *
        print(f'\t{item = }')

    print()
    _ = input('Hit enter to return to the previous menu.')
    return


def open_bag(player: Player, *items):
    print('Balance:\n')
    [print(f'\t{item[0]}: {val}\n') for item, val in player.balance()]

    print('\nItems: ')
    print('\t', *items)

    print()
    _ = input('Hit enter to return to the previous menu.')
    return


# TODO: combat mechanics ***
# TODO: different coloured hit for crits *
def start_fight(player: Player, enemy: Enemy, is_tutorial: bool = False) -> bool:

    print(f'Starting fight between {player.name} and {enemy.name}\n')
    sleep(0.5)

    if player.speed > enemy.speed:
        print(f"You go first! Your speed is {player.speed}, is faster than {enemy.name}'s speed of {enemy.speed}")
        player_turn = True

    elif enemy.speed > player.speed:
        print("The opponent goes first! "
              f"Your speed of {player.speed} is slower than {enemy.name}'s speed of {enemy.speed}")
        player_turn = False

    else:
        print(f"{player.name}'s speed is the same as {enemy.name}'s speed. ", end='')
        sleep(0.5)
        print(f'By the randomness of surprise, ', end='')
        player_turn = bool(getrandbits(1))

        print(f'{player.name} is going first') if player_turn else print(f'{enemy.name} is going first')

    print()
    sleep(1.5)

    while True:
        if player_turn:
            print_health(player, enemy)

            print(f'{Colors.UNDERLINE}Your Turn{Colors.END}')
            sleep(0.65)

            if is_tutorial:
                while True:
                    print('Actions:\n'
                          f'\t{Colors.OPTION}1{Colors.END} Attack\n'
                          f'\t{Colors.OPTION}2{Colors.END} Defend')
                    sleep(0.5)

                    # TODO: Error Trapping
                    try:
                        action = int(input('Enter action: '))
                        if action not in [1, 2]:
                            print("Please Enter 1 or 2")
                        else:
                            break
                    except ValueError:
                        print("Invalid Input - Please Retry")

            else:
                print('Actions:\n'
                      f'\t{Colors.OPTION}1{Colors.END} Attack\n'
                      f'\t{Colors.OPTION}2{Colors.END} Defend\n'
                      f'\t{Colors.OPTION}3{Colors.END} Use Item\n'
                      f'\t{Colors.OPTION}4{Colors.END} Run')
                sleep(0.5)

                # TODO: Error Trapping
                action = int(input('Enter action: '))

            sleep(1)
            match action:
                case 1:
                    attack(player, enemy)
                case 2:
                    defend(player)
            sleep(1)

        else:
            print(f"{Colors.UNDERLINE}{enemy.name}'s Turn{Colors.END}")
            sleep(1)

            attack(enemy, player)
            sleep(1)

        if enemy.hp <= 0:
            print(f'Congratulations! You Defeated {enemy.name}!')
            return True

        if player.hp <= 0:
            print('You lost')
            return False

        player_turn = not player_turn


def print_health(player: Player, enemy: Enemy):
    print(f'You: {player.hp}/{player.max_hp} HP')
    print(f'{enemy.name}: {enemy.hp}/{enemy.max_hp} HP')
    print()
    sleep(1.5)


def attack(attacker: Player | Enemy, defender: Player | Enemy):
    crit_roll = randint(1, 100)

    do_crit = True if attacker.crit_rate >= crit_roll else False

    # TODO: adjust sleeps for time spacing *

    damage_dealt = (attacker.atk * ((attacker.crit_damage / 100) + 1)) if do_crit \
        else attacker.atk - (defender.defense * 0.5)

    # TODO: better relay of information *

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
            defender.hp = defender.hp - damage_dealt
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

        if damage_dealt <= 0:
            print(f"{defender.name}'s defense was too strong! ", end='')
            sleep(1.5)
            print(f"{attacker.name}'s attack did nothing!\n")

        else:
            defender.hp = defender.hp - damage_dealt
            if defender.hp < 0: defender.hp = 0

            print(f'{attacker.name} landed a hit that did {damage_dealt} damage! ', end='')
            sleep(1.5)
            print(f'{defender.name} has {defender.hp} HP remaining!\n')


def defend(defender: Player):
    print(f'{defender.name} is going to block!\n')

    defender.is_defending = True


# TODO: use item in combat ***
def use_items():
    pass

# TODO: run combat feature **
