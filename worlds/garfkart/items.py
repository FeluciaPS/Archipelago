# This file should cover every item we could possibly need, even ones that are
# unimplemented as of writing this. There's a small chance we'll need to clean
# up unused ones on a full release
#
# The first ID (000, 100, 150) in every group is reserved for a progressive
# unlock item, even if one doesn't exist
#
# There's an argument to be made for fully writing out the item lists instead
# of generating a bunch of them with for loops for easy ID lookup, but 
# right now this is a whole lot easier on me.
 
from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld

from BaseClasses import Item, ItemClassification
from .data import RACE_NAMES, CUP_NAMES, CHARACTER_NAMES, CAR_NAMES, HAT_NAMES, SPOILER_NAMES


# Puzzle Pieces are named by race and numbered 1-3 to match the order 
# in which they are displayed in-game
PUZZLE_PIECE_TABLE = {}
COURSE_ITEM_TABLE = {
    "Progressive Course Unlock": 100
}
TIME_TRIAL_ITEM_TABLE = { # TODO: I suspect these will end up going unused
    "Progressive Time Trial Unlock": 150
}
CUP_ITEM_TABLE = {
    "Progressive Cup Unlock": 200,
    "Cup Unlock - Lasagna Cup": 201,
    "Cup Unlock - Pizza Cup": 202,
    "Cup Unlock - Burger Cup": 203,
    "Cup Unlock - Ice Cream Cup": 204,
}
CHARACTER_ITEM_TABLE = {}
CAR_ITEM_TABLE = {}
HAT_ITEM_TABLE = {}
SPOILER_ITEM_TABLE = {}
ITEM_BOX_RANDOMIZER_TABLE = {
    "Item Unlock - Pie": 901,
    "Item Unlock - Homing Pie": 902,
    "Item Unlock - Diamond": 903,
    "Item Unlock - Magic Wand": 904,
    "Item Unlock - Perfume": 905,
    "Item Unlock - Lasagna": 906,
    "Item Unlock - UFO": 907,
    "Item Unlock - Pillow": 908,
    "Item Unlock - Spring": 909,
}

# Generate race-specific items:
# - Course Unlock
# - Time Trial Unlock
# - Puzzle piece 1-3
for index, race in enumerate(RACE_NAMES):
    course_unlock_name = f'Course Unlock - {race}'
    time_trial_unlock_name = f'Time Trial Unlock - {race}'

    # 3 puzzle pieces per race
    for n in range(3):
        name = f'{race} - Puzzle Piece {n + 1}'
        PUZZLE_PIECE_TABLE[name] = index * 3 + n + 1

    COURSE_ITEM_TABLE[course_unlock_name] = index + 101
    TIME_TRIAL_ITEM_TABLE[time_trial_unlock_name] = index + 151

# Generate 8 character unlock items
for index, character in enumerate(CHARACTER_NAMES):
    CHARACTER_ITEM_TABLE[character] = index + 301

# Generate 8 car unlock items
for index, car in enumerate(CAR_NAMES):
    CAR_ITEM_TABLE[car] = index + 351

# Generate 48 hat unlock items
for index, hat in enumerate(HAT_NAMES):
    HAT_ITEM_TABLE[f'Progressive {hat}'] = index + 401
    HAT_ITEM_TABLE[f'{hat} - Bronze'] = index + 426
    HAT_ITEM_TABLE[f'{hat} - Silver'] = index + 451
    HAT_ITEM_TABLE[f'{hat} - Gold'] = index + 476

# Generate 24 spoiler unlock items
for index, spoiler in enumerate(SPOILER_NAMES):
    SPOILER_ITEM_TABLE[f'Progressive {spoiler}'] = index + 501
    SPOILER_ITEM_TABLE[f'{spoiler} - Bronze'] = index + 526
    SPOILER_ITEM_TABLE[f'{spoiler} - Silver'] = index + 551
    SPOILER_ITEM_TABLE[f'{spoiler} - Gold'] = index + 576

# Filler items reserve IDs 1000+
# Trap items reserve IDs 1500+
FILLER_ITEM_TABLE = {
    "Filler Item": 1000, # Does nothing, delete later in dev
    "Item - Spring": 1001, # Gives spring next time player has an empty item slot
    "Item - Pie": 1002, # Gives pie next time player has an empty item slot
    "Random Item Box": 1003, # Gives random item box next time player has an empty item slot
    "Start Boost Helper (Single Use)": 1004, # Guarantees perfect boost at start of next race
}
TRAP_ITEM_TABLE = {
    "Mirror Trap": 1500, # Mirrors all tracks until you beat one race
    "Handling Trap": 1501, # Drastically increases handling until you beat one race
}

