from flashcards.database import session, Card


def add_card(front, back):
    session.add(Card(front=front, back=back))
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
    list_cards()


if __name__ == "__main__":
    main()
