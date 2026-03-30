from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()
engine = create_engine("sqlite:///menu.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Dish(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

Base.metadata.create_all(bind=engine)

class DishCreate(BaseModel):
    name: str
    price: int

@app.post("/menu")
def add_dish(dish: DishCreate):
    db = SessionLocal()
    new_dish = Dish(name=dish.name, price=dish.price)
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return {"id": new_dish.id, "name": new_dish.name, "price": new_dish.price}

@app.get("/menu")
def get_menu():
    db = SessionLocal()
    dishes = db.query(Dish).all()
    return [{"id": d.id, "name": d.name, "price": d.price} for d in dishes]