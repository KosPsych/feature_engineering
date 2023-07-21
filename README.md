# Feature engineering Application

This is a feature engineering application that takes a JSON file as an input and performs feature engineering using some automated/manual methodologies.
The application consists of three basic endpoints, namely:
*  healthcheck -> check the status of the application
* feature_engineering -> Given a JSON as input produces a JSON file with identical structures with more relevant features
* dimensionality_reduction -> Given a JSON as input produces a JSON file with identical structures were the features have been reduced using principal Component Analysis (PCA)


---------------------------------
## Setup

To run this application one needs to follow the steps below:

### Step One

``git clone``

### Have docker installed

``Docker version 24.0.2``

### Have docker installed

``docker build -t feature_eng_img .``

### Create a container

``docker run -p 8000:8000 feature_eng_img``

---------------------------------
## Test
Acquire a relevant JSON file.\\
Produce an HTTP request, for example:

### feature engineering endpoint

``curl -X POST http://127.0.0.1:8000/feature_engineering -H "Content-Type: application/json" -d @cvas_data.json -o f_e_result.json``

### dimensionality_reduction endpoint

``curl -X POST http://127.0.0.1:8000/dimensionality_reduction?target=amount
 -H  "Content-Type: application/json" /
 -d @f_e_result.json -o reduced.json``

 ### healthcheck endpoint

 curl -X GET http://127.0.0.1:8000/healthcheck 
