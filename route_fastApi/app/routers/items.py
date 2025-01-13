from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_items():
    return {"items": ["Item1", "Item2", "Item3"]}

@router.post("/")
async def create_item(name: str):
    return {"message": f"Item {name} created successfully!"}
