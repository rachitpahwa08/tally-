from google.cloud import storage
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

# cred = open('E:\Tally Connector\Tally-connector-6d187b87ff6d.json', 'rb').read()
# credJson=json.loads(cred)
# credentials = ServiceAccountCredentials.from_json_keyfile_dict(credJson)
#client = storage.Client(credentials=credentials, project='tally-connector')
credentials = service_account.Credentials.from_service_account_file(
    'D:/Equipshare/tally/Tally-connector-10b12c06b3eb.json',
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
client = storage.Client(credentials=credentials, project='tally-connector')
bucket = client.get_bucket('tally-connector')
blob = bucket.blob('myfiletest')
blob.upload_from_filename('D:/Equipshare/tally/TallyPython new/tally-/Transactions-23-10-19.csv')
if(blob.public_url):
    print("file uploded successfully")
