from .base_ids import BASE_ID_ITEM_INVENTORY, BASE_ID_ITEM_WORLD
from .items_inventory import BASE_ITEM_IDS as INVENTORY_ITEM_IDS
from .items_world import BASE_ITEM_IDS as WORLD_ITEM_IDS

ITEM_IDS = {}

for name in INVENTORY_ITEM_IDS:
    ITEM_IDS[name] = INVENTORY_ITEM_IDS[name] + BASE_ID_ITEM_INVENTORY

for name in INVENTORY_ITEM_IDS:
    ITEM_IDS[name] = INVENTORY_ITEM_IDS[name] + BASE_ID_ITEM_WORLD

def get_item_ids_by_name(names: list[str]):
    result = {}

    for name in names:
        result[name] = ITEM_IDS[name]
        
    return result

if __name__ == "__main__":
    # It's easier to get mod parity if I can easily output a list of item IDs
    with open("item_ids.txt", "w") as file:
        for item in ITEM_IDS:
            file.write(f'{item}: {ITEM_IDS[item]}')