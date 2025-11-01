from __future__ import annotations

# Logic goes here
# Logic goes here
# For v0.1 logic is just "require item to unlock cup"
# I hope.


from worlds.generic.Rules import set_rule

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld


def set_all_rules(world: GarfKartWorld):
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: GarfKartWorld):
    lasagna_cup = world.get_entrance("Menu to Lasagna Cup")
    pizza_cup = world.get_entrance("Menu to Pizza Cup")
    burger_cup = world.get_entrance("Menu to Burger Cup")
    ice_cream_cup = world.get_entrance("Menu to Ice Cream Cup")

    if world.options.progressive_cups:
        set_rule(pizza_cup, lambda state: state.has("Progressive Cup", world.player, 1))
        set_rule(burger_cup, lambda state: state.has("Progressive Cup", world.player, 2))
        set_rule(ice_cream_cup, lambda state: state.has("Progressive Cup", world.player, 3))
    else:
        set_rule(lasagna_cup, lambda state: state.has("Cup Unlock - Lasagna Cup", world.player))
        set_rule(pizza_cup, lambda state: state.has("Cup Unlock - Pizza Cup", world.player))
        set_rule(burger_cup, lambda state: state.has("Cup Unlock - Burger Cup", world.player))
        set_rule(ice_cream_cup, lambda state: state.has("Cup Unlock - Ice Cream Cup", world.player))

def set_all_location_rules(world: GarfKartWorld):
    pass

def set_completion_condition(world: GarfKartWorld):
    # The game is considered "completed" if all cup victory events are present
    world.multiworld.completion_condition[world.player] = lambda state: state.has_all([
        "Lasagna Cup Victory",
        "Pizza Cup Victory",
        "Burger Cup Victory",
        "Ice Cream Cup Victory"
    ], world.player)