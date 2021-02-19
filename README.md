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
df_eda = eda_obj.eda()
```
|columns              |na_count|na_percentage|value_types                     |cardinality|count                                                                                 |mean   |std               |min                |25%  |50%     |75%    |max     |outlier_IQR|
|---------------------|--------|-------------|--------------------------------|-----------|--------------------------------------------------------------------------------------|-------|------------------|-------------------|-----|--------|-------|--------|-----------|
|Id                   |0       |0            |{<class 'int'>}                 |40000      |40000                                                                                 |20000.5|11547.1           |1.0                |10000.75|20000.5 |30000.25|40000   |(-19998.5, 59999.5)|
|city                 |1864    |4.66         |{<class 'str'>, <class 'float'>}|856        |                                                                                      |       |                  |                   |     |        |       |        |           |
|age                  |0       |0            |{<class 'int'>}                 |62         |40000                                                                                 |55.2   |3830.4            |2.0                |29   |35      |42     |766105  |(9.5, 61.5)|
|sex                  |0       |0            |{<class 'str'>}                 |3          |                                                                                      |       |                  |                   |     |        |       |        |           |
|social_class         |5255    |13.1375      |{<class 'str'>, <class 'float'>}|519        |                                                                                      |       |                  |                   |     |        |       |        |           |
|primary_business     |26      |0.065        |{<class 'str'>, <class 'float'>}|441        |                                                                                      |       |                  |                   |     |        |       |        |           |
|secondary_business   |5241    |13.1025      |{<class 'str'>, <class 'float'>}|5          |                                                                                      |       |                  |                   |     |        |       |        |           |
|annual_income        |0       |0            |{<class 'float'>}               |359        |40000                                                                                 |37640.2|28739.1           |0.0                |14400|36000   |56000  |1200000 |(-48000.0, 118400.0)|
|monthly_expenses     |120     |0.3          |{<class 'float'>}               |260        |39880                                                                                 |3810.9 |4593.0            |2.0                |2500 |3500    |4000   |240000  |(250.0, 6250.0)|
|old_dependents       |0       |0            |{<class 'int'>}                 |4          |40000                                                                                 |0.0    |0.2               |0.0                |0    |0       |0      |3       |(0.0, 0.0) |
|young_dependents     |0       |0            |{<class 'int'>}                 |8          |40000                                                                                 |1.1    |1.1               |0.0                |0    |1       |2      |7       |(-3.0, 5.0)|
|home_ownership       |379     |0.9475       |{<class 'float'>}               |2          |39621                                                                                 |1.0    |0.2               |0.0                |1    |1       |1      |1       |(1.0, 1.0) |
|type_of_house        |694     |1.735        |{<class 'str'>, <class 'float'>}|3          |                                                                                      |       |                  |                   |     |        |       |        |           |
|occupants_count      |0       |0            |{<class 'int'>}                 |23         |40000                                                                                 |26.6   |4750.0            |0.0                |2    |3       |4      |950000  |(-1.0, 7.0)|
|house_area           |0       |0            |{<class 'float'>}               |391        |40000                                                                                 |552.8  |4596.9            |0.0                |200  |400     |600    |700000  |(-400.0, 1200.0)|
|sanitary_availability|208     |0.52         |{<class 'float'>}               |3          |39792                                                                                 |0.7    |0.5               |-1.0               |0    |1       |1      |1       |(-1.5, 2.5)|
|water_availabity     |5253    |13.1325      |{<class 'float'>}               |4          |34747                                                                                 |0.8    |0.3               |-1.0               |0.5  |1       |1      |1       |(-0.25, 1.75)|
|loan_purpose         |26      |0.065        |{<class 'str'>, <class 'float'>}|37         |                                                                                      |       |                  |                   |     |        |       |        |           |
|loan_tenure          |0       |0            |{<class 'int'>}                 |11         |40000                                                                                 |12.0   |1.4               |3.0                |12   |12      |12     |84      |(12.0, 12.0)|
|loan_installments    |0       |0            |{<class 'int'>}                 |21         |40000                                                                                 |21.8   |16.7              |0.0                |12   |12      |50     |84      |(-45.0, 107.0)|
|loan_amount          |0       |0            |{<class 'float'>}               |115        |40000                                                                                 |8412.6 |13596.9           |100.0              |5000 |8000    |10000  |1343000 |(-2500.0, 17500.0)|
