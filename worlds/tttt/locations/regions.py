# Defines region structure

from __future__ import annotations
from dataclasses import dataclass

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from worlds.generic.Rules import CollectionRule
    from ..world import TTTTWorld

OVERWORLD_NAME = "Sprankelwater"

# Why not add potential support for randomized starting locations
STARTING_LOCATION = "Sprankelwater"

# List of overworld area names. These all get a 2 way entrance without logic
# to Sprankelwater and are only used to store overworld items. There should be
# no entrances leading to/from these areas, all other regions connect to 
# sprankelwater
#
# These are purely here for my own sanity to make it easier to section off
# clusters of turbo junk without completely losing track of what's what.
OVERWORLD_ROAD_NAMES = [
    "Knijpkeurig",
    "Beukhaven Road",
    "Onderpret",
    "Zandtoeter Onderdoor",
    "Sloerdwijk",
    "Waardan Tunnel",
    "Autodrop",
    "Geldweg",
    "Stadsbengel"
]

OVERWORLD_AREA_NAMES = [
    *OVERWORLD_ROAD_NAMES,
    "Binnenrot",
    "Buitenrot Beach",
    "Sky Plaza",
    "Mascot Grounds",
    "Hotel", # + Braklam Street,
    "Zandtoeter Plains",
    "Waardan Bergrat",
    "Dakraderf",
    "Kinderpuin", # + Kinderpuin Road,
    "Truck & Trucker",
    "Katsklep",
    "Poedelstark & Mokernakt",
    "Mushroom Park",
    "Job Application Center",
]

# I'm sure this region manager will make things easier right? RIGHT?
@dataclass
class RegionManager:
    name: str = OVERWORLD_NAME
    children: dict[str, RegionManager] = {}
    required_items = {}
    parent_name = None

    def add_region(self, name, parent_region=None, is_locked_door=False, required_items={}):

        # Small optimisation: Only run this check on the root region
        if self.name == OVERWORLD_NAME:
            if self.get_region(name):
                raise Exception(f"Region {name} can't be added to RegionManager because a region by that name already exists.")

        if parent_region is not self.name:
            for value in self.children.values():
                value.add_region(name, parent_region, is_locked_door, required_items)
            return

        # Locked doors simply 
        if is_locked_door:
            required_items = {f"{name} Key": 1}

        self.children[name] = RegionManager(name=name, required_items=required_items, parent_name=name)


    def get_region(self, name):
        if name == self.name: 
            return self
        
        for child in self.children:
            region = self.children[child].get_region(name)
            if region:
                return region
            
        return None

    def get_parent(self):
        if not self.parent_name:
            return False
        return regions.get_region(self.parent_name)

regions = RegionManager()

for area in OVERWORLD_AREA_NAMES:
    regions.add_region(f"Overworld: {area}")

# Regions containing Turbo Junk
regions.add_region(
    "Hat Store (Green)", 
    required_items={
        "Hat Store Green Key": 1, 
        "Progressive Hat Store Key": 1
    }
)
regions.add_region(
    "Hat Store (Red)", 
    required_items={
        "Hat Store Red Key": 1, 
        "Progressive Hat Store Key": 2
    }
)
regions.add_region(
    "Hat Store (Blue)", 
    required_items={
        "Hat Store Blue Key": 1,
        "Progressive Hat Store Key": 3
    }
)

regions.add_region("Pet Store", is_locked_door=True)
regions.add_region("City Hall", is_locked_door=True)
regions.add_region("Beach Club", is_locked_door=True)
regions.add_region("Junk Store", is_locked_door=True)
regions.add_region("Job Application Center")
regions.add_region("The Generator")

# Regions not containing Turbo Junk
regions.add_region("Binnenrot Apartment Building", required_items={"Binnenrot Key": 1, "Progressive Apartment Key": 1})
regions.add_region("Terry's Appartment", parent_region="Binnenrot Apartment Building", required_items={"Terry Apartment Keys": 1, "Progressive Apartment Key": 2})
regions.add_region("Laundry House", required_items={"Laundry Key": 1})
regions.add_region("Zmiraphy's Garage", required_items={"Garage Key": 1})

def get_access_rule(world: TTTTWorld, region: RegionManager):
    requirements = {}
    needs_counts = False

    for item, count in region.required_items.items():
        if not world.has_item(item):
            continue

        requirements[item] = count
        needs_counts = True

    if not requirements:
        return None

    # After profiling, even at 100,000 calls using has over has_all_counts saves
    # less than 50ms. So this ordeal may be overkill but I'm doing it anyway
    if needs_counts:
        return lambda state: state.has_all_counts(requirements, world.player)

    required_items = list(requirements)
    if len(required_items) > 1:
        return lambda state: state.has_all(required_items, world.player)

    item = required_items[0]
    return lambda state: state.has(item, world.player)


# TODO: move this dataclass somewhere more appropriate
@dataclass
class EntranceData:
    entry: str
    exit: str
    rule: Optional[CollectionRule]

def get_entrance_rules(world: TTTTWorld, name, one_way=False):
    region = regions.get_region(name)
    parent = region.get_parent()

    if not parent:
        return []

    rule = get_access_rule(world, region)

    entrances = []
    entrances += [EntranceData(parent.name, region.name, rule)]
    if not one_way:
        entrances += [EntranceData(region.name, parent.name, rule)]

    return entrances

def get_region(world: TTTTWorld, name):
    return regions.get_region(name)