# My-EDA
This repository is for reusable exploratory data analysis functionality. 

Usage: 
```py
df = pd.read_csv('trainingData.csv')
eda_obj = eda()
eda_obj.eda(df)
eda_obj.missingValue()
eda_obj.valueTypes()
eda_obj.cardinality()
eda_obj.sample_records()
eda_obj.pandas_describe()
eda_obj.eda()
```