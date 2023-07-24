import pandas as pd
import numpy as np

def df_func():
    df = pd.read_table('./bank_marketing_dataset.csv')

# Basic data cleaning
    df['job'] = df['job'].str.replace('.', '', regex=True)
    df['education'] = df['education'].str.replace('.', ' ', regex=True).replace({'.4y': ' four years', '.6y': ' six years', '.9y': ' nine years'}, regex=True)
    df['day_of_week'] = df['day_of_week'].replace({'mon': 'monday','tue': 'tuesday', 'wed': 'wednesday', 'thu': 'thursday', 'fri': 'friday'}, regex=True)
    df['month'] = df['month'].replace({'jan': 'january', 'feb': 'february', 'mar': 'march', 'apr': 'april', 'may': 'may', 'jun': 'june', 'jul': 'july', 'aug': 'august', 'sep': 'september', 'oct': 'october', 'nov': 'november', 'dec': 'december'}, regex=True)

# Making yes/no answers into boolean type values: True/False
    for boolean in df.columns:
        df[boolean] = df[boolean].replace({'yes': True, 'no': False})

# To make the values boolean dtype in some columns I am replacing "Unknown" with NaN
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].replace('unknown', np.nan)

# Renaming column to look visaully better
    df = df.rename(columns = {'euribor3m': 'euribor_3m'})

# Declaring the dtypes for columns
    category_columns = ['job','marital','education','contact','month','day_of_week','poutcome']
    num_columns = ['age', 'duration', 'campaign', 'pdays','previous']
    float_columns = ['emp_var_rate', 'cons_price_idx', 'cons_conf_idx', 'euribor_3m', 'nr_employed']
    boolean_columns = ['default', 'housing', 'loan', 'has_deposit', 'target']

# Setting dtypes for columns
    df[category_columns] = df[category_columns].astype(str)
    df[num_columns] = df[num_columns].astype(int)
    df[float_columns] = df[float_columns].astype(float)
    df[boolean_columns] = df[boolean_columns].astype(bool)

    return df