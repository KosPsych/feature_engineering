import pandas as pd
import json
from itertools import chain
import featuretools as ft
import json



def feature_engineering (data):

    # convert JSON file to a dataframe using list comprehension
    all_loans  = [[{key: loan[key] for key in loan} for loan in data['data'][customer]['loans']] for customer in range(len(data['data']))]
    # list explode
    all_loans = list(chain(*all_loans))
    # dataframe conversion
    df = pd.DataFrame(all_loans)

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


    # Convert back into json

    # Step 1: Group the DataFrame and aggregate 'loans' into a list of dictionaries
    grouped_df = df.groupby('customer_ID').apply(lambda x: x[list(df.columns)].to_dict('records')).reset_index(name='loans')

    # Step 2: Convert the grouped DataFrame to a dictionary with 'customer_ID' as the key
    customers_dict = grouped_df.rename(columns={'customer_ID': 'customer_ID', 'loans': 'loans'}).to_dict('records')

    # Step 3: Create the final dictionary with the 'data' key
    final_json = {'data': customers_dict}

    # Convert the final dictionary to JSON format
    json_data = json.dumps(final_json)
    
    return json_data
