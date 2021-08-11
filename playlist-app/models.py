"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = "playlists"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    songlists = db.relationship("Song", secondary="playlist_songs", backref="playlists")


class Song(db.Model):
    """Song."""

    __tablenamme__ = "song"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey(Playlist.id))
    

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = "playlist_songs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(Playlist.id, ondelete="cascade"), nullable = False, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey(Song.id, ondelete="cascade"), nullable=False, primary_key=True)   


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
