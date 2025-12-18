from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import TTTTWorld

LOCATION_NAME_TO_ID = {}

class TTTTLocation(Location):
    game = "Tiny Terry's Turbo Trip"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: TTTTWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: TTTTWorld) -> None:
    pass

def create_events(world: TTTTWorld) -> None:
    pass
