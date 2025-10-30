# Pretty much copied verbatim from
# https://github.com/NewSoupVi/Archipelago/blob/apquest/worlds/apquest/web_world.py
# for the time being

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class GarfKartWebWorld(WebWorld):
    game = "Garfield Kart - Furious Racing"
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Garfield Kart for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["FeluciaPS"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets