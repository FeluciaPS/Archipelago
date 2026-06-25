from __future__ import annotations

from dataclasses import dataclass
from Options import Choice, Toggle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..world import GarfKartWorld


class RandomizeRaces(Choice):
    """
    Sets how to shuffle race unlocks into the item pool

    - Cups: Grand Prix cup unlocks are shuffled into the item pool, races unlock when you unlock their cup
    - Races: Race unlocks are shuffled into the item pool, cups unlock when you've unlocked all races in the cup
    - Cups and Races: Race and cup unlocks are shuffled into the item pool, playing a cup requires all 4 races and the cup item

    Note: "Cups and Races" is incompatible with Progressive Cups - if both are enabled,
    Progressive Cups will be automatically disabled.
    """
    display_name = "Randomize Races"
    default = 0

    option_cups = 0
    option_races = 1
    option_cups_and_races = 2

class ProgressiveCups(Toggle):
    """
    Starts the game with the first cup onlocked, then unlocks them in order
    every time a "Cup Unlock" item is found.
    Turning this off unlocks cups in random order with their specific items.

    This option does nothing if cups aren't randomized.

    Note: This option is automatically disabled if Randomize Races is set to "Cups and Races".
    """
    display_name = "Progressive Cups"