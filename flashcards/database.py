from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE = "data/example.db"

engine = create_engine(f"sqlite:///{DATABASE}")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    front = Column(String, nullable=False)
    back = Column(String, nullable=False)

    def __repr__(self):
        return f"<Card(front='{self.front}', back='{self.back}')>"


Base.metadata.create_all(engine)
