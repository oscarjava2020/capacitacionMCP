from dataclasses import dataclass


@dataclass
class Item:
    item_id: int
    name: str
    description: str | None = None
