from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

cred = open('E:\Tally Connector\Tally-connector-6d187b87ff6d.json', 'rb').read()
credJson=json.loads(cred)
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credJson)
client = storage.Client(credentials=credentials, project='tally-connector')
bucket = client.get_bucket('tally-connector')
blob = bucket.blob('myfile')
blob.upload_from_filename('C:/Users/91908/Desktop/Tally/project/Transactions-23-10-19.csv')
if(blob.public_url):
    print("file uploded successfully")
