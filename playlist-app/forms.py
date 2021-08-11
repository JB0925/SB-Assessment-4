"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Playlist Name", 
                        validators=[DataRequired("Playlist must have a title.")],
                        render_kw={"placeholder": "Enter the Playlist Name"})
    
    description = StringField("Playlist Description", 
                        validators=[DataRequired("Enter a brief description")],
                        render_kw={"placeholder": "Enter a Playlist Description"})

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", 
                        validators=[DataRequired("Song must have a title.")],
                        render_kw={"placeholder": "Enter the Song Title"})
    
    artist = StringField("Artist", 
                        validators=[DataRequired("Enter the artist name.")],
                        render_kw={"placeholder": "Enter the Artist"})


class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
