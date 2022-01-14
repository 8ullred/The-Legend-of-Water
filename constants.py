from __future__ import annotations

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
    HP: Final = '\u001b[38;5;1m'
    DEF: Final = '\u001b[38;5;10m'
    ATK: Final = '\u001b[38;5;11m'
    CRIT: Final = '\u001b[38;5;32m'
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
    def fill(color: 'Colors', text: str | int) -> str:
        return f'{color}{str(text)}{Colors.END}'


class Items:
    # TODO: make colored text work with items *
    # TODO: change rarity to the name color constant

    # TODO: add more to this, more functionality, stats, etc. *

    # types: weapon, armor, consumable, material, special
    # rarities: common: 1, uncommon: 2, rare: 3, epic: 4, legendary: 5

    # standard weapon 'name': ('description', 'rarity', 'atk', 'hp', 'cd', 'cr', 'spd', 'type')
    # TODO: balance crit (after finishing game) *
    WEAPONS: Final = {
        "Training Sword": {"description": "A handy sword that's light and balanced. Through it, can your dreams become "
                                          "reality.",
                           "rarity": Colors.COMMON, "atk": 2, "hp": 0, "cd": 0, "cr": 0, "spd": 0,
                           "type": "weapon"},

        "Bronze Sword": {"description": "A well rounded weapon that will keep you alive in tough situations.",
                         "rarity": Colors.UNCOMMON, "atk": 5, "hp": 0, "cd": 0, "cr": 0, "spd": 0,
                         "type": "weapon"},

        "Iron Sword": {"description": "A strong weapon with a heavy hit. Take it up, and your strike will become slower"
                       " but stronger.", "rarity": Colors.RARE,
                       "atk": 6, "hp": 0, "cd": 30, "cr": -2, "spd": -1, "type": "weapon"},

        "Heroic Blade": {"description": "A weapon revered in legends, only to be wielded by those with true "
                         "ambition and power.", "rarity": Colors.EPIC,
                         "atk": 8, "hp": 5, "cd": 25, "cr": 15, "spd": 3, "type": "weapon"},

        "Dev's Scythe": {"description": "A scythe forged from dying stars, and whoever wields it can cause "
                         "explosions far more powerful than any mortal could... truly a weapon fit for the gods.",
                         "rarity": Colors.LEGENDARY_B,
                         "atk": 99999, "hp": 0, "cd": 99999, "cr": 100, "spd": 0, "type": "weapon"}
    }

    # standard armor 'name': ('description', 'rarity', 'atk', 'hp', 'def', 'cd', 'cr', 'spd', 'type')
    ARMOR: Final = {
        "Leather Tunic": {"description": "A fine set of leather, worn over your standard clothes. "
                          "Will turn away weak strikes.", "rarity": Colors.COMMON,
                          "atk": 0, "hp": 0, "def": 1, "cd": 0, "cr": 0, "spd": 0, "type": "armor"},

        "Chain-Linked Armor": {"description": "A great armor piece, forged by Smith. It will protect you well.",
                               "rarity": Colors.UNCOMMON,
                               "atk": 0, "hp": 0, "def": 3, "cd": 0, "cr": 0, "spd": 0, "type": "armor"},

        "Steel Plate": {"description": "A solid piece of armor that will keep you protected, at the cost of your "
                        "mobility.", "rarity": Colors.RARE,
                        "atk": 0, "hp": 2, "def": 5, "cd": 0, "cr": 0, "spd": -2, "type": "armor"},

        "Conqueror's Guard": {"description": "The chestplate of an ancient hero of old, one that has seen many "
                              "battles but has never wavered.", "rarity": Colors.EPIC,
                              "atk": 2, "hp": 8, "def": 8, "cd": 0, "cr": 5, "spd": 2, "type": "armor"},

        "Star-Woven Cloak": {"description": "A cloak that shimmers with the pattern of the galaxy, flinging all attacks"
                             " away to a distant land... Such is the power of the gods", "rarity": Colors.LEGENDARY_B,
                             "atk": 0, "hp": 99999, "def": 99999, "cd": 0, "cr": 0, "spd": 99999, "type": "armor"},
    }

    # TODO: add rarities for consumables
    # normal items 'name': ('description', 'rarity', 'effect', 'amount', 'type'
    CONSUMABLE: Final = {
        "Filtered Water": {"Water that tastes the same as Tap Water, but is slightly healthier.", 2,
                           "heal", 5, "consumable"},

        "Holy Water": {"Water that has been purified with magic. Has superior healing qualities.", 3,
                       "heal", 15, "consumable"},
    }

    OTHER: Final = {}


# TODO: functional enemy types ***
ENEMY_TYPES: Final = {
    'tutorial1': {'max_hp': 5, 'atk': 1, 'defense': 0,
                  'speed': 100, 'crit_rate': 0, 'crit_damage': 0},

    'tutorial2': {'max_hp': 10, 'atk': 3, 'defense': 1,
                  'speed': 100, 'crit_rate': 5, 'crit_damage': 20},

    'dummy': {'max_hp': 2 ** 100, 'atk': 0, 'defense': 0,
              'speed': 0, 'crit_rate': 0, 'crit_damage': 0}
}
