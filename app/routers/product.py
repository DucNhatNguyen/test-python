from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .. import models, schemas
from ..database import get_db
from pydantic import BaseModel
from datetime import datetime

class ProductSchema(BaseModel):
    name: str
    create_time: datetime
    price: int

class ProductUpdateSchema(BaseModel):
    name: str
    create_time: datetime
    price: int

router = APIRouter()

@router.get('/')
def get_products(db: Session = Depends(get_db)):
    data = db.query(models.Product).all()
    return {'status': 200, 'response': data}

@router.post('/')
def create_product(prod: ProductSchema, db: Session = Depends(get_db)):
    product_query = models.Product(name=prod.name, create_time=prod.create_time, price=prod.price)
    db.add(product_query)
    db.commit()
    db.refresh(product_query)
    return {'status': 200, 'response': product_query}

@router.put('/')
def update_product(id:int, prod: ProductUpdateSchema, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(models.Product.id == id)
    updated_product = product_query.first()

    if not updated_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id: '{id}' not found")
    
    product_query.update(prod.model_dump(), synchronize_session=False)
    db.commit()
    return updated_product

@router.get('/{id}')
def get_by_id(id:int, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(models.Product.id == id)
    prod_by_id = product_query.first()

    if not prod_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id: '{id}' not found")
    
    return prod_by_id

@router.delete('/{id}')
def delete_product(id:int, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(models.Product.id == id)
    prod_by_id = product_query.first()

    if not prod_by_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id: '{id}' not found")
    
    product_query.delete(synchronize_session=False)
    db.commit()
    
    return {'status': status.HTTP_200_OK, 'msg': "Xoa San pham thanh cong!"}