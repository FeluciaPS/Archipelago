from __future__ import annotations

from dataclasses import dataclass
from Options import Choice, Toggle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..world import GarfKartWorld
    

class RandomizeCharacters(Toggle):
    """
    Adds characters to the item pool, and adds a location for winning a race as each character.
    """
    display_name = "Randomize Characters"

class RandomizeKarts(Toggle):
    """
    Adds karts to the item pool, and adds a location for winning a race with each kart.
    """
    display_name = "Randomize Karts"

class RandomizeHats(Choice):
    """
    Adds hats to the item pool

    - Off: Hats are unlocked in their vanilla locations
    - Progressive: Always unlock bronze hats first, then silver, then gold
    - Combine Tiers: Unlocking a hat instantly unlocks bronze, silver, and gold
    """
    display_name = "Randomize Hats"
    default = 0

    option_off = 0
    option_progressive = 1
    option_combine_tiers = 2

class RandomizeSpoilers(Choice):
    """
    Adds spoilers to the item pool

    - Off: Spoilers are unlocked in their vanilla locations
    - Progressive: Always unlock bronze spoilers first, then silver, then gold
    - Combine Tiers: Unlocking a spoiler instantly unlocks bronze, silver, and gold
    """
    display_name = "Randomize Spoilers"
    default = 0

    option_off = 0
    option_progressive = 1
    option_combine_tiers = 2

class StatRandomizer(Choice):
    """
    Randomizes the top speed, acceleration, and handling for Karts and/or Characters

    - Off: Karts and characters use their default values
    - Karts: Randomizes kart stats, not characters
    - Characters: Randomizes character stats, not karts
    - Both: Randomizes stats for both karts and characters.
    """
    display_name = "Stat Randomizer"
    default = 0

    option_off = 0
    option_karts  = 1
    option_characters = 2
    option_both = 3

class RandomStatValues(Choice):
    """
    Choose how high you want randomized stats to be. Note that these are just
    averages and outliers may still happen, they're just less likely.

    - Low: Stats are generally much lower than the base game
    - Medium: Stats are generally around the same as the base game
    - High: Stats are generally much higher than the base game
    """
    display_name = "Random Stat Values"
    default = 1

    option_low = 0
    option_medium = 1
    option_high = 2