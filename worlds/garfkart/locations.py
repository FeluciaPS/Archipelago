from __future__ import annotations


# This file defines all locations that contain items.
# for the first version those locations will just be 4 simple locations:
# - Beat Cup 1
# - Beat Cup 2
# - Beat Cup 3
# - Beat Cup 4
# (Yes, I can't be bothered to look up the cup names right now)

from BaseClasses import Location
from . import items

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld

from .data import CUP_NAMES

# Cup victories reserve IDs 100-150.

CUP_LOCATION_TABLE = {}

for index, cup in enumerate(CUP_NAMES):
    name = f'Win {cup}'
    CUP_LOCATION_TABLE[name] = index + 101

LOCATION_NAME_TO_ID = {
    **CUP_LOCATION_TABLE
}

class GarfKartLocation(Location):
    game = "Garfield Kart - Furious Racing"

# Copied from APQuest and now's not the time for me to figure out how it works or why
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: GarfKartWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: GarfKartWorld) -> None:
    # Add cup victory locations
    for cup in CUP_NAMES:
        location_data = get_location_names_with_ids([f"Win {cup}"])
        region = world.get_region(cup)
        region.add_locations(location_data, GarfKartLocation)

def create_events(world: GarfKartWorld) -> None:
    pass