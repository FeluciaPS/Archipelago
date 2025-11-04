from __future__ import annotations

# Logic goes here
# Logic goes here
# For v0.1 logic is just "require item to unlock cup"
# I hope.


from .data import CUP_NAMES, RACE_NAMES, RACES_BY_CUP
from worlds.generic.Rules import set_rule

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld


def set_all_rules(world: GarfKartWorld):
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: GarfKartWorld):
    # TODO: It'd be a whole lot easier to split options for randomize_races
    # and randomize_cups for logic purposes
    if world.options.randomize_races == "races" or world.options.randomize_races == "cups_and_races":

        # If races are randomized, each race is only accessible if you have the race item
        for race in RACE_NAMES:
            entrance = world.get_entrance(f'Menu to {race}')
            set_rule(entrance, lambda state: state.has(f'Course Unlock - {race}', world.player))

    elif world.options.randomize_races == "cups":

        # If grand prix are randomized and races aren't, races become available
        # whenever the associated grand prix cup is unlocked
        if world.options.progressive_cups:

            # Progressive cup unlocks require n Progressive Cup Unlock items to unlock their races
            for index, cup in enumerate(CUP_NAMES): 
                if index > 0:
                    for race in RACES_BY_CUP[cup]:
                        entrance = world.get_entrance(race)
                        set_rule(entrance, lambda state: state.has("Progressive Cup Unlock", world.player, index))
        else:

            # Regular cup unlocks simply require the item to unlock their races
            for cup in CUP_NAMES:
                for race in RACES_BY_CUP[cup]:
                    entrance = world.get_entrance(race)
                    set_rule(entrance, lambda state: state.has(f"Cup Unlock - {cup}", world.player))
    else:
        
        # Otherwise, races are always unlocked
        pass

def set_all_location_rules(world: GarfKartWorld):
    lasagna_cup = world.get_location("Lasagna Cup: Victory")
    pizza_cup = world.get_location("Pizza Cup: Victory")
    burger_cup = world.get_location("Burger Cup: Victory")
    ice_cream_cup = world.get_location("Ice Cream Cup: Victory")

    if world.options.progressive_cups:
        set_rule(pizza_cup, lambda state: state.has("Progressive Cup Unlock", world.player, 1))
        set_rule(burger_cup, lambda state: state.has("Progressive Cup Unlock", world.player, 2))
        set_rule(ice_cream_cup, lambda state: state.has("Progressive Cup Unlock", world.player, 3))
    else:
        set_rule(lasagna_cup, lambda state: state.has("Cup Unlock - Lasagna Cup", world.player))
        set_rule(pizza_cup, lambda state: state.has("Cup Unlock - Pizza Cup", world.player))
        set_rule(burger_cup, lambda state: state.has("Cup Unlock - Burger Cup", world.player))
        set_rule(ice_cream_cup, lambda state: state.has("Cup Unlock - Ice Cream Cup", world.player))

def set_completion_condition(world: GarfKartWorld):

    if world.options.goal == "grand_prix":
        # The game can be completed if all cups are unlocked
        if world.options.progressive_cups:
            world.multiworld.completion_condition[world.player] = lambda state: state.has("Progressive Cup Unlock", world.player, 3)
        else:
            world.multiworld.completion_condition[world.player] = lambda state: state.has_all([
                "Cup Unlock - Lasagna Cup",
                "Cup Unlock - Pizza Cup",
                "Cup Unlock - Burger Cup",
                "Cup Unlock - Ice Cream Cup"
            ], world.player)
    elif world.options.goal == "puzzle_piece_hunt":
        # Game can be completed if all puzzle pieces are received
        puzzle_piece_names = [
            f'{race} - Puzzle Piece {n + 1}' for race in RACE_NAMES for n in range(3)
        ]
        world.multiworld.completion_condition[world.player] = lambda state: state.has_all(puzzle_piece_names, world.player)
    