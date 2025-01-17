from fastapi import APIRouter
router = APIRouter()

@router.get("/products/{product_id}")
async def get_products(product_id: int, q: str = "Products"):
    return {"product_id": product_id, "q": q}


@router.post("/products")
async def create_product(name = str):
    return {"message": f"Product '{name}' created successfully!"}
