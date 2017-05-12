PRAGMA foreign_keys;

drop table if exists collections;
drop table if exists items;

create table collections(
    coll_id INTEGER PRIMARY KEY AUTOINCREMENT,
    coll_name TEXT NOT NULL
);

create table items(
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    coll_id INTEGER NOT NULL REFERENCES collections(coll_id)
);