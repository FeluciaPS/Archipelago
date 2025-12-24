from __future__ import annotations

# Logic goes here
# Logic goes here

from .items import get_n_puzzle_pieces
from .data import KART_NAMES, CHARACTER_NAMES, CUP_NAMES, CUPS_BY_RACE, ITEM_NAMES, PUZZLE_PIECE_REQUIREMENTS, RACE_NAMES, RACES_BY_CUP, PuzzlePieceRequirements
from .options import RandomizerType, is_cups_randomized, is_races_randomized

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
    randomize_races = is_races_randomized(world) == RandomizerType.random
    randomize_cups = is_cups_randomized(world) == RandomizerType.random

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

        set_rule(cup_entrance, lambda state, items=required_items: state.has_all_counts(items, world.player))

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

        set_rule(race_entrance, lambda state, items=required_items: state.has_all_counts(items, world.player))

def set_all_location_rules(world: GarfKartWorld):

    # Winning a race as a character also requires having the character unlock
    if world.options.randomize_characters:
        for character in CHARACTER_NAMES:
            location = world.get_location(f'Win Race as {character}')
            set_rule(location, lambda state, c=character: state.has(c, world.player))

    # And same for karts
    if world.options.randomize_karts:
        for kart in KART_NAMES:
            location = world.get_location(f'Win Race with {kart}')
            set_rule(location, lambda state, k=kart: state.has(k, world.player))

    # Certain puzzle pieces require a Spring or Lasagna item to be accessed
    if world.options.randomize_puzzle_pieces and world.options.randomize_items:
        for race in PUZZLE_PIECE_REQUIREMENTS:
            for piece in PUZZLE_PIECE_REQUIREMENTS[race]:
                location = world.get_location(f'{race}: Puzzle Piece {piece}')
                required_items = [
                    "Item Unlock - Spring"
                ]

                if PUZZLE_PIECE_REQUIREMENTS[race][piece] == PuzzlePieceRequirements.Either and not world.options.springs_only:
                    required_items.append("Item Unlock - Lasagna")

                set_rule(location, lambda state, items=required_items: state.has_any(items, world.player))

    # Item acquisition locations can't be accessed until you have the associated item
    if world.options.randomize_items:
        if world.options.springs_only:
            location = world.get_location("Find Item: Spring")
            set_rule(location, lambda state: state.has("Item Unlock - Spring", world.player))
        else:
            for item in ITEM_NAMES:
                location = world.get_location(f'Find Item: {item}')
                set_rule(location, lambda state: state.has(f"Item Unlock - {item}", world.player))

def set_completion_condition(world: GarfKartWorld):
    randomize_races = is_races_randomized(world) == RandomizerType.random
    randomize_cups = is_cups_randomized(world) == RandomizerType.random

    # Build on a single required_items dict, adding required items depending
    # on various victory conditions, this is nice because a lot of them have
    # partial overlap
    required_items = {}

    if world.options.goal == "grand_prix":
        # The game can be completed if all cups can be reached
        for cup in CUP_NAMES:
            required_items = {
                **required_items, 
                **get_required_cup_items(cup, randomize_races, randomize_cups, world.options.progressive_cups)
            }

    if world.options.goal in ["races", "time_trials"]:
        # All races need to be accessible to beat the game
        for race in RACE_NAMES:
            required_items = {
                **required_items, 
                **get_required_race_items(race, randomize_races, randomize_cups, world.options.progressive_cups)
            }

    if world.options.goal == "time_trials":
        # TODO: Platinum time trials require specific items to beat, 
        # but for now we just assume they're always beatable
        pass

    if world.options.goal == "puzzle_piece_hunt":
        puzzle_pieces_in_pool = get_n_puzzle_pieces(world.options.puzzle_piece_count)
        for puzzle_piece in puzzle_pieces_in_pool:
            required_items[puzzle_piece] = 1

    world.multiworld.completion_condition[world.player] = lambda state: state.has_all_counts(required_items, world.player)

    