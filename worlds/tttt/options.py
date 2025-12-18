from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class RandomPrices(Choice):
    """
    Choose how shop prices are randomized. 

    - off: No price randomizer
    - even: All random shop items are roughly the same price
    - sphere: Shop prices get higher if later into a playthrough
    - item_type: Progression items are more expensive, filler items cheaper
    - item_type_and_sphere: Combines the prior 2 options
    """

    display_name = "Randomize Shop Prices"

    option_off = 0
    option_even = 1
    option_sphere = 2
    option_item_type = 3
    option_item_type_and_sphere = 4

    default = option_off


@dataclass
class TTTTOptions(PerGameCommonOptions):
    randomize_shop_prices: RandomPrices


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Shop Options",
        [RandomPrices],
    )
]

option_presets = {}
