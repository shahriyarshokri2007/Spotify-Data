import pandas as pd
from src.song import Song
class DataLoader():
    def __init__(self,file):
        self.file=file
        self.songs=[]
        self.df=None
        self.skip_row=0
        
    def load_data(self):
        self.songs=[]
        self.skip_row=0
        try:
            self.df=pd.read_csv(self.file,index_col=0)
        except FileNotFoundError:
            raise FileNotFoundError
        
        for index, row in self.df.iterrows():
            try:
                song = Song(**row.to_dict())
                self.songs.append(song)
            except ValueError:
                self.skip_row += 1
                continue

    def get_missing_report(self):
        return self.df.isnull().sum()

    def append_song(self, song):
        self.songs.append(song)
        data = song.to_dict()
        new_index = len(self.df) 
        new_row = pd.DataFrame([data], index=[new_index])
        new_row.to_csv(self.file, mode="a", header=False)

    def dataframe(self):
        song_list=[song.to_dict() for song in self.songs]
        return pd.DataFrame(song_list)