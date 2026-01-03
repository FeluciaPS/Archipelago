# Data file for any items that can end up in Terry's inventory, like the Map.
# Archipelago-specific items such as "Breenklap Dig Spot" can be found in
# items_world.py.

from .base_ids import BASE_ID_ITEM_INVENTORY
from ..world import TTTTWorld


SHOP_HAT_NAMES = [
    "Diving Goggles",
    "Snow Hat",
    "Gato Hat",
    "Paper Hat",
    "Sun Hat",
    "Top Hat",
    "Crumpled Hat",
    "Sun Hat Green",
    "Derby Hat",
    "Racer Helmet",
    "Construction Hat",
    "Baseball Cap",
    "Sun Hat Pink",
    "Small Pointy Hat",
    "Cone Hat",
]

OTHER_HAT_NAMES = [
    "Sunglasses",
    "Government Hat 1",
    "Government Hat 2",
    "Government Hat 3",
    "Government Hat 4",
    "Sun Hat Blue",
    "Snekflat Glasses",
    "Bird Hat 1",
    "Bird Hat 2",
    "Bird Hat 3",
    "Bird Hat 4",
    "Familiar Shoe Hat",
    "Green Cap Hat",
    "Big Beard Hat",
    "Geometry Hat",
]

CONSUMABLE_ITEM_NAMES = [
    "Fries",
    "Bug Bun"
]

CRITTER_ITEM_NAMES = [
    "Cricket 1",
    "Cricket 2",
    "Cricket 3",
    "Cricket 4",
    "Cricket 5",
    "Cricket 6",
    "Cricket 7",
    "Cricket 8",
    "Cricket 9",
    "Cricket 10",

]

PET_ITEM_NAMES = [
    "Pet - Brass Duck",
    "Pet - Clyfax",
    "Pet - Honica",
    "Pet - Moletor",
    "Pet - Muscle Frog",
    "Pet - Kneft",
    "Pet - Gerelex",
]

PET_BLUEPRINT_ITEM_NAMES = [
    "Pet - Brass Duck (Blueprint)",
    "Pet - Clyfax (Blueprint)",
    "Pet - Honica (Blueprint)",
    "Pet - Moletor (Blueprint)",
    "Pet - Muscle Frog (Blueprint)",
    "Pet - Kneft (Blueprint)",
    "Pet - Gerelex (Blueprint)",
]

WEAPON_ITEM_NAMES = [
    "Toy Sword",
    "Toy Axe",
    "Wrench",
    "Baseball Bat",
    "Broken Pipe"
]

MISC_ITEM_NAMES = [
    "Shovel",
    "Bug Net",
    "Map",
    "Cell Phone",
    "Junk Finder Hat",
    "Turbo Upgrade",
    "Para Glider",
    "Government Document",
    "Terry Apartment Keys",
    "Sprankelwater Flag",
]

# Turbo Junk item names
TURBO_JUNK_ITEM_NAMES = [
    "Turbo Junk",               # 1 turbo junk
    "Buried Turbo Junk Bundle", # 5 turbo junk
    "Turbo Junk Bundle",        # 15 turbo junk
    "Turbo Junk Trash Can"      # 100 turbo junk
]

# Keeping money separately in case I want to do anything with it in the future
MONEY_ITEM_NAMES = [
    "Money"
]

MUSHROOM_CHIME_ITEM_NAMES = [
    "Mushroom Chime"
]

ALL_INVENTORY_ITEM_NAMES = [
    *SHOP_HAT_NAMES,
    *OTHER_HAT_NAMES,
    *CONSUMABLE_ITEM_NAMES,
    *CRITTER_ITEM_NAMES,
    *PET_ITEM_NAMES,
    *PET_BLUEPRINT_ITEM_NAMES,
    *WEAPON_ITEM_NAMES,
    *MISC_ITEM_NAMES,
    *TURBO_JUNK_ITEM_NAMES,
    *MONEY_ITEM_NAMES,
    *MUSHROOM_CHIME_ITEM_NAMES
]

BASE_ITEM_IDS = {
    "Toy Sword": 1,
    "Toy Axe": 2,
    "Wrench": 3,
    "Baseball Bat": 4,
    "Broken Pipe": 5,
    "Shovel": 6,
    "Bug Net": 7,
    "Map": 8,
    "Cell Phone": 9,
    "Junk Finder Hat": 10,
    "Sunglasses": 11,
    "Paper Hat": 12,
    "Sun Hat": 13,
    "Derby Hat": 14,
    "Top Hat": 15,
    "Diving Goggles": 16,
    "Racer Helmet": 17,
    "Snow Hat": 18,
    "Turbo Junk": 19,
    "Turbo Upgrade": 20,
    "Construction Hat": 21,
    "Para Glider": 22,
    "Money": 23,
    "Baseball Cap": 24,
    "Cone Hat": 25,
    "Fries": 26,
    "Cricket 1": 27,
    "Cricket 2": 28,
    "Cricket 3": 29,
    "Cricket 4": 30,
    "Cricket 5": 31,
    "Cricket 6": 32,
    "Cricket 7": 33,
    "Cricket 8": 34,
    "Cricket 9": 35,
    "Cricket 10": 36,
    "Pet - Muscle Frog": 37,
    "Pet - Brass Duck": 38,
    "Pet - Moletor": 39,
    "Pet - Honica": 40,
    "Pet - Clyfax": 41,
    "Pet - Kneft": 42,
    "Pet - Gerelex": 43,
    "Pet - Brass Duck (Blueprint)": 44,
    "Pet - Clyfax (Blueprint)": 45,
    "Pet - Honica (Blueprint)": 46,
    "Pet - Moletor (Blueprint)": 47,
    "Pet - Muscle Frog (Blueprint)": 48,
    "Pet - Kneft (Blueprint)": 49,
    "Pet - Gerelex (Blueprint)": 50,
    "Government Hat 1": 51,
    "Government Hat 2": 52,
    "Government Hat 3": 53,
    "Government Hat 4": 54,
    "Government Document": 55,
    "Mushroom Chime": 56,
    "Bug Bun": 57,
    "Snekflat Glasses": 58,
    "Crumpled Hat": 59,
    "Sun Hat Blue": 60,
    "Sun Hat Pink": 61,
    "Small Pointy Hat": 62,
    "Sun Hat Green": 63,
    "Terry Apartment Keys": 64,
    "Sprankelwater Flag": 65,
    "Bird Hat 1": 66,
    "Bird Hat 2": 67,
    "Bird Hat 3": 68,
    "Bird Hat 4": 69,
    "Gato Hat": 70,
    "Familiar Shoe Hat": 71,
    "Green Cap Hat": 72,
    "Big Beard Hat": 73,
    "Geometry Hat": 74,
    
    # Turbo junk items
    "Buried Turbo Junk Bundle": 75,
    "Turbo Junk Bundle": 76,
    "Turbo Junk Trash Can": 77,
}