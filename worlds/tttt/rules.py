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
    pass
