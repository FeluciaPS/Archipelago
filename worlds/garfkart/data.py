"""Contains data objects used to generate items, locations, and rules"""
from __future__ import annotations


# List of race names in order of appearance
RACE_NAMES = [
    "Catz in the Hood",
    "Crazy Dunes",
    "Palerock Lake",
    "City Slicker",
    "Country Bumpkin",
    "Spooky Manor",
    "Mally Market",
    "Valley of the Kings",
    "Misty for Me",
    "Sneak-a-Peak",
    "Blazing Oasis",
    "Pastacosi Factory",
    "Mysterious Temple",
    "Prohibited Site",
    "Caskou Park",
    "Loopy Lagoon"
]

# Dict of races in each cup
RACES_BY_CUP = {
    "Lasagna Cup": [
        "Catz in the Hood",
        "Crazy Dunes",
        "Palerock Lake",
        "City Slicker"
    ],
    "Pizza Cup": [
        "Country Bumpkin",
        "Spooky Manor",
        "Mally Market",
        "Valley of the Kings"
    ],
    "Burger Cup": [
        "Misty for Me",
        "Sneak-a-Peak",
        "Blazing Oasis",
        "Pastacosi Factory"
    ],
    "Ice Cream Cup": [
        "Mysterious Temple",
        "Prohibited Site",
        "Caskou Park",
        "Loopy Lagoon"
    ]
}

CUPS_BY_RACE = {}
for cup in RACES_BY_CUP:
    for race in RACES_BY_CUP[cup]:
        CUPS_BY_RACE[race] = cup

# List of cup names in order of appearance
# The order of these matters for Progressive Cup Unlock logic
CUP_NAMES = [
    "Lasagna Cup",
    "Pizza Cup",
    "Burger Cup",
    "Ice Cream Cup",
]

CHARACTER_NAMES = [
    "Garfield",
    "Jon",
    "Liz",
    "Odie", 
    "Arlene",
    "Nermal",
    "Squeak",
    "Harry",
]

KART_NAMES = [
    "Formula Zzzz",
    "Abstract-Kart",
    "Medi-Kart",
    "Woof-Mobile",
    "Kissy-Kart",
    "Cutie-Pie Cat",
    "Rat-Racer",
    "Muck-Madness",
]

HAT_NAMES = [
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
    "Mule Head", # Harry
]

SPOILER_NAMES = [
    "Bombastic Spoiler",
    "Whacky Spoiler",
    "Superfit Spoiler",
    "Cyclobone Spoiler",
    "Foxy Spoiler",
    "Shimmering Spoiler",
    "Holey Moley Spoiler",
    "Stained Spoiler",
]

ITEM_NAMES = [
    "Pie",
    "Homing Pie",
    "Diamond",
    "Magic Wand",
    "Perfume",
    "Lasagna",
    "UFO",
    "Pillow",
    "Spring",
]

# Some puzzle pieces logically require items which is relevant for the planned
# item randomizer
class PuzzlePieceRequirements:
    Nothing = 0 # Probably unused 
    Spring = 1 # Spring
    Lasagna = 2 # Lasagna (unused)
    Either = 3 # Lasagna or Spring

# Dictionary of puzzle pieces and their required items
PUZZLE_PIECE_REQUIREMENTS = {
    "Catz in the Hood": {
        2: PuzzlePieceRequirements.Spring,
    },
    "Crazy Dunes": {
        1: PuzzlePieceRequirements.Spring,
        2: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Either,
    },
    "Palerock Lake": {},
    "City Slicker": {
        1: PuzzlePieceRequirements.Spring,
        2: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Spring,
    },
    "Country Bumpkin": {},
    "Spooky Manor": {
        1: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Spring,
    },
    "Mally Market": {
        1: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Spring,
    },
    "Valley of the Kings": {
        2: PuzzlePieceRequirements.Spring,
    },
    "Misty for Me": {
        1: PuzzlePieceRequirements.Spring,
        2: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Spring,
    },
    "Sneak-a-Peak": {
        1: PuzzlePieceRequirements.Spring,
        2: PuzzlePieceRequirements.Spring,
    },
    "Blazing Oasis": {
        1: PuzzlePieceRequirements.Spring,
        2: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Either,
    },
    "Pastacosi Factory": {
        1: PuzzlePieceRequirements.Spring,
    },
    "Mysterious Temple": {
        1: PuzzlePieceRequirements.Spring,
        2: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Spring,
    },
    "Prohibited Site": {
        1: PuzzlePieceRequirements.Spring,
        3: PuzzlePieceRequirements.Spring,
    },
    "Caskou Park": {
        3: PuzzlePieceRequirements.Spring,
    },
    "Loopy Lagoon": {
        3: PuzzlePieceRequirements.Spring,
    },
}