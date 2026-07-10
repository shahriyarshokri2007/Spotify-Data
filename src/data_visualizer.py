import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self,df):
        self.df=df

    def plot_scatter(self,x,y,hue=None):
        plt.figure(figsize=(10, 6))
        plot_copy=self.df.copy()
        if hue == "artists":
            plot_copy["artists"] = plot_copy["artists"].str.replace("$","",regex=False)
        plot=sns.scatterplot(data=plot_copy,x=x,y=y,hue=hue)
        plt.title(f"{y} vs {x}")
        plt.xlabel(x)
        plt.ylabel(y)
        if hue is not None:
            plt.legend(bbox_to_anchor=(1.02,1),loc="upper left")
        plt.show()

    def plot_boxplot(self,col,title=""):
        plt.figure(figsize=(8, 6))
        sns.boxplot(data=self.df,y=col)
        plt.title(f"Box plot {col}")
        plt.show()

    def plot_correlation_heatmap(self,corr_matrix):
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Audio Features Correlation Matrix")
        plt.show()