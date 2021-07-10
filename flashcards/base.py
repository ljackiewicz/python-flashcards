from flashcards.database import session, Card, Deck


def add_deck(name):
    session.add(Deck(name=name))
    session.commit()


def delete_deck(deck_id):
    deck = session.query(Deck).filter_by(id=deck_id).first()
    session.delete(deck)
    session.commit()


def list_decks():
    decks = session.query(Deck).all()

    if decks:
        print("Existing decks:")
        for deck in decks:
            print(f"{deck.id}: {deck.name}")
    else:
        print("There are no decks created yet")


def add_card(front, back, deck_id=1):
    session.add(Card(front=front, back=back, deck_id=deck_id))
    session.commit()


def delete_card(card_id):
    card = session.query(Card).filter_by(id=card_id).first()
    session.delete(card)
    session.commit()


def list_cards():
    cards = session.query(Card).all()

    if cards:
        print("Existing cards:")
        for card in cards:
            print(f"{card.id}: {card.front} - {card.back}")
    else:
        print("There are no cards created yet")


def main():
    list_decks()
    list_cards()


if __name__ == "__main__":
    main()
