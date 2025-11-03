from __future__ import annotations

# Region structure starts with the origin (Main Menu) region
# Then probably splits regions by course/cup
#
# The reason for not structuring it like Main Menu->Cup->Course is 
# that makes individual courses logically inaccessible if you can't 
# access the corresponding cup, which might be undesirable in the future.
#
# I don't see a purpose in setting up some deep logical structure for regions
# as of now. Most logic will end up pretty simple and can be done at the 
# location level instead.

from BaseClasses import Region

from typing import TYPE_CHECKING

from worlds.garfkart.data import RACE_NAMES
if TYPE_CHECKING:
    from .world import GarfKartWorld


def create_and_connect_regions(world: GarfKartWorld):
    create_regions(world)
    connect_regions(world)

def create_regions(world: GarfKartWorld):
    # For the time being each cup is a region but eventually we'll probably
    # have to split it by race
    menu = Region("Menu", world.player, world.multiworld)
    
    regions = [
        menu
    ]

    regions += [
        Region(race, world.player, world.multiworld) for race in RACE_NAMES
    ]

    world.multiworld.regions += regions

def connect_regions(world: GarfKartWorld):
    menu = world.get_region("Menu")

    for race in RACE_NAMES:
        region = world.get_region(race)
        menu.connect(region, race)