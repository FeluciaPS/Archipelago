

from BaseClasses import Item, ItemClassification

# Planned items for version 1:
# - Progressive Cup Unlock
#
# Planned items for future:
# - Specific Cup Unlocks (yaml)
# - Character Unlocks
# - Spoiler/Kart/Hat Unlocks
# - Time Trial Unlocks/Specific Course Unlocks
# - Puzzle Pieces
# - I'm sure I've forgotten some

# Setting up a lot of the potential items we'll need to deal with in the future
# even if they don't necessarily need to exist for the v0.1 
# Leaving room between ID groups to be able to extend them later and just for
# clarity.
#
# The first ID (000, 100, 150) in every group is reserved for a progressive
# unlock item, even if one doesn't exist
#
# There's an argument to be made for fully writing out the item lists instead
# of generating a bunch of them with for loops for easy ID lookup, but 
# right now this is a whole lot easier on me.

# This might not be the best place to put a race names list, I suspect
# we may be re-using this in other files.
RACE_NAMES = [
    "City Slicker",
    "Mally Market",
    "Play Misty For Me",
    "Prohibited Site",
    "Catz In The Hood",
    "Spooky Manor",
    "Pastacosi Factory",
    "Caskou Park",
    "Palerock Lake",
    "Country Bumpkin",
    "Sneak-A-Peak",
    "Loopy Lagoon",
    "Crazy Dunes",
    "Valley Of The Kings",
    "Blazing Oasis",
    "Mysterious Temple"
]


# Puzzle pieces reserve IDs 0-100. 
# They're named by race name and numbered 1-3
PUZZLE_PIECE_TABLE = {}

index = 1
for race in RACE_NAMES:
    for n in range(3):
        name = f'{race} - Puzzle Piece {n}'
        PUZZLE_PIECE_TABLE[name] = index
        index += 1


# Course items reserve IDs 100-150.
COURSE_ITEM_TABLE = {
    "Progressive Course Unlock": 100
}

index = 101
for race in RACE_NAMES:
    name = f'Course Unlock - {race}'
    COURSE_ITEM_TABLE[name] = index
    index += 1


# Time trial items reserve IDs 150-200.
TIME_TRIAL_ITEM_TABLE = {
    "Progressive Time Trial Unlock": 150
}

index = 151
for race in RACE_NAMES:
    name = f'Time Trial Unlock - {race}'
    TIME_TRIAL_ITEM_TABLE[name] = index
    index += 1


# Cup items reserve IDs 200-250.
CUP_ITEM_TABLE = {
    "Progressive Cup Unlock": 200,
    "Cup Unlock - Lasagna": 201,
    "Cup Unlock - Pizza": 202,
    "Cup Unlock - Burger": 203,
    "Cup Unlock - Ice Cream": 204
}


# Character items reserve IDs 300-325
CHARACTER_ITEM_TABLE = {
    "Garfield": 301,
    "Jon": 302,
    "Liz": 303,
    "Odie": 304, 
    "Arlene": 305,
    "Nermal": 306,
    "Squeak": 307,
    "Harry": 308
}


# Car items reserve IDs 325-350
CAR_ITEM_TABLE = {
    "Formula Zzzz": 326,
    "Abstract-Kart": 327,
    "Medi-Kart": 328,
    "Woof-Mobile": 329,
    "Kissy-Kart": 330,
    "Cutie-Pie Cat": 331,
    "Rat-Racer": 332,
    "Muck-Madness": 333
}


# Hat items reserve IDs 400-500
HAT_LIST = [
    "Beddy-Bye Cap",
    "Whizzy Wizard",
    "Tic-Toque",
    "Elasto-Hat",
    "Chef's Special",
    "Cutie-Pie Crown",
    "Viking Helmet",
    "Stink-O-Rama",

    # Unique character hats
    "Space Bubble", # Garfield
    "Pizzaiolo Hat", # Jon
    "Bunny Band", # Liz
    "Joe Montagna", # Odie
    "Aristo-Catic Bicorn", # Arlene
    "Toutankhameow", # Nermal
    "Apprentice Sorcerer", # Squeak
    "Mule Head" # Harry
]

HAT_ITEM_TABLE = {}
index = 401
for hat in HAT_LIST:
    HAT_ITEM_TABLE[f'Progressive {hat}'] = index
    HAT_ITEM_TABLE[f'{hat} - Bronze'] = index + 25
    HAT_ITEM_TABLE[f'{hat} - Silver'] = index + 50
    HAT_ITEM_TABLE[f'{hat} - Gold'] = index + 75
    index += 1

# Spoiler items reserve IDs 500-600
SPOILER_LIST = [
    "Bombastic Spoiler",
    "Whacky Spoiler",
    "Superfit Spoiler",
    "Cyclobone Spoiler",
    "Foxy Spoiler",
    "Shimmering Spoiler",
    "Holey Moley Spoiler",
    "Stained Spoiler"
]

SPOILER_ITEM_TABLE = {}
index = 501
for spoiler in SPOILER_LIST:
    SPOILER_ITEM_TABLE[f'Progressive {spoiler}'] = index
    SPOILER_ITEM_TABLE[f'{spoiler} - Bronze'] = index + 25
    SPOILER_ITEM_TABLE[f'{spoiler} - Silver'] = index + 50
    SPOILER_ITEM_TABLE[f'{spoiler} - Gold'] = index + 75
    index += 1

# Combine them all into an items list
ITEMS = {
    **PUZZLE_PIECE_TABLE,
    **COURSE_ITEM_TABLE,
    **TIME_TRIAL_ITEM_TABLE,
    **CUP_ITEM_TABLE,
    **CHARACTER_ITEM_TABLE,
    **CAR_ITEM_TABLE,
    **HAT_ITEM_TABLE,
    **SPOILER_ITEM_TABLE
}