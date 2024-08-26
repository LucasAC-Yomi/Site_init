import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv('.env')
link = os.getenv('DB')
engine = db.create_engine(link)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(engine)

class Usuario(Base):
    __tablename__ = 'usuario'    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    validation = Column(String, nullable=False)

def select_usuario():
    Table = Session()
    result = Table.query(Usuario).all()
    Table.close()
    return result