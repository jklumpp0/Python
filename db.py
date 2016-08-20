import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
class DBImage(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    width = Column(Integer)
    height = Column(Integer)
    model = Column(String)
    ctime = Column(DateTime)
    exif_time = Column(DateTime)
    size = Column(Integer)

    def __init__(self, path, name, camera_model, width, height, ctime, exif_time):
        self.path = path
        self.name = name
        self.width = width
        self.height = height
        self.ctime = ctime
        self.exif_time = exif_time
        self.model = camera_model
        self.size = os.stat(self.path).st_size

    def __repr__(self):
        return "{}, model: {}, width: {}, height: {}, ctime: {}, exif_time: {}, size: {}".format(self.name, self.model, self.width, self.height, self.ctime, self.exif_time, self.size)
 
class Database:
    def __init__(self):
        self.engine = create_engine("sqlite:///tmp.db", echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, image):
        session = self.Session()
        session.add(image)
        session.commit()
        print("Added image {}.".format(image))
