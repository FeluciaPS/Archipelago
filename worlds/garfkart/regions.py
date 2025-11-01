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
if TYPE_CHECKING:
    from .world import GarfKartWorld


def create_and_connect_regions(world: GarfKartWorld):
    create_regions(world)
    connect_regions(world)

def create_regions(world: GarfKartWorld):
    # For the time being each cup is a region but eventually we'll probably
    # have to split it by race
    menu = Region("Menu", world.player, world.multiworld)
    lasagna_cup = Region("Lasagna Cup", world.player, world.multiworld)
    pizza_cup = Region("Pizza Cup", world.player, world.multiworld)
    burger_cup = Region("Burger Cup", world.player, world.multiworld)
    ice_cream_cup = Region("Ice Cream Cup", world.player, world.multiworld)

    regions = [
        menu,
        lasagna_cup,
        pizza_cup,
        burger_cup,
        ice_cream_cup,
    ]

    world.multiworld.regions += regions

def connect_regions(world: GarfKartWorld):
    menu = world.get_region("Menu")
    lasagna_cup = world.get_region("Lasagna Cup")
    pizza_cup = world.get_region("Pizza Cup")
    burger_cup = world.get_region("Burger Cup")
    ice_cream_cup = world.get_region("Ice Cream Cup")

    menu.connect(lasagna_cup, "Menu to Lasagna Cup")
    menu.connect(pizza_cup, "Menu to Pizza Cup")
    menu.connect(burger_cup, "Menu to Burger Cup")
    menu.connect(ice_cream_cup, "Menu to Ice Cream Cup")