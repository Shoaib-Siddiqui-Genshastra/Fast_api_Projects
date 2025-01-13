from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@router.post("/")
async def create_user(name: str):
    return {"message": f"User {name} created successfully!"}
