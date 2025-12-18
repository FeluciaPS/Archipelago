from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import TTTTWorld

#
# Regions should be pretty limited in this game, most of the game is effortlessly 
# accessible from the start I think it'd be valid to use every enterable building 
# as a region, in case we want to add arbitrary locks to the doors eventually
#
def create_and_connect_regions(world: TTTTWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: TTTTWorld) -> None:
    sprankelwater = Region("Sprankelwater", world.player, world.multiworld)

    regions = [ sprankelwater ]

    world.multiworld.regions += regions

def connect_regions(world: TTTTWorld) -> None:
    pass
