from fastapi import FastAPI
from first import router as first_router
from products import router as products_router
from pydantic import BaseModel
from typing import Optional


 # instance
app = FastAPI(
    title="My Custom API",
    description="This is a custom API with enhanced documentation.",
    version="1.0.0",
    openapi_tags=[
        {"name": "root", "description": "Root endpoint"},
        {"name": "items", "description": "Operations with items"}
    ],
    openapi_external_docs={
        "description": "Find more info here",
        "url": "https://example.com/docs"
    }
)


app.include_router(first_router)
app.include_router(products_router)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Sample Item",
                "price": 29.99,
                "is_offer": True
            }
        }


@app.get("/", tags=["root"], summary="Root Endpoints ", description="Returns a greeting message.")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/", tags=["root"], summary="Root Endpoint", description="Returns a greeting message.")
async def read_root():
    return {"Hello": "All items"}

@app.post("/items/", tags=["items"], summary="Create an Item",
          description="Creates an item with the specified attributes.")
async def create_item(item: Item):
    return item


@app.get("/items/{item_id}", tags=["items"], summary="Get an Item", description="Retrieves an item by its ID.")
async def read_item(item_id: int, q: Optional[str] = None):
    """
    Retrieve an item by its ID.

    - **item_id**: The ID of the item to retrieve.
    - **q**: Optional query string parameter.
    """
    return {"item_id": item_id, "q": q}


