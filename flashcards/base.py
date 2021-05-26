from flashcards.database import query_db, init_db


def list_cards():
    query = "SELECT id, front, back FROM cards"
    cards = query_db(query)

    for card in cards:
        print(f"{card['id']}: {card['front']} - {card['back']}")


def add_card(front, back):
    query = "INSERT INTO cards (front, back) VALUES (?, ?)"
    query_db(query, [front, back])


def remove_card(card_id):
    query = "DELETE FROM cards WHERE id=?"
    query_db(query, [card_id])


def main():
    init_db()

    list_cards()


if __name__ == "__main__":
    main()
