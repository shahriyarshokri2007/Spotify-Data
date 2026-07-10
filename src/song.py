class Song:
    def __init__(self, track_id, artists, album_name, track_name, popularity, duration_ms,
                 explicit, danceability, energy, key, loudness, mode, speechiness,
                 acousticness, instrumentalness, liveness, valence, tempo,
                 time_signature, track_genre):

        self.track_id = track_id
        self.artists = artists
        self.album_name = album_name
        self.track_name = track_name
        self.popularity = popularity
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.time_signature = time_signature
        self.track_genre = track_genre

    @property
    def popularity(self):
        return self._popularity

    @popularity.setter
    def popularity(self, value):
        value = int(value)
        if 0 <= value <= 100:
            self._popularity = value
        else:
            raise ValueError(f"popularity must be between 0 and 100, got: {value}")

    @property
    def duration_ms(self):
        return self._duration_ms

    @duration_ms.setter
    def duration_ms(self, value):
        value = int(value)
        if value > 0:
            self._duration_ms = value
        else:
            raise ValueError(f"duration_ms must be positive, got: {value}")

    @property
    def explicit(self):
        return self._explicit

    @explicit.setter
    def explicit(self, value):
        if isinstance(value, bool):
            self._explicit = value
        elif isinstance(value, str):
            if value.strip().lower() == "true":
                self._explicit = True
            elif value.strip().lower() == "false":
                self._explicit = False
            else:
                raise ValueError(f"explicit must be True or False, got: {value}")
        elif isinstance(value, int) and value in (0, 1):
            self._explicit = bool(value)
        else:
            raise ValueError(f"explicit must be True or False, got: {value}")

    @property
    def danceability(self):
        return self._danceability

    @danceability.setter
    def danceability(self, value):
        value = float(value)
        if 0 <= value <= 1:
            self._danceability = value
        else:
            raise ValueError(f"danceability must be between 0 and 1, got: {value}")

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        value = float(value)
        if 0 <= value <= 1:
            self._energy = value
        else:
            raise ValueError(f"energy must be between 0 and 1, got: {value}")

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        value = int(value)
        if -1 <= value <= 11:
            self._key = value
        else:
            raise ValueError(f"key must be between -1 and 11, got: {value}")

    @property
    def loudness(self):
        return self._loudness

    @loudness.setter
    def loudness(self, value):
        value = float(value)
        if -60 <= value <= 0:
            self._loudness = value
        else:
            raise ValueError(f"loudness must be between -60 and 0 dB, got: {value}")

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        value = int(value)
        if value in (0, 1):
            self._mode = value
        else:
            raise ValueError(f"mode must be 0 or 1, got: {value}")

    @property
    def speechiness(self):
        return self._speechiness

    @speechiness.setter
    def speechiness(self, value):
        value = float(value)
        if 0 <= value <= 1:
            self._speechiness = value
        else:
            raise ValueError(f"speechiness must be between 0 and 1, got: {value}")

    @property
    def acousticness(self):
        return self._acousticness

    @acousticness.setter
    def acousticness(self, value):
        value = float(value)
        if 0 <= value <= 1:
            self._acousticness = value
        else:
            raise ValueError(f"acousticness must be between 0 and 1, got: {value}")

    @property
    def instrumentalness(self):
        return self._instrumentalness

    @instrumentalness.setter
    def instrumentalness(self, value):
        value = float(value)
        if 0 <= value <= 1:
            self._instrumentalness = value
        else:
            raise ValueError(f"instrumentalness must be between 0 and 1, got: {value}")

    @property
    def liveness(self):
        return self._liveness

    @liveness.setter
    def liveness(self, value):
        value = float(value)
        if 0 <= value <= 1:
            self._liveness = value
        else:
            raise ValueError(f"liveness must be between 0 and 1, got: {value}")

    @property
    def valence(self):
        return self._valence

    @valence.setter
    def valence(self, value):
        value = float(value)
        if 0 <= value <= 1:
            self._valence = value
        else:
            raise ValueError(f"valence must be between 0 and 1, got: {value}")

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, value):
        value = float(value)
        if value > 0:
            self._tempo = value
        else:
            raise ValueError(f"tempo must be positive, got: {value}")

    @property
    def time_signature(self):
        return self._time_signature

    @time_signature.setter
    def time_signature(self, value):
        value = int(value)
        if 3 <= value <= 7:
            self._time_signature = value
        else:
            raise ValueError(f"time_signature must be between 3 and 7, got: {value}")

    def to_dict(self):
        return {
            "track_id":         self.track_id,
            "artists":          self.artists,
            "album_name":       self.album_name,
            "track_name":       self.track_name,
            "popularity":       self.popularity,
            "duration_ms":      self.duration_ms,
            "explicit":         self.explicit,
            "danceability":     self.danceability,
            "energy":           self.energy,
            "key":              self.key,
            "loudness":         self.loudness,
            "mode":             self.mode,
            "speechiness":      self.speechiness,
            "acousticness":     self.acousticness,
            "instrumentalness": self.instrumentalness,
            "liveness":         self.liveness,
            "valence":          self.valence,
            "tempo":            self.tempo,
            "time_signature":   self.time_signature,
            "track_genre":      self.track_genre,
        }