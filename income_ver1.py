""" Import Statements """

import numpy as np
import pandas as pd

# Load the data 
income_df = pd.read_csv('census_income.data')
# Print the shape and check the first 5 rows
print(income_df.shape)
"""(32560, 15)"""
print(income_df.head())
"""
   39          State-gov   77516   Bachelors   13  ...  2174  0  40   United-States   <=50K
0  50   Self-emp-not-inc   83311   Bachelors   13  ...     0  0  13   United-States   <=50K
1  38            Private  215646     HS-grad    9  ...     0  0  40   United-States   <=50K
2  53            Private  234721        11th    7  ...     0  0  40   United-States   <=50K
3  28            Private  338409   Bachelors   13  ...     0  0  40            Cuba   <=50K
4  37            Private  284582     Masters   14  ...     0  0  40   United-States   <=50K
"""
# Print columns
print(income_df.columns)
"""
Index(['39', ' State-gov', ' 77516', ' Bachelors', ' 13', ' Never-married',
       ' Adm-clerical', ' Not-in-family', ' White', ' Male', ' 2174', ' 0',
       ' 40', ' United-States', ' <=50K'],
      dtype='object')
"""

# Remove unimportant columns and crate a copy of the dataframe with reduced number of columns
income_df.columns = ['Age', 'Workclass', 'fnlwgt', 'Education', 'Edu_num', 'Marital_status', 'Occupation', 'Relationship', 
                    'Race', 'Gender', 'Capital_gain', 'Capital_loss', 'Hours_per_week', 'Country', 'Income']

income_df = income_df[['Age', 'Education', 'Edu_num', 'Occupation', 'Race', 'Gender','Hours_per_week', 'Country', 'Income']]

print(income_df.head())
"""
   Age   Education  Edu_num          Occupation    Race   Gender  Hours_per_week         Country  Income
0   50   Bachelors       13     Exec-managerial   White     Male              13   United-States   <=50K
1   38     HS-grad        9   Handlers-cleaners   White     Male              40   United-States   <=50K
2   53        11th        7   Handlers-cleaners   Black     Male              40   United-States   <=50K
3   28   Bachelors       13      Prof-specialty   Black   Female              40            Cuba   <=50K
4   37     Masters       14     Exec-managerial   White   Female              40   United-States   <=50K
"""

# Check for nulls (missing values)
print(income_df.isnull().sum())

# Identify target and count the values
print(income_df['Income'].value_counts())

# Create and save a new csv file with modified dataset
income_df.to_csv('income.csv', index=False)
