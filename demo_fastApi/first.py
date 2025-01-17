from fastapi import FastAPI
#from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter
router = APIRouter()



@router.get("/first")    # default one
async def read_first():
    return [{"item_id": "Dynamic Route done. Shoaib!"}]


