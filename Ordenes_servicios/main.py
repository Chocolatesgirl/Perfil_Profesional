from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()
engine = create_engine("sqlite:///orders.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    dish_id = Column(Integer)
    status = Column(String, default="pendiente")

Base.metadata.create_all(bind=engine)

class OrderCreate(BaseModel):
    user_id: int
    dish_id: int

@app.post("/orders")
def create_order(order: OrderCreate):
    db = SessionLocal()
    new_order = Order(user_id=order.user_id, dish_id=order.dish_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"id": new_order.id, "user_id": new_order.user_id, "dish_id": new_order.dish_id, "status": new_order.status}

@app.get("/orders/{user_id}")
def get_orders(user_id: int):
    db = SessionLocal()
    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return [{"id": o.id, "dish_id": o.dish_id, "status": o.status} for o in orders]