from typing import Final


class Colors:
    # rarities
    COMMON: Final = '\u001b[38;5;243m'
    UNCOMMON: Final = '\u001b[38;5;40m'
    RARE: Final = '\u001b[38;5;39m'
    EPIC: Final = '\u001b[38;5;129m'
    LEGENDARY: Final = '\u001b[38;5;220m'
    LEGENDARY_B: Final = '\u001b[38;5;220;1m'

    # extra colours
    OPTION: Final = '\u001b[38;5;81m'
    GREEN: Final = '\u001b[38;5;40;1m'
    WATER: Final = '\u001b[38;5;32m'

    # special formatting
    UNDERLINE: Final = '\033[4m'
    STRIKE: Final = '\033[9m'
    BOLD: Final = '\033[1m'

    # end of format declaration
    END: Final = '\033[0m'

    @staticmethod
    def fill(color, val: str | int) -> str:
        return f'{color}{str(val)}\033[0m'


class Items:
    # TODO: make colored text work with items *
    # TODO: add more to this, more functionality, stats, etc. *
    WEAPONS: Final = []
    ARMOR: Final = []
    ITEMS: Final = []


# TODO: functional enemy types ***
ENEMY_TYPES: Final = {'tutorial1': {'max_hp': 10.0, 'atk': 1.0, 'defense': 0,
                                    'speed': 1, 'crit_rate': 0, 'crit_damage': 0},
                      'tutorial2': {'max_hp': 20.0, 'atk': 3.0, 'defense': 1,
                                    'speed': 5, 'crit_rate': 5, 'crit_damage': 20},
                      'dummy': {'max_hp': 2**100, 'atk': 0.0, 'defense': 0,
                                'speed': 0, 'crit_rate': 0, 'crit_damage': 0}}
