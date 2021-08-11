from flask import Flask, redirect, render_template, url_for

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    if playlist:
        return render_template('playlist.html', playlist=playlist)
    return redirect(url_for('show_all_playlists'))


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    form = PlaylistForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        playlist = Playlist(name=name, description=description)
        db.session.add(playlist)
        db.session.commit()
        return redirect(url_for('show_all_playlists'))
    
    return render_template('new_playlist.html', form=form)


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    song = Song.query.get(song_id)
    if song:
        print(song.playlists)
        return render_template('song.html', song=song)
    return redirect(url_for('show_all_songs'))


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    form = SongForm()
    if form.validate_on_submit():
        title = form.title.data
        artist = form.artist.data
        song = Song(title=title, artist=artist)
        db.session.add(song)
        db.session.commit()
        return redirect(url_for("show_all_songs"))
    
    return render_template('new_song.html', form=form)


@app.route("/playlists/<playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""
    playlist = Playlist.query.get_or_404(playlist_id)
    print(playlist.songlists)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    curr_on_playlist = [song.title for song in playlist.songlists]
    form.song.choices = [(int(song.id), song.title.title()) for song 
                            in Song.query.all() if song.title not in curr_on_playlist]

    if form.validate_on_submit():
        song = Song.query.get_or_404(form.song.data)
        song.playlist_id = playlist_id
        song_playlist = PlaylistSong(playlist_id=int(playlist_id), song_id=int(song.id))
        db.session.add(song)
        db.session.add(song_playlist)
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
