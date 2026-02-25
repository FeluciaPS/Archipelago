from collections.abc import Mapping
from typing import Any
from Options import OptionError
from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world
from locations.regions import OVERWORLD_NAME
from data.items import ITEM_IDS

class TTTTWorld(World):
    """
    Tiny Terry's Turbo Trip is a silly collectathon about making your 
    car go fast enough to go to space. Makes sense to me!
    """
    game = "Tiny Terry's Turbo Trip"

    web = web_world.TTTTWebWorld()

    options_dataclass = options.TTTTOptions
    options: options.TTTTOptions

    def has_item(self, name: str):
        for item in self.multiworld.itempool:
            if item.player != self.player:
                continue
            
            if item.name == name:
                return True
            
        return False

    location_name_to_id = ITEM_IDS
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = OVERWORLD_NAME

    # TODO: Copied from Garfield Kart, this shouldn't end up in v1.0
    def pre_fill(self):
        from BaseClasses import CollectionState
        from Fill import sweep_from_pool
        state = sweep_from_pool(CollectionState(self.multiworld), self.multiworld.itempool)
        unreachable_locations = [location for location in self.get_locations() if not location.can_reach(state)]

        # I'm not good with exception types I'm sure "Exception" covers it
        if len(unreachable_locations):
            raise Exception(f"There are unreachable locations, please let Felucia know: {unreachable_locations}")
        if not len(self.multiworld.itempool):
            raise OptionError("There aren't any items in the item pool. Let Felucia know this is a bug.")

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_itempool(self)

    def create_item(self, name: str) -> items.GarfKartItem:
        return items.create_item_object(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item(self)
    
    # Slot data should at least contain the following:
    # - A copy of all settings for remote use
    # - Shop prices
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict()