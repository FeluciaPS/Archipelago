

from collections.abc import Mapping
from typing import Any
from Options import OptionError
from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world

# I'll be calling these classes GarfKart because GarfieldKartFuriousRacing
# is way too long and I don't believe for a second anyone's going to
# randomize the original Garfield Kart, so there shouldn't be an issue
# using that class name.
class GarfKartWorld(World):
    """
    Garfield Kart - Furious Racing is a chaotic kart racer featuring
    everyone's favourite orange cat and plenty of lasagna.
    """

    game = "Garfield Kart - Furious Racing"

    web = web_world.GarfKartWebWorld()

    options_dataclass = options.GarfKartOptions
    options: options.GarfKartOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    # Helper variable stores puzzle pieces that aren't logically required, these
    # may later be used as filler items in the filler item pool.
    unused_puzzle_pieces = []

    # TODO: this shouldn't end up in v1.0
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

    def generate_early(self):
        if self.options.goal == "puzzle_piece_hunt":
            self.options.randomize_puzzle_pieces.value = True

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
    
    # Copied from APQuest for the time being
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal", "time_trial_goal_grade", "cc_requirement", "progressive_cups", "puzzle_piece_count", "randomize_puzzle_pieces", "randomize_items"
        )
