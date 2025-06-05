from fastapi import FastAPI, HTTPException
from app.crud import get_all_fruits, get_fruit_by_id,get_fruit_by_name, add_fruit
from app.models import Fruit
import uvicorn

app = FastAPI()

@app.get("/fruits")
def read_fruits():
    return get_all_fruits()

@app.get("/fruits/{fruit_id}")
def read_fruit(fruit_id: int):
    fruit = get_fruit_by_id(fruit_id)
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return fruit

@app.get("/fruits/by-name/{fruit_name}")
def read_fruit_by_name(fruit_name: str):
    fruit = get_fruit_by_name(fruit_name)
    if not fruit:
        raise HTTPException(status_code=404, detail=f"{fruit_name} is not in the list.")
    return fruit

@app.post("/fruits")
def create_fruit(fruit: Fruit):
    try:
        return add_fruit(fruit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)