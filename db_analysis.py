from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String 

base_model = declarative_base()

#tabla_analysis
var1= Column(Integer, nullable=False)