import pandas as pd
from datetime import datetime

csv_file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 2 MongoDB\0- Dataset\customer_dataset.csv'

df = pd.read_csv(csv_file_path)

converted_data = []
for index, row in df.iterrows():
    converted_row = {
        "order_id": int(row['order_id']),
        "customer_id": str(row['customer_id']),
        "customer_name": str(row['customer_name']),
        "shipment_date": datetime.strptime(row['shipment_date'], '%d/%m/%Y'),
        "product_id": str(row['product_id']),
        "order_date": datetime.strptime(row['order_date'], '%d/%m/%Y'),
        "product_description": str(row['product_description']),
        "quantity": int(row['quantity']),
        "unit_price": float(row['unit_price'])
    }
    converted_data.append(converted_row)

new_df = pd.DataFrame(converted_data)

output_csv_file_path = r'C:\Users\lenovo\Desktop\Data Engineering Projects\Data Engineering Task - Cowlar\Task 2 MongoDB\0- Dataset\new_customer_dataset.csv'

new_df.to_csv(output_csv_file_path, index=False)

# The data is used to match the MongoDB Schema