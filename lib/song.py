class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
       
        
        self.name = name
        self.artist = artist
        self.genre = genre
        

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre) if genre not in cls.genres else cls.genres
    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist) if artist not in cls.artists else cls.genres
    

    




pass
