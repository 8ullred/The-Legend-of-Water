class Colors:
    # rarities
    COMMON = '\u001b[38;5;243m'
    UNCOMMON = '\u001b[38;5;40m'
    RARE = '\u001b[38;5;21m'
    EPIC = '\u001b[38;5;129m'
    LEGENDARY = '\u001b[38;5;220m'
    LEGENDARY_B = '\u001b[38;5;220;1m'

    # extra colours
    GREEN = '\u001b[38;5;40;1m'
    WATER = '\u001b[38;5;32m'

    # special formatting
    UNDERLINE = '\033[4m'
    STRIKE = '\033[9m'
    BOLD = '\033[1m'

    # end of format declaration
    END = '\033[0m'


class Items:
    # TODO: make colored text work with items
    # TODO: add more to this, more functionality, stats, etc.
    WEAPONS = []
    ARMOR = []
    ITEMS = []


class Enemies:
    ENEMY_TYPES = ['tutorial1', 'tutorial2']
