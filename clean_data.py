import pandas as pd
import numpy as np

def clean_data(df):
    print('Missing data:\n', df.isna().sum()) # check for missing data
    print('\nDublicates:\n', df.duplicated().sum()) # check for duplicated data

    df['date'] = pd.to_datetime(df['date']) # convert Date column to datetime

    # Fill empty cells where applicable
    df['store_location'] = df['store_location'].fillna(np.nan)
    df['county_number'] = df['county_number'].fillna(0)
    df['county'] = df['county'].fillna(np.nan)
    df['category'] = df['category'].fillna(0)
    df['category_name'] = df['category_name'].fillna(np.nan)

    # Convert all cells in column to the same data type
    df['zip_code'] = df['zip_code'].astype(int)
    df['category'] = df['category'].astype(int)
    df['vendor_number'] = df['vendor_number'].astype(int)

    df = df.replace(np.nan, None)
    df = df.replace(0, np.nan)

    df['year'] = df['date'].dt.year # create years column

    # df.to_csv('./Data/cleaned_data.csv', index = False) # to check cleaned data
    return df