from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()



class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# @router.get("/test")
# def get_test(q:str = Query('test',alias='item-query',deprecated=True),data:str=Query(None,alias='data')):
#     return {"item-query":q ,  "data":data}