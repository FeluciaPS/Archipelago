from __future__ import annotations


# This file defines all locations that contain items.
# for the first version those locations will just be 4 simple locations:
# - Beat Cup 1
# - Beat Cup 2
# - Beat Cup 3
# - Beat Cup 4
# (Yes, I can't be bothered to look up the cup names right now)

from BaseClasses import Location
from .data import CAR_NAMES, CHARACTER_NAMES, CUP_NAMES, RACE_NAMES

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld

# Locations for winning cups 
CUP_LOCATION_TABLE = {
    "Lasagna Cup: Victory": 101,
    "Pizza Cup: Victory": 102,
    "Burger Cup: Victory": 103,
    "Ice Cream Cup: Victory": 104,
}

HAT_UNLOCK_LOCATION_TABLE = {}
SPOILER_UNLOCK_LOCATION_TABLE = {}
PUZZLE_PIECE_LOCATION_TABLE = {}
COURSE_WIN_LOCATION_TABLE = {}
TIME_TRIAL_LOCATION_TABLE = {}

# Generate 8 spoiler unlock locations for every cup
for index, cup in enumerate(CUP_NAMES):
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Spoiler (1)'] = index + 301
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Spoiler (2)'] = index + 311
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Bronze Spoiler (1)'] = index + 321
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Bronze Spoiler (2)'] = index + 331
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Silver Spoiler (1)'] = index + 341
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Silver Spoiler (2)'] = index + 351
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Gold Spoiler (1)'] = index + 361
    SPOILER_UNLOCK_LOCATION_TABLE[f'{cup}: Unlock Gold Spoiler (2)'] = index + 371

# Generate race-specific locations:
# - Race victory
# - Hat unlock (any cc)
# - Hat unlock (gold/silver/bronze)
# - Time trials (platinum/gold/silver/bronze)
# - Puzzle piece 1-3
for index, race in enumerate(RACE_NAMES):
    # 3 puzzle pieces per race
    for n in range(3):
        name = f'{race}: Puzzle Piece {n + 1}'
        PUZZLE_PIECE_LOCATION_TABLE[name] = 3 * index + n + 201

    # Cource victory location
    COURSE_WIN_LOCATION_TABLE[f'{race}: Victory'] = index + 1

    # Hat unlocks 
    HAT_UNLOCK_LOCATION_TABLE[f'{race}: Hat Unlock'] = index + 401
    HAT_UNLOCK_LOCATION_TABLE[f'{race}: Bronze Hat Unlock'] = index + 421
    HAT_UNLOCK_LOCATION_TABLE[f'{race}: Silver Hat Unlock'] = index + 441
    HAT_UNLOCK_LOCATION_TABLE[f'{race}: Gold Hat Unlock'] = index + 461

    # 4 time trials per race
    TIME_TRIAL_LOCATION_TABLE[f'{race}: Time Trial Bronze'] = index + 21
    TIME_TRIAL_LOCATION_TABLE[f'{race}: Time Trial Silver'] = index + 41
    TIME_TRIAL_LOCATION_TABLE[f'{race}: Time Trial Gold'] = index + 61
    TIME_TRIAL_LOCATION_TABLE[f'{race}: Time Trial Platinum'] = index + 81

# Additional locations for character and car unlocks that don't exist in the
# vanilla game
ADDITIONAL_CHARACTER_LOCATIONS = {}
ADDITIONAL_CAR_LOCATIONS = {}

# 8 locations for character unlocks
for index, character in enumerate(CHARACTER_NAMES):
    ADDITIONAL_CHARACTER_LOCATIONS[f'Win Race as {character}'] = index + 1001

# 8 locations for car unlocks
for index, car in enumerate(CAR_NAMES):
    ADDITIONAL_CAR_LOCATIONS[f'Win Race with {car}'] = index + 1051

LOCATION_NAME_TO_ID = {
    **COURSE_WIN_LOCATION_TABLE,
    **TIME_TRIAL_LOCATION_TABLE,
    **PUZZLE_PIECE_LOCATION_TABLE,
    **SPOILER_UNLOCK_LOCATION_TABLE,
    **HAT_UNLOCK_LOCATION_TABLE,
    **CUP_LOCATION_TABLE,
    **ADDITIONAL_CAR_LOCATIONS,
    **ADDITIONAL_CHARACTER_LOCATIONS
}

class GarfKartLocation(Location):
    game = "Garfield Kart - Furious Racing"

# Return a filtered dictionary of location names and IDs based on an input list of names
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def get_locations_by_key_substring(locations: dict, substring: str):
    return {location: id for location, id in locations.items() if substring in location}

def create_all_locations(world: GarfKartWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: GarfKartWorld) -> None:
    # Add cup victory locations
    # TODO: This probably depends on some yaml option
    for cup in CUP_NAMES:
        location_data = get_location_names_with_ids([f"{cup}: Victory"])
        region = world.get_region("Menu")
        region.add_locations(location_data, GarfKartLocation)

    # Add puzzle pieces
    if world.options.randomize_puzzle_pieces:
        for race in RACE_NAMES:
            # This helper function is the most graceful way I can think to do this right now.
            # If you're reading this and think you can do better let me know 
            # ~Felucia
            location_data = get_locations_by_key_substring(PUZZLE_PIECE_LOCATION_TABLE, race)
            region = world.get_region(race)
            region.add_locations(location_data, GarfKartLocation)
            

def create_events(world: GarfKartWorld) -> None:
    pass