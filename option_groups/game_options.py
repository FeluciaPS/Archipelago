from __future__ import annotations

from dataclasses import dataclass
from Options import Range, Toggle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..world import GarfKartWorld


class SingleLapMode(Toggle):
    """
    Races only have a single lap. This makes the game significantly harder, 
    especially on weak kart combos.

    This overrides Lap Count setting
    """
    display_name = "Single Lap Mode"

class LapCount(Range):
    """
    Modifies the amount of laps in a race, has no effect if single lap mode is on.
    """
    display_name = "Lap Count"
    default = 3

    range_start = 2
    range_end = 10

class DisableCPUItems(Toggle):
    """
    Prevents CPUs from using items for a less chaotic experience.

    Has no effect if Item Mania is enabled.
    """
    display_name = "Disable CPU Items"

class ItemMania(Toggle):
    """
    CPUs will always get 3 copies of items they get from item boxes. CPU items can't be
    disabled if this option is selected.

    !!!WARNING!!! This makes the game significantly harder and more frustrating to play,
    not for the faint of heart
    """
    display_name = "Item Mania"

class SpringsOnly(Toggle):
    """
    Item boxes can only give springs. This makes puzzle piece hunting a lot easier.
    """
    display_name = "Springs Only"