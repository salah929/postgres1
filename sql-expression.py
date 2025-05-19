# This file is about using SQLAlchemy's Expression Language

from sqlalchemy import (
    create_engine, select, Table, Column, Float,
    ForeignKey, Integer, String, MetaData
)

"""
in this file, there are many code was written wrong in the video
because the course is very old and not updated
"""

db = create_engine("postgresql://postgres:admin@localhost:5432/chinook")
meta = MetaData()
meta.bind = db

artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

track_table = Table(
    "track", meta,
    Column("track_id", Integer, primary_key=True),
    Column("name", String),
    Column("album_id", Integer, ForeignKey("album_table.album_id")),
    Column("media_type_id", Integer, primary_key=False),
    Column("genre_id", Integer, primary_key=False),
    Column("composer", String),
    Column("milliseconds", Integer),
    Column("bytes", Integer),
    Column("unit_price", Float)
)

with db.connect() as connection:
    # select all records from artist table
    # select_query = select(artist_table)

    # select only the name column from artist table
    # select_query = select(artist_table.c.name)

    # select only "Queen" from the artist table
    # select_query = select(artist_table).where(artist_table.c.name == "Queen")

    # select only artist_id 51 from artist table
    # select_query = select(artist_table).where(artist_table.c.artist_id == 51)

    select_query = select(track_table).where(track_table.c.album_id == 219)
    results = connection.execute(select_query)
    for result in results:
        print(result)
