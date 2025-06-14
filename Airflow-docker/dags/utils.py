from datetime import datetime

import awswrangler as wr
import boto3
import pandas as pd
import requests
from airflow.models import Variable

# session credentials
session = boto3.Session(
    aws_access_key_id=Variable.get('ACCESS_KEY'),
    aws_secret_access_key=Variable.get('SECRET_KEY'),
    region_name='us-east-1')


# extraction for API
API_KEY = Variable.get('API_KEY')

def weather_api_extract():
    Base_url = f"https://api.weatherbit.io/v2.0/current?lat=7.422&lon=3.957&key={API_KEY}"
    response = requests.get(Base_url)
    if response.status_code == 200:
        data = response.json()['data']
        df = pd.json_normalize(data)
        df = df.astype(str)

# Load the dataframe to s3 bucket.
        s3_bucket = 'victor-job-2025'
        s3_folder = 'weather_folder'

        date_str = datetime.today().strftime('%Y-%m-%d')
        s3_pathway = f"s3://{s3_bucket}/{s3_folder}/weather_file-{date_str}.parquet"
        wr.s3.to_parquet(
            df=df,
            path=s3_pathway,
            index=False,
            boto3_session=session,
            dataset=False
        )
        return df
    else:
        raise ValueError(f"There is an error{response.status_code}")
