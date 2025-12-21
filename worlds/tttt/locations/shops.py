from ..world import TTTTWorld


BASE_SHOP_LOCATION_IDS = {
    "Beach Club": 100,
    "Hat Store (Blue)": 125,
    "Hat Store (Green)": 150,
    "Hat Store (Red)": 175,
    "Junk Store": 200,
}

def get_all_shop_locations(world: TTTTWorld):
    locations = {}

    for shop in BASE_SHOP_LOCATION_IDS:
        item_count = world.options.shop_item_count[shop]
        base_id = BASE_SHOP_LOCATION_IDS[shop]
        for i in range(item_count):
            locations[f"{shop}: Item {i+1}"] = base_id + i

    return locations

def get_shop_location_id(world: TTTTWorld, shopName: str, itemIndex: int):
    locations = get_all_shop_locations(world)
    return locations[f'{shopName}: Item {itemIndex}']