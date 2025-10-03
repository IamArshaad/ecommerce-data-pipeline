# src/generate_synthetic_data.py
import pandas as pd
import numpy as np
from faker import Faker
fake = Faker()

# Customers
customers = []
for i in range(1, 501):
    customers.append({
      'customer_id': i,
      'name': fake.name(),
      'signup_date': fake.date_between(start_date='-3y', end_date='today').isoformat(),
      'city': fake.city(),
      'state': fake.state(),
      'age_group': np.random.choice(['18-25','26-35','36-45','46-55','above 55'])
    })
pd.DataFrame(customers).to_csv('data/customers.csv', index=False)

# Products
products = []
for i in range(1, 201):
    products.append({
      'product_id': i,
      'product_name': f'Product_{i}',
      'category': np.random.choice(['Electronics','Home','Clothing','Toys','Beauty']),
      'cost_price': round(np.random.uniform(5, 200),2),
      'list_price': round(np.random.uniform(10, 400),2)
    })
pd.DataFrame(products).to_csv('data/products.csv', index=False)

# Orders (transactions)
orders = []
order_id=1
date_range = pd.date_range(start='2024-01-01', end='2024-06-30')
for day in date_range:
    n = np.random.poisson(30)  # number of orders that day
    for _ in range(n):
        cust = np.random.randint(1,501)
        prod = np.random.randint(1,201)
        qty = np.random.choice([1,1,1,2,3])
        price = round(np.random.choice([10,20,50,100,200]) * (1+np.random.rand()*0.5),2)
        orders.append({
           'order_id': order_id,
           'customer_id': cust,
           'order_date': day.strftime('%Y-%m-%d'),
           'product_id': prod,
           'quantity': qty,
           'price': price,
           'channel': np.random.choice(['web','mobile','store']),
           'order_status': np.random.choice(['completed','returned','cancelled'], p=[0.9,0.08,0.02])
        })
        order_id+=1
pd.DataFrame(orders).to_csv('data/orders.csv', index=False)

print("Generated customers.csv, products.csv, orders.csv in data/")
