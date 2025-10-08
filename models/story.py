from sqlalchemy import *
from extentions import db


class Story(db.Model):
    __tablename__ = "stories"
    id = Column(Integer , primary_key=True)
    title = Column(String(255),nullable=False)
    desc = Column(Text , nullable=True)
    slug = Column(String(255), unique=True , nullable=False)


    parts = db.relationship("StoryPart" , backref = "story" , cascade ="all,delete-orphan")

class StoryPart(db.Model) :
    __tablename__ = "story_parts"
    id = Column(Integer , primary_key=True)
    title = Column(String(255),nullable=False)
    content = Column(Text , nullable=False)

    story_id = Column(Integer , ForeignKey("stories.id") , nullable=False)