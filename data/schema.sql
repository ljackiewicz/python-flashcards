drop table if exists cards;
create table cards (
    id      integer     primary key autoincrement,
    front   text        not null,
    back    text        not null
);
