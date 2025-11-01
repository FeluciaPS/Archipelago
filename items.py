from __future__ import annotations

from BaseClasses import Item, ItemClassification

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld

from .data import RACE_NAMES, CUP_NAMES, CHARACTER_NAMES, CAR_NAMES, HAT_NAMES, SPOILER_NAMES

# Set up a lot of the potential items we'll need to deal with in the future
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


# Puzzle pieces reserve IDs 0-100. 
# They're named by race name and numbered 1-3
# 
# Course items reserve IDs 100-150.
# Time trial items reserve IDs 150-200.
PUZZLE_PIECE_TABLE = {}
COURSE_ITEM_TABLE = {
    "Progressive Course Unlock": 100
}
TIME_TRIAL_ITEM_TABLE = {
    "Progressive Time Trial Unlock": 150
}

for index, race in enumerate(RACE_NAMES):
    course_unlock_name = f'Course Unlock - {race}'
    time_trial_unlock_name = f'Time Trial Unlock - {race}'

    # 3 puzzle pieces per race
    for n in range(3):
        name = f'{race} - Puzzle Piece {n}'
        PUZZLE_PIECE_TABLE[name] = index + 1
    COURSE_ITEM_TABLE[course_unlock_name] = index + 101
    TIME_TRIAL_ITEM_TABLE[time_trial_unlock_name] = index + 151


# Cup items reserve IDs 200-250.
CUP_ITEM_TABLE = {
    "Progressive Cup Unlock": 200,
}

for index, cup in enumerate(CUP_NAMES):
    name = f'Cup Unlock - {cup}'
    CUP_ITEM_TABLE[name] = index + 201


# Character items reserve IDs 300-325
CHARACTER_ITEM_TABLE = {}

for index, character in enumerate(CHARACTER_NAMES):
    CHARACTER_ITEM_TABLE[name] = index + 301


# Car items reserve IDs 350-400
CAR_ITEM_TABLE = {}

for index, car in enumerate(CAR_NAMES):
    CAR_ITEM_TABLE[name] = index + 351


# Hat items reserve IDs 400-500
HAT_ITEM_TABLE = {}
for index, hat in enumerate(HAT_NAMES):
    HAT_ITEM_TABLE[f'Progressive {hat}'] = index + 401
    HAT_ITEM_TABLE[f'{hat} - Bronze'] = index + 426
    HAT_ITEM_TABLE[f'{hat} - Silver'] = index + 451
    HAT_ITEM_TABLE[f'{hat} - Gold'] = index + 476


# Spoiler items reserve IDs 500-600
SPOILER_ITEM_TABLE = {}
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
    "Mirror Trap": 1500 # Mirrors all tracks until you beat one race
}


# Combine them all into an items list
ITEM_NAME_TO_ID = {
    **PUZZLE_PIECE_TABLE, # 48
    **COURSE_ITEM_TABLE, # 16
    **TIME_TRIAL_ITEM_TABLE, # 16
    **CUP_ITEM_TABLE, # 4
    **CHARACTER_ITEM_TABLE, # 8
    **CAR_ITEM_TABLE, # 8
    **HAT_ITEM_TABLE, # 48
    **SPOILER_ITEM_TABLE, # 24 
    **FILLER_ITEM_TABLE, # ???
    **TRAP_ITEM_TABLE # ???
}

# Progression items, for the time being, 
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
    return world.random.choice(list(FILLER_ITEM_TABLE))

def create_item_object(world: GarfKartWorld, name: str):
    classification = ItemClassification.useful

    # Progression items are progression items
    if name in PROGRESSION_ITEMS:
        classification = ItemClassification.progression

    # Deprioritize puzzle pieces
    if name in PUZZLE_PIECE_TABLE:
        classification = ItemClassification.progression_deprioritized_skip_balancing

    # Filler is filler
    if name in FILLER_ITEM_TABLE:
        classification = ItemClassification.filler

    # Traps are traps
    if name in TRAP_ITEM_TABLE:
        classification = ItemClassification.trap

    return GarfKartItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: GarfKartWorld) -> None:
    itempool: list[Item] = []

    # For v0.1 the only relevant items are cup unlocks, I'm gonna make Jeff 
    # a bit sad and include both progressive and direct unlocks in v0.1
    if world.options.progressive_cups:
        itempool += [
            world.create_item("Progressive Course Unlock"),
            world.create_item("Progressive Course Unlock"),
            world.create_item("Progressive Course Unlock"),
        ]
    else:
        # For now random cups assume you want a randomized starting cup,
        # progressive cups assume you don't.
        shuffled_cups = CUP_NAMES
        world.random.shuffle(shuffled_cups)
        starting_cup_name = shuffled_cups.pop()
        starting_cup_item = world.create_item(f'Cup Unlock - {starting_cup_name}')
        world.push_precollected(starting_cup_item)

        # Add the other 3 cups to the itempool
        itempool += [
            world.create_item(f'Cup Unlock - {cup}') for cup in shuffled_cups
        ]

    # Compare item pool size to location size, and fill what's left with
    # filler items
    item_count = len(itempool)
    unfilled_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    filler_item_count = unfilled_location_count - item_count
    
    if world.options.goal != "puzzle_piece_hunt":
        # TODO: Down the line we can add puzzle pieces as filler items when 
        # they're not progression items
        pass

    itempool += [
        world.create_filler() for _ in range(filler_item_count)
    ]

    # Append the item pool to the world's
    world.multiworld.itempool += itempool