from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .data.items_inventory import KEY_ITEM_NAMES, PET_BLUEPRINT_ITEM_NAMES, WEAPON_ITEM_NAMES
from .data.items import ITEM_IDS

if TYPE_CHECKING:
    from .world import TTTTWorld

class TTTTItem(Item):
    game = "Tiny Terry's Turbo Trip"

def get_random_filler_item_name(world: TTTTWorld) -> str:
    return "Filler Item"


def create_item_with_correct_classification(world: TTTTWorld, name: str) -> TTTTItem:
    classification = ItemClassification.filler

    # Hardcoding this whole thing because I want to get v0.1 out
    progression_items = [
        "Shovel",
        "Bug Net",
        "Para Glider",
        *WEAPON_ITEM_NAMES,
        *PET_BLUEPRINT_ITEM_NAMES,
        *KEY_ITEM_NAMES
    ]

    if name in progression_items:
        classification = ItemClassification.progression

    if name == "Turbo Upgrade":
        classification = ItemClassification.progression_deprioritized_skip_balancing

    if name == "Map":
        classification = ItemClassification.useful
        
    return TTTTItem(name, classification, ITEM_IDS[name], world.player)


def create_all_items(world: TTTTWorld) -> None:
    itempool: list[Item] = []

    # For v0.1 I'm adding exactly 8 turbo upgrades to the pool. We can worry about more later
    # that DOES mean the game won't generate if you set your goal to >8 so just don't do that
    # LOL
    itempool += [
        world.create_item("Turbo Upgrade") for _ in range(8)
    ]

    # At least one weapon should be in the itempool
    random_weapon = world.random.sample(WEAPON_ITEM_NAMES)
    itempool += [
        world.create_item(random_weapon)
    ]

    # Net, Shovel, and Glider are always randomized
    itempool += [
        world.create_item("Shovel"),
        world.create_item("Bug Net"),
        world.create_item("Para Glider"),
    ]

    # Add all blueprints to itempool
    # Pets aren't added to itempool and instead treated as filler items
    itempool += [
        world.create_item(blueprint) for blueprint in PET_BLUEPRINT_ITEM_NAMES
    ]

    # Map can be randomized
    if world.options.randomize_map:
        itempool += [
            world.create_item("Map")
        ]

    if world.options.lock_doors == "apartment_only":
        itempool += [
            world.create_item("Terry's Apartment Keys")
        ]

    # Compare item pool size to location size, and fill what's left with
    # filler items.
    item_count = len(itempool)
    unfilled_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    filler_item_count = unfilled_location_count - item_count
    
    itempool += [
        world.create_filler() for _ in range(filler_item_count)
    ]

    # Append the item pool to the world's
    world.multiworld.itempool += itempool