import pandas as pd
import json
import featuretools as ft
from utils.dframe2json import *
from utils.json2dframe import *
import sys
import logging

def feature_engineering (data):

    # COnvert Json input to dataframe

    df = json2dframe(data)

    # Converting data to the right format
    df['customer_ID'] = df['customer_ID'].astype('category')
    df['loan_date'] = pd.to_datetime(df['loan_date'], format='%d/%m/%Y')
    df['amount'] =  df['amount'].astype(int)
    df['fee'] =  df['fee'].astype(int)
    df['loan_status'] =  df['loan_status'].apply(lambda x : 'paid back' if x == '0' else 'defaulted')
    df['annual_income'] =  df['annual_income'].astype(int)
    df['term'] =  df['term'].astype('category')

    ########## Data cleaning/checking
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

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
                                          trans_primitives = ['year', 'quarter','add_numeric', 'multiply_numeric'])

    # df = pd.concat([df['customer_ID'], numeric_augmented], axis=1)


    # Manual feature engineering
    df['income/loan'] = df['annual_income'] / df['amount']
    df['interest'] = df['fee'] / df['amount']
    df['term'] = df['term'].apply(lambda x : 1 if x=='long' else 0)
    df['pol_amount'] = df['amount']^2
    df['pol_fee'] = df['fee']^2

    ############### one-hot encode categorical features

    df['YEAR(loan_date)'] = df['YEAR(loan_date)'].astype(str)
    # selecting categorical features to one-hot encode
    cat = df.select_dtypes(include='category')
    one_hot_cat = [item for item in cat if item != 'customer_ID']

    # one-hot encoding
    df = pd.get_dummies(df, columns = one_hot_cat)

    #convert back into json
    json_data = dframe2json(df)
    logging.info("feature_engineering complete.")
    return json_data
