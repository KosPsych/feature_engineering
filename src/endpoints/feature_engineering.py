import pandas as pd
import json
import featuretools as ft
from utils.dframe2json import *
from utils.json2dframe import *



def feature_engineering (data):

    # COnvert Json input to dataframe

    df = json2dframe(data)

    # Converting data to the right format
    df['loan_date'] = pd.to_datetime(df['loan_date'], format='%d/%m/%Y')
    df['amount'] =  df['amount'].astype(int)
    df['fee'] =  df['fee'].astype(int)
    df['loan_status'] =  df['loan_status'].astype(int)
    df['annual_income'] =  df['annual_income'].astype(int)
    df['term'] =  df['term'].astype(str)

    ########## Data cleaning/checking
    print('NaN values')
    print(df.isna().sum())

    if df.duplicated().any():
        print("The DataFrame has duplicates.")
    else:
        print("The DataFrame does not have duplicates.")

    print(df.drop(columns=['loan_status']).describe())


    #### Feature enginnering process

    # Using featuretools
    # Make an entityset and add the entity
    es = ft.EntitySet(id = 'loans')
    es = es.add_dataframe(
          dataframe_name="data",
          dataframe=df,
          index="index",
    )

    # Run deep feature synthesis with transformation primitives
    df, feature_defs = ft.dfs(entityset = es, target_dataframe_name = 'data',
                                          trans_primitives = ['year', 'quarter', 'week'])

    # Manual feature engineering
    df['income/loan'] = df['annual_income'] / df['amount']
    df['interest'] = df['fee'] / df['amount']
    df['term'] = df['term'].apply(lambda x : 1 if x=='long' else 0)
    df['pol_amount'] = df['amount']^2
    df['pol_fee'] = df['fee']^2



    #convert back into json
    json_data = dframe2json(df)

    return json_data
