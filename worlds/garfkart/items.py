

from BaseClasses import Item, ItemClassification
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
    name = f'Cup Unlock {cup}'
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


# Combine them all into an items list
ITEM_IDS = {
    **PUZZLE_PIECE_TABLE,
    **COURSE_ITEM_TABLE,
    **TIME_TRIAL_ITEM_TABLE,
    **CUP_ITEM_TABLE,
    **CHARACTER_ITEM_TABLE,
    **CAR_ITEM_TABLE,
    **HAT_ITEM_TABLE,
    **SPOILER_ITEM_TABLE
}