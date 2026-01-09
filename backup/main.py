from typing import Optional, Union
from fastapi import FastAPI, Query
from pydantic import BaseModel
from datetime import datetime
import asyncio
from enum import Enum

app = FastAPI()

@app.get('/')
def get_root():
    return 'Hello world'

@app.get('/hello/{item_id}')
async def read_item(item_id):
    return {"item_id": item_id}

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

# def process_items(items: list[str]):
#     for item in items:
#         print(item)

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

print(get_root())
print(get_full_name("john", "doe"))
print(get_name_with_age("Khai", 21))
print(get_items("Khai", 21, 2.4, True, 0))
# print(process_items([1,2,3,4]))
print(process_items([1,2,3], [2]))



class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Union[datetime, None] = None
    friends: list[int] = []

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

user = User(**external_data)
print(user)

# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123
def get_items(price:  float, age: int):
	return "Price: " + str(price) + " Age: " + str(age)

print(get_items(2000, 40))

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi()


class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

p = Person("Khai")
print(get_person_name(p))

@app.get("/io-task")
async def io_task():
    print("Start waiting...")
    await  asyncio.sleep(2)   # giả lập gọi DB / API
    print("Done!")
    return {"message": "IO task finished"}


import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"},
    {"id": 3, "name": "C"},
    {"id": 4, "name": "D"},
    {"id": 5, "name": "E"},
    {"id": 6, "name": "F"},
    {"id": 7, "name": "G"},
    {"id": 8, "name": "H"},
    {"id": 9, "name": "I"},
    {"id": 10, "name": "J"},
]

@app.get("/items")
def get_items(page: int = Query(1, ge=1), page_size: int = Query(3, ge=1, le=100)):
    total = len(fake_items_db)

    skip = (page - 1) * page_size
    limit = page_size

    items = fake_items_db[skip : skip + limit]

    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "items": items
    }

class NewProject(BaseModel):
    name: str
    description: str | Union[str | None] = None

async def create_project(project: NewProject):
    return project
