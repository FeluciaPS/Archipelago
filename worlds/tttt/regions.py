from __future__ import annotations

from typing import TYPE_CHECKING
from .locations.regions import get_entrance_rules, regions as REGIONS
from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import TTTTWorld
    from .locations.regions import RegionManager, EntranceData

#
# Regions should be pretty limited in this game, most of the game is effortlessly 
# accessible from the start I think it'd be valid to use every enterable building 
# as a region, in case we want to add arbitrary locks to the doors eventually
#
def create_and_connect_regions(world: TTTTWorld) -> None:
    create_regions(world, REGIONS)

def create_regions(world: TTTTWorld, region_node: RegionManager):
    region = Region(region_node.name, world.player, world.multiworld)

    world.multiworld.regions += [region]

    if region_node.get_parent():
        entrances = get_entrance_rules(world, region_node.name)
        for entrance in entrances:
            connect_regions(world, entrance)

    for key, node in region_node.children:
        create_regions(world, node)

def connect_regions(world: TTTTWorld, entrance: EntranceData):
    entry_region = world.get_region(entrance.entry)
    exit_region = world.get_region(entrance.exit)
    entry_region.connect(exit_region, f"{entrance.entry} to {entrance.exit}", entrance.rule)