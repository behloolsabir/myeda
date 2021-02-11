# df = pd.read_csv('/mnt/01A460F67A4DAD69/Documents/ThoughtWorks/trainingData.csv')
# import eda
# import importlib
# importlib.reload(eda)

# eda_obj = eda.eda(df)
# eda_obj.missingValue()
# eda_obj.valueTypes()
# eda_obj.cardinality()
# eda_obj.sample_records()
# eda_obj.pandas_describe()
# eda_obj.eda()
# df.pipe(driver_distance_to_pickup)
#         .pipe(hour_of_day)
#         .pipe(driver_historical_completed_bookings)

import pandas as pd
class eda:
    """
    Usage: 
    df = pd.read_csv('/mnt/01A460F67A4DAD69/Documents/ThoughtWorks/trainingData.csv')
    eda_obj = eda()
    eda_obj.eda(df)
    """
    def __init__(self, df: pd.DataFrame):
        self.df_eda = pd.DataFrame()
        self.df = df
        self.df_eda['columns'] = self.df.columns
    def missingValue(self):
        self.df_eda['na_count'] = [self.df[col].isna().sum() for col in self.df]
        self.df_eda['na_percentage'] = self.df_eda['na_count']*100/self.df.shape[0]
        return self.df_eda
    def valueTypes(self):
        self.df_eda['value_types'] = [set([type(val) for val in self.df[col]]) for col in self.df]
        return self.df_eda
    def cardinality(self):
        self.df_eda['cardinality'] = [self.df[col].nunique() for col in self.df]
        return self.df_eda
    def sampleRecords(self):
        self.df_eda['sample_records'] = [
            set(self.df[col].unique()[:5]) for col in self.df
        ]
    def pandas_describe(self):
        desc = self.df.describe().T.rename_axis('columns').reset_index()
        self.df_eda = self.df_eda.merge(desc, on='columns', how='left')
        return self.df_eda
    def eda(self):
        self.missingValue()
        self.valueTypes()
        self.cardinality()
        self.sampleRecords()
        self.pandas_describe()
        return self.df_eda
