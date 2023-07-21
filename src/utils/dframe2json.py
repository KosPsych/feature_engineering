import pandas as pd


def dframe2json (df):

    # Step 1: Group the DataFrame and aggregate 'loans' into a list of dictionaries
    grouped_df = df.groupby('customer_ID').apply(lambda x: x[list(df.columns)].to_dict('records')).reset_index(name='loans')

    # Step 2: Convert the grouped DataFrame to a dictionary with 'customer_ID' as the key
    customers_dict = grouped_df.rename(columns={'customer_ID': 'customer_ID', 'loans': 'loans'}).to_dict('records')

    # Step 3: Create the final dictionary with the 'data' key
    json_data = {'data': customers_dict}

    # Convert the final dictionary to JSON format
    return json_data
