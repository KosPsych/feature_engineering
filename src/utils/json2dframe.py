
from itertools import chain
import pandas as pd

def json2dframe (data):
    
    # convert JSON file to a dataframe using list comprehension
    all_loans  = [[{key: loan[key] for key in loan} for loan in data['data'][customer]['loans']] for customer in range(len(data['data']))]

    # list explode
    all_loans = list(chain(*all_loans))

    # dataframe conversion
    df = pd.DataFrame(all_loans)

    return df
