create table if not exists notes  (
    title text not null primary key,
    content text not null
);

create table if not exists metadata    (
    title text not null,
    meta_key text not null,
    meta_value text not null,
    
    UNIQUE (title, meta_key),
    Foreign key (title) references notes (title) ON DELETE CASCADE ON UPDATE CASCADE
);