import pandas as pd
from scipy import stats
import numpy as np
# outliers = df_numeric[(np.abs(stats.zscore(df_numeric[col])) > 3)][col]


def getOutliersIQR(df: pd.DataFrame):
    return [outliersIQR(df[col]) for col in df]
    
def outliersIQR(data: pd.Series):
    try:
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        min_threshold = Q1 - 1.5 * IQR
        max_threshold = Q3 + 1.5 * IQR
        return (min_threshold, max_threshold)
    except:
        return None
