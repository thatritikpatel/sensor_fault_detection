
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import json

uri = "mongodb+srv://ritikpatel:password1234@cluster0.ndxaj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


#create database name and collection name
DATABASE_NAME="sensor_data"
COLLECTION_NAME='waferfault'

df=pd.read_csv(r"C:\Users\pcc\Desktop\Python Projects\sensor_fault_detection\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)