from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory database
db = []

# Model for the item
class Item(BaseModel):
    name: str
    price: float

# Create an item
@app.post("/items/")
async def create_item(item: Item):
    db.append(item)
    return item

# Get all items
@app.get("/items/")
async def read_items():
    return db

# Get a single item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return db[item_id]

# Update an item
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    print(item_id, item)
    db[item_id] = item
    return {"item_id": item_id, "item": item}

# Delete an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    db.pop(item_id)
    return {"item_id": item_id}
