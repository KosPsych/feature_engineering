
import pandas as pd
from utils.dframe2json import *
from utils.json2dframe import *
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import logging

def dimensionality_reduction(data, target):

    # Data reading
    df = json2dframe(data)
    customer_id = 'customer_ID'
    target = target
    cols_to_drop = [customer_id, target]
    # Data scaling
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.drop(columns=[customer_id]))
    scaled_data = pd.DataFrame(scaled_data, columns = df.drop(columns=[customer_id]).columns)

    logging.info("Scaling completed.")
    # PCA
    pca = PCA()
    # fit PCA into the data
    fit_res = pca.fit(scaled_data.drop(columns=[target]))
    # Calculate the explained variance for each component
    explained_variance = pca.explained_variance_ratio_

    # Calculate the cumulative explained variance
    cumulative_variance = np.cumsum(explained_variance)

    # Find the number of components that explain a desired percentage of the total variance
    desired_variance = 0.9 # Choose the desired percentage (e.g., 95%)
    num_components = np.argmax(cumulative_variance >= desired_variance) + 1

    # Perform PCA with the selected number of components
    pca = PCA(n_components=num_components)
    reduced_data = pca.fit_transform(scaled_data.drop(columns=[target]))
    reduced_data = pd.DataFrame(reduced_data )
    reduced_data = pd.concat([df[customer_id],reduced_data, scaled_data[target]],axis=1)
    logging.info("PCA completed.")
    #convert back into json
    json_data = dframe2json(reduced_data)
    logging.info("dimensionality reduction complete.")
    return json_data
