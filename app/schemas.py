from pydantic import BaseModel
from typing import Optional

class RawProduct(BaseModel):
    product: str
    quantity: Optional[str] | Optional[int]
    price: Optional[str] | Optional[float]
    order_date: Optional[str]
