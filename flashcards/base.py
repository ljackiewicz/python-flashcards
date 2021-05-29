from flashcards.database import Database


def list_cards():
    with Database() as db:
        cards = db.execute("SELECT id, front, back FROM cards").fetchall()

    for card in cards:
        print(f"{card['id']}: {card['front']} - {card['back']}")


def add_card(front, back):
    with Database() as db:
        db.execute("INSERT INTO cards (front, back, deck_id) VALUES (?, ?, ?)", front, back, 1)
        db.commit()


def remove_card(card_id):
    with Database() as db:
        db.execute("DELETE FROM cards WHERE id=?", card_id)
        db.commit()


def main():
    print("Already created cards:")
    list_cards()


if __name__ == "__main__":
    main()
