from sqlalchemy import *
from extentions import db

class Character(db.Model):
    id = Column(Integer , primary_key=True)
    name = Column(String(100) , nullable=False)
    desc = Column(Text , nullable=False)
    image_thumb = Column(String, nullable=False)
    image_full = Column(String , nullable=False)
    slug = Column(String(50) , unique=True , nullable=False)