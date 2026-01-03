# Item IDs
BASE_ID_ITEM_INVENTORY = 0 # 74 inventory items
BASE_ID_ITEM_WORLD = 100 # Everything else is world state item

# Location IDs
BASE_ID_LOCATION_EQUIPMENT = 0 # 0-10: Shovel, pipe, sunglasses, cape
BASE_ID_LOCATION_QUEST_ITEM = 10 # 10-20: 4 wind chimes + government docs
BASE_ID_LOCATION_CRITTER = 20 # 20-30: 10 critters (first time catch only)
BASE_ID_LOCATION_MONEY_PILE = 30 # 30-40: 2 steelkees trash money + 1 crab money
BASE_ID_LOCATION_JUNK_CLUSTER = 40 # 40-50: 7 turbo junk clusters
BASE_ID_LOCATION_TTC_QUEST = 60 # 60-70: 9 quest completions that normally give a dig spot
BASE_ID_LOCATION_BURIED_TTC = 70 # 70-80: 9 trash can dig spots
BASE_ID_LOCATION_TTC = 80 # 80-100: 12 trash cans
BASE_ID_LOCATION_BLUEPRINT = 100 # 100-110: 7 pet blueprints
BASE_ID_LOCATION_PET = 100 # 110-120: 7 pets
BASE_ID_LOCATION_SHOP = { # 150-275: Max 25 items per shop
    "Beach Club": 150,
    "Hat Store (Blue)": 175,
    "Hat Store (Green)": 200,
    "Hat Store (Red)": 225,
    "Junk Store": 250,
}
BASE_ID_LOCATION_UPGRADE = 275 # 275-300: 25 turbo upgrades should be enough
BASE_ID_LOCATION_QUEST = 300 # 300-700 reserved for world events and quests
BASE_ID_LOCATION_BURIED_JUNK = 700 # 700-750: 27 buried turbo junk clusters
BASE_ID_LOCATION_DIG = 750 # 750-1000 reserved for money dig spots
BASE_ID_LOCATION_JUNK = 1000 # 1000-2000 reserved for individual turbo junk