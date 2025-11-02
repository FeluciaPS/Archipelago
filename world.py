

from collections.abc import Mapping
from typing import Any
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

    def generate_early(self):
        if self.options.goal == "puzzle_piece_hunt":
            self.options.randomize_puzzle_pieces = True

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.GarfKartItem:
        return items.create_item_object(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item(self)
    
    # Copied from APQuest for the time being
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "goal", "progressive_cups"
        )