# Combine them all into an item dict
ITEM_NAME_TO_ID = {
    **PUZZLE_PIECE_TABLE, # 48
    **COURSE_ITEM_TABLE, # 16
    **TIME_TRIAL_ITEM_TABLE, # 16
    **CUP_ITEM_TABLE, # 4
    **CHARACTER_ITEM_TABLE, # 8
    **CAR_ITEM_TABLE, # 8
    **HAT_ITEM_TABLE, # 48
    **SPOILER_ITEM_TABLE, # 24 
    **ITEM_BOX_RANDOMIZER_TABLE, # 8
    **FILLER_ITEM_TABLE, # as many as we want
    **TRAP_ITEM_TABLE # as many as we want
}

# Progression items
# TODO: Handle these differently
PROGRESSION_ITEMS = [
    *COURSE_ITEM_TABLE,
    *TIME_TRIAL_ITEM_TABLE,
    *CUP_ITEM_TABLE
]

class GarfKartItem(Item):
    game = "Garfield Kart - Furious Racing"


############# 
# Functions #
#############
def get_random_filler_item(world: GarfKartWorld) -> str:
    # Hardcode filler items to be blank items that do nothing
    return "Filler Item"

    # TODO: Include traps
    # TODO: Optionally include puzzle pieces, since they're filler when not the goal
    return world.random.choice(list(FILLER_ITEM_TABLE))

def create_item_object(world: GarfKartWorld, name: str):
    classification = ItemClassification.useful

    # Progression items are progression items
    if name in PROGRESSION_ITEMS:
        classification = ItemClassification.progression

    # Deprioritize puzzle pieces
    if name in PUZZLE_PIECE_TABLE:
        if world.options.randomize_puzzle_pieces:
            classification = ItemClassification.progression_deprioritized_skip_balancing
        else:
            classification = ItemClassification.filler

    # Filler is filler (no way!)
    if name in FILLER_ITEM_TABLE:
        classification = ItemClassification.filler

    # Traps are traps
    if name in TRAP_ITEM_TABLE:
        classification = ItemClassification.trap

    return GarfKartItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_itempool(world: GarfKartWorld) -> None:
    itempool: list[Item] = []

    randomize_races = world.options.randomize_races == "races" or world.options.randomize_races == "cups_and_races"
    randomize_cups = world.options.randomize_races == "cups" or world.options.randomize_races == "cups_and_races"

    # Add race victory locations
    if randomize_races:
        shuffled_races = RACE_NAMES
        world.random.shuffle(shuffled_races)
        starting_race_name = shuffled_races.pop()
        starting_race_item = world.create_item(f'Course Unlock - {starting_race_name}')
        world.push_precollected(starting_race_item)

        itempool += [
            world.create_item(f'Course Unlock - {race}') for race in shuffled_races
        ]

    # Add cup victory locations
    if randomize_cups:
        if world.options.progressive_cups:

            itempool += [
                world.create_item("Progressive Cup Unlock"),
                world.create_item("Progressive Cup Unlock"),
                world.create_item("Progressive Cup Unlock"),
            ]
        else:

            # For now random cups assume you want a randomized starting cup,
            # but I suppose you could just want to start with Lasagna cup?
            shuffled_cups = CUP_NAMES
            world.random.shuffle(shuffled_cups)
            starting_cup_name = shuffled_cups.pop()
            starting_cup_item = world.create_item(f'Cup Unlock - {starting_cup_name}')
            world.push_precollected(starting_cup_item)

            # Add the other 3 cups to the itempool
            itempool += [
                world.create_item(f'Cup Unlock - {cup}') for cup in shuffled_cups
            ]

    # randomize_puzzle_pieces is automatically set to True if the goal is 
    # Puzzle Piece Hunt, so we don't need to check both.
    # TODO: Above comment is lying. We need to check both if we want to put them in the filler pool
    if world.options.randomize_puzzle_pieces:
        itempool += [world.create_item(piece) for piece in list(PUZZLE_PIECE_TABLE)]

    # Compare item pool size to location size, and fill what's left with
    # filler items.
    item_count = len(itempool)
    unfilled_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    filler_item_count = unfilled_location_count - item_count
    
    itempool += [
        world.create_filler() for _ in range(filler_item_count)
    ]

    # Append the item pool to the world's
    world.multiworld.itempool += itempool