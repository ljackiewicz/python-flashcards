from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE = "data/example.db"

engine = create_engine(f"sqlite:///{DATABASE}")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    cards = relationship("Card", order_by="Card.id",
                         cascade="all, delete-orphan", back_populates="deck")

    def __repr__(self):
        return f"<Deck(name='{self.name}')>"


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    front = Column(String, nullable=False)
    back = Column(String, nullable=False)
    deck_id = Column(Integer, ForeignKey('decks.id'), nullable=False)

    deck = relationship("Deck", back_populates="cards")

    def __repr__(self):
        return f"<Card(front='{self.front}', back='{self.back}')>"


Base.metadata.create_all(engine)
