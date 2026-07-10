class DataAnalyzer():
    def __init__(self,df):
        self.df=df
        
    def correlation_matrix(self,col=None):
        if col is None:
            col=["popularity", "danceability", "energy", "loudness",
                    "speechiness", "acousticness", "instrumentalness",
                    "liveness", "valence", "tempo"]
    
        corr = self.df[col].corr()
        return corr

    def genre_insights(self,genre):
        genre_df=self.df[self.df["track_genre"] == genre]
        if genre_df.empty:
            raise ValueError(f"{genre} not found")
        return genre_df.describe()