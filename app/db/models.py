from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    category = Column(String(100))
    unit = Column(String(50))  # pieces, kg, litres, etc
    created_at = Column(DateTime, default=datetime.utcnow)
    
    sales = relationship("SalesRecord", back_populates="product")
    inventory = relationship("Inventory", back_populates="product")
    forecasts = relationship("Forecast", back_populates="product")

class SalesRecord(Base):
    __tablename__ = "sales_records"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    store_id = Column(Integer)  # Optional store/location identifier
    date = Column(DateTime, nullable=False, index=True)
    quantity_sold = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    product = relationship("Product", back_populates="sales")

class Inventory(Base):
    __tablename__ = "inventory"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    store_id = Column(Integer)
    current_stock = Column(Float, nullable=False)
    safety_stock = Column(Float, default=0)
    lead_time_days = Column(Integer, default=7)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    product = relationship("Product", back_populates="inventory")

class Forecast(Base):
    __tablename__ = "forecasts"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    store_id = Column(Integer)
    forecast_date = Column(DateTime, nullable=False, index=True)
    forecasted_demand = Column(Float, nullable=False)
    confidence = Column(Float, default=0.0)
    model_version = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    product = relationship("Product", back_populates="forecasts")
