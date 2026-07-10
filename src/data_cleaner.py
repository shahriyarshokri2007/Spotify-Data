from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer as SklearnKNNImputer
class BaseImputer(ABC):
    @abstractmethod
    def impute(self,df,col):
        pass

class UnnumericImputer(BaseImputer):
    def impute(self, df, col):
        df[col] = df[col].fillna("Unknown")
        return df

class MeanImputer(BaseImputer):
    def impute(self,df,col):
        df[col]=df[col].fillna(df[col].mean())
        return df

class MedianImputer(BaseImputer):
    def impute(self,df,col):
        df[col]=df[col].fillna(df[col].median())
        return df

class KNNImputer(BaseImputer):
    def impute(self, df, col):
        imputer=SklearnKNNImputer(n_neighbors=5)
        numeric_df = df.select_dtypes(include=[np.number])
        imputed_array=imputer.fit_transform(numeric_df)
        imputed_df = pd.DataFrame(
            imputed_array,
            columns=numeric_df.columns,
            index=numeric_df.index
        )
        df[col]=imputed_df[col]
        return df


class BaseOutlierHandler(ABC):
    @abstractmethod
    def handle(self,df,col):
        pass


class IQROutlierHandler(BaseOutlierHandler):
    def handle(self, df, col):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR=Q3-Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        mask = (df[col] >= lower_bound) & (df[col] <= upper_bound)
        df = df[mask]
        return df
        

class ZScoreOutlierHandler(BaseOutlierHandler):
    def handle(self, df, col,threshold=3):
        mean = df[col].mean()
        std = df[col].std()
        z_score=(df[col]-mean)/std
        mask=z_score.abs()<=threshold
        df=df[mask]
        return df

    