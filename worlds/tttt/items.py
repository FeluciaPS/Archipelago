from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import TTTTWorld

ITEM_NAME_TO_ID = {}

class TTTTItem(Item):
    game = "Tiny Terry's Turbo Trip"

def get_random_filler_item_name(world: TTTTWorld) -> str:
    return "Filler Item"


def create_item_with_correct_classification(world: TTTTWorld, name: str) -> TTTTItem:
    pass

def create_all_items(world: TTTTWorld) -> None:
    pass