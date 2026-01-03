# Defines region structure

from __future__ import annotations
from dataclasses import dataclass

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

    def add_region(self, name, target_region=OVERWORLD_NAME, is_locked_door=False, required_items={}):

        # Small optimisation: Only run this check on the root region
        if self.name == OVERWORLD_NAME:
            if self.get_region(name):
                raise Exception(f"Region {name} can't be added to RegionManager because a region by that name already exists.")

        if target_region is not self.name:
            for value in self.children.values():
                value.add_region(name, target_region, is_locked_door, required_items)
            return

        # Locked doors simply 
        if is_locked_door:
            required_items = {f"{name} Key": 1}

        self.children[name] = RegionManager(name=name, required_items=required_items)

    def get_region(self, name):
        if name == self.name: 
            return self
        
        for child in self.children:
            region = self.children[child].get_region(name)
            if region:
                return region
            
        return None

regions = RegionManager()

for area in OVERWORLD_AREA_NAMES:
    regions.add_region(f"Overworld: {area}")

# Regions containing Turbo Junk
regions.add_region("Hat Store (Green)", required_items={"Hat Store Green Key": 1, "Progressive Hat Store Key": 1})
regions.add_region("Hat Store (Red)", required_items={"Hat Store Red Key": 1, "Progressive Hat Store Key": 2})
regions.add_region("Hat Store (Blue)", required_items={"Hat Store Blue Key": 1, "Progressive Hat Store Key": 3})
regions.add_region("Pet Store", is_locked_door=True)
regions.add_region("City Hall", is_locked_door=True)
regions.add_region("Beach Club", is_locked_door=True)
regions.add_region("Junk Store", is_locked_door=True)
regions.add_region("Job Application Center")
regions.add_region("The Generator")

# Regions not containing Turbo Junk
regions.add_region("Binnenrot Apartment Building", required_items={"Binnenrot Key": 1, "Progressive Apartment Key": 1})
regions.add_region("Terry's Appartment", "Binnenrot Apartment Building", required_items={"Apartment Key": 1, "Progressive Apartment Key": 2})
regions.add_region("Laundry House", required_items={"Laundry Key": 1})
regions.add_region("Zmiraphy's Garage", required_items={"Garage Key": 1})