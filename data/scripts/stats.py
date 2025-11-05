import pandas as pd
import numpy as np

class Stats:
    def __init__(self):
        pass

    
    @staticmethod
    def median(df:pd.DataFrame, col:str):
        df = df.sort_values(col).reset_index(drop=True)
        length = len(df)
        if(length%2 ==1) : return df[col].iloc[length // 2]
        m1 = df[col].iloc[length // 2]
        m2 = df[col].iloc[length // 2 - 1]
        return (m1 + m2)/2
        
    
    @staticmethod
    def average(df:pd.DataFrame, col:str):
        return df[col].mean()
    
    @staticmethod
    def max(df:pd.DataFrame, col:str):
        return df[col].max()

    @staticmethod
    def min(df:pd.DataFrame, col:str):
        return df[col].min()
    
    @staticmethod
    def mode(df:pd.DataFrame, col:str):
        counts = df[col].value_counts()
        return counts.index[0] if (counts.values[0] > 1) else None

    @staticmethod
    def range(df:pd.DataFrame, col:str):
        return df[col].max() - df[col].min()

    @staticmethod
    def standardDeviation(df:pd.DataFrame, col:str):
        return df[col].std()
    
    @staticmethod
    def variance(df:pd.DataFrame, col:str):
        return df[col].var()
    
    @staticmethod
    def iqr(df:pd.DataFrame, col:str):
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        return q3 - q1
    
    def coeficientOfVariation(df:pd.DataFrame, col:str):
        mean = df[col].mean()
        std  = df[col].std()
        return std/mean if mean != 0 else np.nan