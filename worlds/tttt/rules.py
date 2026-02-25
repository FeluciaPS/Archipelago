from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import TTTTWorld


def set_all_rules(world: TTTTWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: TTTTWorld) -> None:
    pass


def set_all_location_rules(world: TTTTWorld) -> None:
    pass


def set_completion_condition(world: TTTTWorld) -> None:
    # Redundant if statement because no other goals are planned right now
    if world.options.goal == "space":
        world.multiworld.completion_condition[world.player] = lambda state: state.has_all_counts({
            "Turbo Upgrade": world.options.turbo_requirement
        }, world.player)

    else:
        # Exact same goal because I don't like it when there's if statements without a fallback
        world.multiworld.completion_condition[world.player] = lambda state: state.has_all_counts({
            "Turbo Upgrade": world.options.turbo_requirement
        }, world.player)