CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    artist_name VARCHAR
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    album_title VARCHAR,
    artist_id VARCHAR REFERENCES artist(id),
);

CREATE TABLE song(
    id INTEGER PRIMARY KEY,
    song_title VARCHAR,
    album_id VARCHAR REFERENCES album(id),
    track_num INTEGER,
    song_length INTEGER
);