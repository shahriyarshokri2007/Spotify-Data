from src.data_loader import DataLoader
from src.data_cleaner import MeanImputer, MedianImputer, KNNImputer, UnnumericImputer
from src.data_cleaner import IQROutlierHandler, ZScoreOutlierHandler
from src.song import Song
from src.data_analyzer import DataAnalyzer
from src.data_visualizer import DataVisualizer
import pandas as pd

loader=DataLoader("data/dataset.csv")

while True:
    print("========================   Spotify Data Studio & Management System   ========================")
    print("1. Load Dataset & View Missing Values Report")
    print("2. Clean Missing Values (Mean / Median / KNN)")
    print("3. Handle Outliers (IQR / Z-Score)")
    print("4. Add a New Song to the Dataset (Interactive Input)")
    print("5. Calculate Genre Insights & Correlation Matrix")
    print("6. Generate Advanced Visualizations (Plots)")
    print("7. Exit")
    print("===================================================================")
    try:
        choice=int(input("Enter your choice (1-7): "))
    except ValueError:
        print("The choice is not valid")
        print("Try again")
        continue

    if choice==1:
        try:
            loader.load_data()
            print(f"{len(loader.songs)} songs successfully uploaded")
            print(f"{loader.skip_row} invalid rows rejected")
            print("report missing values:")
            print(loader.get_missing_report())
        except FileNotFoundError:
            print("FileNotFoundError")
            continue

    elif choice==2:
        if loader.df is None:
            print("Select option 1 to load first")
            continue

        choice_col=input("col: ")
        if choice_col not in loader.df.columns:
            print("The choice is not valid")
            print("Try again")
            continue

        if not pd.api.types.is_numeric_dtype(loader.df[choice_col]):
                loader.df = UnnumericImputer().impute(loader.df,choice_col)
                print(f"Column '{choice_col}' was cleaned successfully")
                continue

        print("1- Mean")
        print("2- Median")
        print("3- KNN")
        try:
            choice_2 = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("The choice is not valid")
            print("Try again")
            continue        
        if choice_2==1:
            imputer=MeanImputer()
        elif choice_2==2:
            imputer=MedianImputer()
        elif choice_2==3:
            imputer=KNNImputer()
        else:
            print("The choice is not valid")
            print("Try again")
            continue

        loader.df = imputer.impute(loader.df, choice_col)
        print(f"Column '{choice_col}' was cleaned successfully")

    elif choice==3:
        if loader.df is None:
            print("Select option 1 to load first")
            continue
        choice_col=input("col: ")
        if choice_col not in loader.df.columns:
            print("The choice is not valid")
            print("Try again")
            continue
        if not pd.api.types.is_numeric_dtype(loader.df[choice_col]):
            print("The column is not numeric")
            print("Try again")
            continue

        print("1- IQR")
        print("2- Z-Score")
        try:
            choice_3 = int(input("Enter your choice (1-2): "))
        except ValueError:
            print("The choice is not valid")
            print("Try again")
            continue

        if choice_3 == 1:
            handler = IQROutlierHandler()
        elif choice_3 == 2:
            handler = ZScoreOutlierHandler()
        else:
            print("The choice is not valid")
            print("Try again")
            continue

        loader.df = handler.handle(loader.df, choice_col)
        print(f"Column '{choice_col}' was cleaned successfully")

    elif choice==4:
        if loader.df is None:
            print("Select option 1 to load first")
            continue
        
        track_id = input("Track ID: ")
        artists = input("Artists: ")
        album_name = input("Album name: ")
        track_name = input("Track name: ")
        popularity = input("Popularity (0-100): ")
        duration_ms = input("Duration (ms): ")
        explicit = input("Explicit (True/False): ")
        danceability = input("Danceability (0-1): ")
        energy = input("Energy (0-1): ")
        key = input("Key (-1 to 11): ")
        loudness = input("Loudness (-60 to 0): ")
        mode = input("Mode (0 or 1): ")
        speechiness = input("Speechiness (0-1): ")
        acousticness = input("Acousticness (0-1): ")
        instrumentalness = input("Instrumentalness (0-1): ")
        liveness = input("Liveness (0-1): ")
        valence = input("Valence (0-1): ")
        tempo = input("Tempo: ")
        time_signature = input("Time signature (3-7): ")
        track_genre = input("Track genre: ")

        try:
            new_song = Song(
                track_id=track_id,
                artists=artists,
                album_name=album_name,
                track_name=track_name,
                popularity=popularity,
                duration_ms=duration_ms,
                explicit=explicit,
                danceability=danceability,
                energy=energy,
                key=key,
                loudness=loudness,
                mode=mode,
                speechiness=speechiness,
                acousticness=acousticness,
                instrumentalness=instrumentalness,
                liveness=liveness,
                valence=valence,
                tempo=tempo,
                time_signature=time_signature,
                track_genre=track_genre
            )
        except ValueError as e:
            print(f"{e}")
            continue

        loader.append_song(new_song)
        loader.df = loader.dataframe()
        print(f"Song '{new_song.track_name}' added successfully")

    elif choice==5:
        if loader.df is None:
            print("Select option 1 to load first")
            continue
        analyzer = DataAnalyzer(loader.df)
        print("Correlation Matrix:")
        print(analyzer.correlation_matrix())
        genre = input("Enter genre name for insights: ")

        try:
            insights = analyzer.genre_insights(genre)
            print(f"\nInsights for genre '{genre}':")
            print(insights)
        except ValueError as e:
            print(f"{e}")
            continue

    elif choice==6:
        if loader.df is None:
            print("Select option 1 to load first")
            continue

        visualizer = DataVisualizer(loader.df)

        print("1- Scatter Plot")
        print("2- Box Plot")
        print("3- Correlation Heatmap")
        try:
            choice_6 = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("The choice is not valid")
            print("Try again")
            continue
        
        if choice_6 == 1:
            x_col = input("Enter X column: ")
            y_col = input("Enter Y column: ")
            hue_col = input("Enter hue column (or press Enter to skip): ")
            if x_col not in loader.df.columns or y_col not in loader.df.columns:
                print("The choice is not valid")
                print("Try again")
                continue
            if hue_col == "":
                hue_col = None
            elif hue_col not in loader.df.columns:
                print("The choice is not valid")
                print("Try again")
                continue
            if pd.api.types.is_numeric_dtype(loader.df[x_col]) and pd.api.types.is_numeric_dtype(loader.df[y_col]):
                visualizer.plot_scatter(x_col,y_col,hue=hue_col)
            else:
                print("The column is not numeric")
                print("Try again")
                continue

        elif choice_6 == 2:
            col = input("Enter column for Box Plot: ")
            if col not in loader.df.columns:
                print("The choice is not valid")
                print("Try again")
                continue
            if pd.api.types.is_numeric_dtype(loader.df[col]):
                visualizer.plot_boxplot(col)
            else:
                print("The column is not numeric")
                print("Try again")
                continue
        
        elif choice_6 == 3:
            analyzer = DataAnalyzer(loader.df)
            corr = analyzer.correlation_matrix()
            visualizer.plot_correlation_heatmap(corr)

        else:
            print("The choice is not valid")
            print("Try again")
            continue


    elif choice==7:
        print("Good bye!")
        break


    else:
        print("The choice is not valid")
        print("Try again")
        continue

