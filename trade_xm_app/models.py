from enum import Enum
from pydantic import BaseModel


class OrderStatusEnum(str, Enum):
    PENDING = "PENDING"
    EXECUTED = "EXECUTED"
    CANCELLED = "CANCELLED"


class Order(BaseModel):
    id: int
    details: str
    status: OrderStatusEnum


class OrderCreate(BaseModel):
    details: str


class OrderUpdate(BaseModel):
    status: OrderStatusEnum
