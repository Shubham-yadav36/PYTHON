from cx_Oracle import *
from traceback import *


class Model:
    def __init__(self):
        self.song_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None
        try:
            self.conn = connect("musicapp/Shubham36@localhost:1522/orcl")
            self.cur = self.conn.cursor()
            print("Connected Successfully.")
        except DatabaseError:
            self.db_status = False
            print("Database connection interupted : ", format_exc())

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
            print("Disconnected Successfully.")

    def add_song(self, song_name, song_path):
        self.song_dict[song_name] = song_path
        print("Song Added : ", self.song_dict[song_name])

    def get_song_path(self, song_name):
        return self.song_dict[song_name]

    def remove_song(self, song_name):
        return self.song_dict.pop(song_name)
        print("Song Deleted.")
        print("Now Playlist : ", self.song_dict)

    def search_song_in_favourites(self, song_name):
        songs = self.cur.execute("SELECT SONG_NAME FROM MYFAVOURITES WHERE SONG_NAME=:1", (song_name,))
        song_tuple = self.cur.fetchone()
        if song_tuple is None:
            return False
        return True

    def add_song_in_favourites(self, song_name, song_path):
        is_present = self.search_song_in_favourites(song_name)
        if not is_present:
            return "Song Already Present in Favourites."
        self.cur.execute("SELECT MAX(SONG_ID) FROM MYFAVOURITES")
        last_song_id = self.cur.fetchone()[0]
        next_song_id = 1
        if last_song_id is not None:
            next_song_id = last_song_id + 1
        self.cur.execute("INERT INTO MYFAVOURITES VALUES(:1,:2,:3)", (next_song_id, song_name, song_path))
        self.conn.commit()
        return "Song Successfully Added to Your Favourites."

    def load_songs_from_favourites(self):
        self.cur.execute("SELECT SONG_NAME,SONG_PATH FROM MYFAVOURITES")
        is_song = True
        for song_name, song_path in self.cur:
            self.song_dict[song_name] = song_path
            is_song = False

        if is_song:
            return "List Populated From Favourites."
        else:
            return "No Song Present in Favourites."

    def remove_song_from_favourites(self, song_name):
        self.cur.execute("delete from MYFAVOURITES where song_name=:1", (song_name,))
        count = self.cur.rowcount
        if count == 0:
            return "Song Not Present In Your Favourites."
        else:
            self.song_dict.pop(song_name)
            self.conn.commit()
            return "Song Successfully Removed From Favourites."


