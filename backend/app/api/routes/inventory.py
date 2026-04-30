from fastapi import APIRouter
from typing import List
from app.db import get_database
from app.models.inventory import InventoryDB

router = APIRouter()

@router.get("/", response_model=List[InventoryDB])
async def get_inventory():
    db = get_database()
    cursor = db.inventario.find()
    items = await cursor.to_list(length=1000)
    for item in items:
        item["_id"] = str(item["_id"])
    return items

@router.post("/")
async def create_inventory_item():
    return {"message": "item created"}
