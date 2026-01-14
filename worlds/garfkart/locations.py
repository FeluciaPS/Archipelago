# This file defines all locations that contain items, including ones that may not
# make it into the final release. I'd rather cast a wide net and delete things later
# than find out halfway through development that I'm missing a location and need to go
# back and patch it in.
#
# To match the convention set by items.py, all location IDs start at XX1 
# rather than XX0
 
from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld

from BaseClasses import Location
from .data import KART_NAMES, CHARACTER_NAMES, CUP_NAMES, RACE_NAMES
from .options import is_cups_randomized, is_races_randomized


# Locations for winning cups are short enough to hardcode instead of generating
# from CUP_NAMES
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

# Additional locations for character and kart unlocks that don't exist in the
# vanilla game
ADDITIONAL_CHARACTER_LOCATIONS = {}
ADDITIONAL_KART_LOCATIONS = {}

# 9 locations for item unlocks
ADDITIONAL_ITEM_LOCATIONS = {
    "Find Item: Pie": 1101,
    "Find Item: Homing Pie": 1102,
    "Find Item: Diamond": 1103,
    "Find Item: Magic Wand": 1104,
    "Find Item: Perfume": 1105,
    "Find Item: Lasagna": 1106,
    "Find Item: UFO": 1107,
    "Find Item: Pillow": 1108,
    "Find Item: Spring": 1109,
}

# 8 locations for character unlocks
for index, character in enumerate(CHARACTER_NAMES):
    ADDITIONAL_CHARACTER_LOCATIONS[f'Win Race as {character}'] = index + 1001

# 8 locations for kart unlocks
for index, kart in enumerate(KART_NAMES):
    ADDITIONAL_KART_LOCATIONS[f'Win Race with {kart}'] = index + 1051


LOCATION_NAME_TO_ID = {
    **COURSE_WIN_LOCATION_TABLE,
    **TIME_TRIAL_LOCATION_TABLE,
    **PUZZLE_PIECE_LOCATION_TABLE,
    **SPOILER_UNLOCK_LOCATION_TABLE,
    **HAT_UNLOCK_LOCATION_TABLE,
    **CUP_LOCATION_TABLE,
    **ADDITIONAL_KART_LOCATIONS,
    **ADDITIONAL_CHARACTER_LOCATIONS,
    **ADDITIONAL_ITEM_LOCATIONS
}

class GarfKartLocation(Location):
    game = "Garfield Kart - Furious Racing"

# Returns a filtered dictionary of location names and IDs based on an input list of names
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

# Returns all locations matching a substring
def get_locations_by_key_substring(locations: dict, substring: str):
    return {location: id for location, id in locations.items() if substring in location}

def create_all_locations(world: GarfKartWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: GarfKartWorld) -> None:
    randomize_races = is_races_randomized(world)
    randomize_cups = is_cups_randomized(world)

    if world.options.randomize_characters:
        region = world.get_region("Menu")
        region.add_locations(ADDITIONAL_CHARACTER_LOCATIONS)

    if world.options.randomize_karts:
        region = world.get_region("Menu")
        region.add_locations(ADDITIONAL_KART_LOCATIONS)

    for cup in CUP_NAMES:
        region = world.get_region(cup)

        # Add cup victory locations
        if randomize_cups:
            location_data = get_location_names_with_ids([f"{cup}: Victory"])
            region.add_locations(location_data, GarfKartLocation)

        # Add spoiler unlock locations
        if world.options.randomize_spoilers == "progressive":
            location_data = get_location_names_with_ids([
                f'{cup}: Unlock Bronze Spoiler (1)',
                f'{cup}: Unlock Bronze Spoiler (2)',
                f'{cup}: Unlock Silver Spoiler (1)',
                f'{cup}: Unlock Silver Spoiler (2)',
                f'{cup}: Unlock Gold Spoiler (1)',
                f'{cup}: Unlock Gold Spoiler (2)',
            ])
            region.add_locations(location_data, GarfKartLocation)
        
        if world.options.randomize_spoilers == "combine_tiers":
            location_data = get_location_names_with_ids([
                f'{cup}: Unlock Spoiler (1)',
                f'{cup}: Unlock Spoiler (2)',
            ])
            region.add_locations(location_data, GarfKartLocation)

    for race in RACE_NAMES:
        region = world.get_region(race)
        
        # Add race victory locations
        if randomize_races:
            location_data = get_location_names_with_ids([f"{race}: Victory"])
            region.add_locations(location_data, GarfKartLocation)

        # Add puzzle pieces
        if world.options.randomize_puzzle_pieces:
            # This helper function is the most graceful way I can think to do this right now.
            # If you're reading this and think you can do better let me know 
            # ~Felucia
            location_data = get_locations_by_key_substring(PUZZLE_PIECE_LOCATION_TABLE, race)
            region.add_locations(location_data, GarfKartLocation)

        # Add hat locations
        if world.options.randomize_hats == "progressive":
            location_data = get_location_names_with_ids([
                f"{race}: Bronze Hat Unlock",
                f"{race}: Silver Hat Unlock",
                f"{race}: Gold Hat Unlock",
            ])
            region.add_locations(location_data, GarfKartLocation)

        if world.options.randomize_hats == "combine_tiers":
            location_data = get_location_names_with_ids([f"{race}: Hat Unlock"])
            region.add_locations(location_data, GarfKartLocation)
            
    if world.options.randomize_items:
        region = world.get_region("Menu")
        if world.options.springs_only:
            location_data = get_location_names_with_ids(["Find Item: Spring"])
            region.add_locations(location_data)
        else:
            region.add_locations(ADDITIONAL_ITEM_LOCATIONS, GarfKartLocation)

def create_events(world: GarfKartWorld) -> None:
    pass
