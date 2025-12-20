from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, DefaultOnToggle, OptionCounter, Toggle, Visibility
from .data.shops import SHOP_NAMES, DEFAULT_SHOP_ITEM_COUNTS

################
# Shop Options #
################
class RandomizeShopItems(DefaultOnToggle):
    """
    Shuffles items normally bought in the 5 shops into the itempool, and offers random
    items in their place in the shops. 

    If shops are NOT randomized, all shops must have at least their vanilla item count in
    the shop_item_count option.
    """
    display_name = "Randomize Shop Items"


class RandomizeShopPrices(Choice):
    """
    Choose how shop prices are randomized.

    - off: Buyable TTTT items use their default prices, all other items cost 100 money
    - even: All shop items cost roughly 100 money
    - sphere: Shop prices get higher if later into a playthrough
    - item_type: Progression items are more expensive, filler items cheaper
    - item_type_and_sphere: Combines the above 2 options
    """

    display_name = "Randomize Shop Prices"

    option_off = 0
    option_even = 1
    option_sphere = 2
    option_item_type = 3
    option_item_type_and_sphere = 4

    default = option_off

class ShopPriceMultiplier(Range):
    """
    Scale all shop prices by a percentage. Works even if shop prices aren't randomized.
    If set to 0, all shop items are free.
    """
    display_name = "Shop Price Multiplier"

    range_start = 0
    range_end = 300

    default = 100

class ShopItemCount(OptionCounter):
    """
    Set the amount of items offered at each shop in the game.
    Each shop must have at least 1 and at most 25 items.

    If shop items aren't randomized, the minimum value is equal to the default, and 
    slots above the default are filled with random items.
    """
    display_name  = "Shop Item Counts"
    min = 1
    max = 25
    default = {shop: count for shop, count in DEFAULT_SHOP_ITEM_COUNTS}
    valid_keys = SHOP_NAMES

#################
# Silly Options #
#################
class DutchItemNames(Toggle):
    """
    In the spirit of TTTT, replaces archipelago item names with Dutch ones.
    """
    display_name = "Dutch Item Names"

    # Maybe: visibility = Visibility.template | Visibility.complex_ui | Visibility.spoiler
    # Probably shouldn't be visible by default on an options page, but for now
    # I'm only putting it in spoiler logs.
    visibility = Visibility.spoiler

@dataclass
class TTTTOptions(PerGameCommonOptions):
    randomize_shop_items: RandomizeShopItems
    randomize_shop_prices: RandomizeShopPrices
    shop_price_multiplier: ShopPriceMultiplier
    shop_item_count: ShopItemCount

option_groups = [
    OptionGroup(
        "Shop Options",
        [RandomizeShopItems, RandomizeShopPrices, ShopPriceMultiplier, ShopItemCount],
    ),
    OptionGroup(
        "Silly Options",
        [DutchItemNames],
    )
]

option_presets = {}
