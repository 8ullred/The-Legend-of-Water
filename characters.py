from random import getrandbits
from time import sleep
from constants import Colors, Enemies


# TODO: finish player class
class Player:
    def __init__(self, name: str):
        self.name = name

        # setting base stats for player
        self.atk = 5.0
        self.max_hp = 20.0
        self.hp = self.max_hp
        self.defense = 0
        self.crit_rate = 5
        self.crit_damage = 50
        self.speed = 5

        # setting statuses for player
        self.is_defending = False

        # setting player balance
        self.currency, self.special_currency = 0, 0

    def update_balance(self, currency=0, special_currency=0, add=True):
        if not add:
            currency *= -1
            special_currency *= -1

        self.currency += currency
        self.special_currency += special_currency

    def balance(self):
        return ('currency', self.currency), ('special_currency', self.special_currency)

    def stats(self):
        return self.atk, self.hp, self.defense, self.crit_rate, self.crit_damage, self.speed

    # TODO: add item equipping
    # TODO: add inventory


# TODO: Enemy class
class Enemy:
    # TODO: being able to have different enemy types with individual stats
    def __init__(self, name):
        self.name = name

        self.max_hp = 10.0
        self.hp = self.max_hp
        self.atk = 1.0
        self.defense = 0
        self.speed = 0

        self.is_defending = False

    def attack(self):
        pass

    # TODO: enemy drops


def menu(player):
    while True:
        print('1 - Battle\n'
              '2 - Town\n'
              '3 - Stats\n'
              '4 - Bag\n'
              '5 - Save\n'
              r"'Q' - Quit")

        print()
        # TODO: Error Trapping
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
                # TODO: save functionality
                pass
            case 'q':
                print("Thank you!")
                return
            case 'dev':
                pass
            case _:
                print('Invalid Command - Please Retry')


# TODO:...


def open_stats(player: Player):
    print('Stats:')
    # TODO: display all stats
    for item in player.stats():
        # TODO: show current hp
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


# TODO: combat mechanics

def attack(attacker: Player | Enemy, defender: Player | Enemy):
    # TODO: add sleeps for time spacing

    damage_dealt = attacker.atk - (defender.defense * 0.5)

    if defender.is_defending:
        print(f'{defender.name} blocked!\n')
        sleep(1.5)

        damage_dealt *= 0.5

        if damage_dealt <= 0:
            print(f"{attacker.name}'s attack did no damage!")

        else:
            defender.hp = defender.hp - damage_dealt
            print(f'{defender.name} blocked for {attacker.atk - damage_dealt} damage ')
            sleep(2)
            print(f'{defender.name} took {damage_dealt} damage instead!')
            sleep(2)
            print(f'{defender.name} has {defender.hp} HP remaining!')

        defender.is_defending = False

    else:
        if damage_dealt < 0:
            print(f"{defender.name}'s defense was too strong! ", end='')
            sleep(1.5)
            print(f"{attacker.name}'s attack did nothing!")

        else:
            defender.hp = defender.hp - damage_dealt
            print(f'{attacker.name} landed a hit that did {damage_dealt} damage! ', end='')
            sleep(1.5)
            print(f'{defender.name} has {defender.hp} HP remaining!')


def defend(defender: Player):
    print(f'{defender.name} is going to block!')
    sleep(1.5)

    defender.is_defending = True

# TODO: use item in combat
# TODO: run combat feature


def use_items():
    pass


def start_fight(player: Player, enemy: Enemy, is_tutorial: bool = False) -> bool:
    # TODO: add sleeps for time spacing

    def print_health():
        print(f'You: {player.hp}/{player.max_hp} HP')
        print(f'{enemy.name}: {enemy.hp}/{enemy.max_hp} HP')
        print()
        sleep(1.5)

    if is_tutorial:
        if player.speed > enemy.speed:
            player_turn = True
        elif enemy.speed > player.speed:
            player_turn = False
        else:
            player_turn = bool(getrandbits(1))

        print(f'Starting fight between {player.name} and {enemy.name}\n')
        sleep(1.5)

        while True:
            if player_turn:
                print_health()

                print(f'{Colors.UNDERLINE}Your Turn{Colors.END}')
                sleep(2)

                print('Actions:\n'
                      '\t1 Attack\n'
                      '\t2 Defend\n'
                      '\t3 Use Items (WIP)')
                sleep(0.5)

                # TODO: Error Trapping
                action = int(input('Enter action: '))

                sleep(2)
                match action:
                    case 1:
                        attack(player, enemy)
                    case 2:
                        defend(player)
                    case 3:
                        pass
                        # TODO: use items
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

# TODO: shop menu
# TODO: map zones
