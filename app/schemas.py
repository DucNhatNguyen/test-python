from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, EmailStr, constr

class ProductSchema(BaseModel):
    name: str
    create_time: datetime
    price: int