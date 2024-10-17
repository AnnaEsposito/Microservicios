from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class pibData(Base):
    __tablename__ = "gdp_data"
    
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String, index=True)
    año = Column(Integer)
    pib_valor = Column(Float)