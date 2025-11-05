import pandas as pd
class Stats:
    def __init__(self):
        pass

    
    @staticmethod
    def findMedian(df:pd.DataFrame, colname:str):
        df = df.sort_values(colname).reset_index(drop=True)
        length = len(df)
        if(length%2 ==1) : return df[colname].iloc[length // 2]
        m1 = df[colname].iloc[length // 2]
        m2 = df[colname].iloc[length // 2 - 1]
        return (m1 + m2)/2
        
    
    @staticmethod
    def findAverage(df:pd.DataFrame, colname:str):
        
        length = len(df)
        total = 0
        for val in df[colname]:
            total += val
        
        total /= length
        return total
    
    @staticmethod
    def findMax(df:pd.DataFrame, colname:str):
        df = df.sort_values(colname).reset_index(drop=True)
        return df[colname].iloc[-1]

    @staticmethod
    def findMin(df:pd.DataFrame, colname:str):
        df = df.sort_values(colname).reset_index(drop=True)
        return df[colname].iloc[0]
    
    @staticmethod
    def findMode(df:pd.DataFrame, colname:str):
        counts = df[colname].value_counts()
        return counts.index[0] if (counts.values[0] > 1) else None
