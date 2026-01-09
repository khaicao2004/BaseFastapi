from typing import Optional, Union, Annotated
from fastapi import FastAPI, Query,Path, HTTPException
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

app = FastAPI()

fake_database = [
    {"id": 1, "name": "Ao mua", "description": "Day la ao mua giup khong bi uot"},
    {"id": 2, "name": "Ao khoac", "description": "Day la ao khoac"},
    {"id": 3, "name": "Ao phao", "description": "Day la ao phao"},
    {"id": 4, "name": "Ao thun", "description": "Day la ao thun"},
    {"id": 5, "name": "Ao sweater", "description": "Day la ao sweater"},
    {"id": 6, "name": "Ao so mi", "description": "Day la ao so mi"},
    {"id": 7, "name": "Ao len", "description": "Day la ao len"},
    {"id": 8, "name": "Ao gio", "description": "Day la ao gio"},
    {"id": 9, "name": "Ao coc", "description": "Day la ao coc"},
    {"id": 10, "name": "Ao khoac da", "description": "Day la ao khoac da"}
]

@app.get('/')
def root():
    return 'Hello world'

@app.get('/items')
def get_items(page: int = Query(1, ge=1), page_size: int = Query(3, ge=1, le=100), q: Annotated[Union[str, None], Query(max_length=50)] = None):
    total = len(fake_database)
    skip = (page - 1) * page_size
    # start = skip
    # end = skip + page_size
    item = fake_database[skip: skip + page_size] #[start: end]

    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "item": item,
        "q": q
    }

@app.get('/items/{item_id}')
def get_item_detail(item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],):
    for item in fake_database:
        if item["id"] == item_id:
            return item

    raise HTTPException(status_code=404, detail="Item not found")