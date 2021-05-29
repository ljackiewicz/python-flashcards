drop table if exists decks;
create table decks (
    id      integer     primary key,
    name    text        not null
);

drop table if exists cards;
create table cards (
    id      integer     primary key,
    front   text        not null,
    back    text        not null,
    deck_id integer     not null,

    foreign key (deck_id)
        references decks(id)
            on update cascade
            on delete cascade
);

insert into decks (name) values ('default');
