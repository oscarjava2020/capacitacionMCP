from fastapi import HTTPException

from fast_api.models.item import Item
from fast_api.schemas.item import ItemCreate

# In-memory store used as a placeholder for a real database/repository.
_items: dict[int, Item] = {}
_next_id = 1


def list_items() -> list[Item]:
    return list(_items.values())


def get_item(item_id: int) -> Item:
    item = _items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def create_item(data: ItemCreate) -> Item:
    global _next_id
    item = Item(item_id=_next_id, name=data.name, description=data.description)
    _items[item.item_id] = item
    _next_id += 1
    return item


def delete_item(item_id: int) -> None:
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
