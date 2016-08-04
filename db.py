import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class DBImage(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    width = Column(Integer)
    height = Column(Integer)
    ctime = Column(DateTime)
    exif_time = Column(DateTime)

    def __init__(self, path, name, width, height, ctime, exif_time):
        self.path = path
        self.name = name
        self.width = width
        self.height = height
        self.ctime = ctime
        self.exif_time = exif_time

    def __repr__(self):
        return "{}, width: {}, height: {}, ctime: {}, exif_time: {}".format(self.name, self.width, self.height, self.ctime, self.exif_time)
 
class Database:
    def __init__(self):
        self.engine = create_engine("sqlite:///tmp.db", echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, image):
        session = self.Session()
        session.add(image)
        session.commit()
        print("Added image {}.".format(image))
