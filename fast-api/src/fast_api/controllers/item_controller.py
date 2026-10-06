from fastapi import APIRouter

from fast_api.schemas.item import ItemCreate, ItemResponse
from fast_api.services import item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[ItemResponse])
def read_items():
    return item_service.list_items()


@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    return item_service.get_item(item_id)


@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate):
    return item_service.create_item(item)


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    item_service.delete_item(item_id)
