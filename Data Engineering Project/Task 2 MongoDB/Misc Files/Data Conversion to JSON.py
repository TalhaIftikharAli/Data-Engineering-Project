import pandas as pd
import json

file = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 2 MongoDB\0- Dataset\customer_dataset.csv'

df = pd.read_csv(file)

df['order_date'] = pd.to_datetime(df['order_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

df['shipment_date'] = pd.to_datetime(df['shipment_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

json_data = json.loads(df.to_json(orient='records'))

json_file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 2 MongoDB\0- Dataset\customer_dataset.json'

with open (json_file_path, 'w') as json_file:
    json.dump(json_data, json_file)