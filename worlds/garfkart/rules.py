from __future__ import annotations

# Logic goes here
# Logic goes here
# For v0.1 logic is just "require item to unlock cup"
# I hope.


from .data import CUP_NAMES, CUPS_BY_RACE, RACE_NAMES, RACES_BY_CUP
from worlds.generic.Rules import set_rule

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import GarfKartWorld


def set_all_rules(world: GarfKartWorld):
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def get_required_cup_items(cup: str, randomize_races: bool, randomize_cups: bool, progressive_cups: bool) -> dict[str, int]:
    items = {}
    if randomize_cups:
        if progressive_cups:
            index = CUP_NAMES.index(cup)
            if index > 0:
                items["Progressive Cup Unlock"] = index
        else:
            items[f'Cup Unlock - {cup}'] = 1

    if randomize_races:
        for race in RACES_BY_CUP[cup]:
            items[f'Course Unlock - {race}'] = 1

    return items

def get_required_race_items(race, randomize_races: bool, randomize_cups: bool, progressive_cups: bool) -> dict[str, int]:
    items = {}
    if randomize_races:
        items[f'Course Unlock - {race}'] = 1

    elif randomize_cups:
        # Only if randomize_races is False should we lock races until the cup is
        # unlocked
        if progressive_cups:
            index = CUP_NAMES.index(CUPS_BY_RACE[race])
            if index > 0:
                items["Progressive Cup Unlock"] = index
        else:
            items[f'Cup Unlock - {CUPS_BY_RACE[race]}'] = 1

    return items

def set_all_entrance_rules(world: GarfKartWorld):
    # Store these in a variable to reduce redundancy
    randomize_races = world.options.randomize_races == "races" or world.options.randomize_races == "cups_and_races"
    randomize_cups = world.options.randomize_races == "cups" or world.options.randomize_races == "cups_and_races"

    # Set cup unlock rules
    for cup in CUP_NAMES:
        cup_entrance = world.get_entrance(cup)
        required_items = get_required_cup_items(
            cup,
            randomize_races,
            randomize_cups,
            world.options.progressive_cups
        )

        if len(required_items) == 0:
            continue

        set_rule(cup_entrance, lambda state: state.has_all_counts(required_items, world.player))

    # Set race unlock rules
    for race in RACE_NAMES:
        race_entrance = world.get_entrance(race)
        required_items = get_required_race_items(
            race,
            randomize_races,
            randomize_cups,
            world.options.progressive_cups
        )

        if len(required_items) == 0:
            continue

        set_rule(race_entrance, lambda state: state.has_all_counts(required_items, world.player))

def set_all_location_rules(world: GarfKartWorld):
    randomize_cups = world.options.randomize_races == "cups" or world.options.randomize_races == "cups_and_races"

    if randomize_cups:
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
    randomize_races = world.options.randomize_races == "races" or world.options.randomize_races == "cups_and_races"
    randomize_cups = world.options.randomize_races == "cups" or world.options.randomize_races == "cups_and_races"

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

    elif world.options.goal == "races":
        race_names = [
            f'Unlock Course - {race}' for race in RACE_NAMES
        ]

        if randomize_races: 
            world.multiworld.completion_condition[world.player] = lambda state: state.has_all(race_names, world.player)
            
        elif randomize_cups:
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
    