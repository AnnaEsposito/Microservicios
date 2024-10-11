from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine =create_engine()
SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine)