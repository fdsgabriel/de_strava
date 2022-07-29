import os
import boto3

#client
client = boto3.client('s3')

#path and others vars
bucket = 'de-cleaned-useast1-strava'
cur_path = os.getcwd()
file = 'strava/1c190fbb672e47498d4815bf2ed1f0be.snappy.parquet'
filename = os.path.join(cur_path, 'strava_parquet', file)

#object method to download file
client.download_file(
        Bucket=bucket,
        Key=file,
        Filename=filename
    )



