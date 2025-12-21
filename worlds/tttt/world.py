from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world

class TTTTWorld(World):
    game = "Tiny Terry's Turbo Trip"

    options_dataclass = options.TTTTOptions
    options: options.TTTTOptions