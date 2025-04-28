import psycopg2
import random
from datetime import datetime
from faker import Faker
import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)
now = datetime.now()

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="dbSource",
    user="useradmin",
    password="password",
    host="db_source",
    port="5432"
)
cur = conn.cursor()

# Insert random data into dim_product
def insert_dim_product(n):
    for _ in range(n):
        cur.execute("""
            INSERT INTO dw.dim_product (id_product, name, category, insertion_timestamp)
            VALUES (%s, %s, %s, %s)
        """, (
            random.randint(100, 999),  
            fake.ecommerce_name(),   
            fake.ecommerce_category(),  
            now
        ))

# Insert random data into dim_channel
def insert_dim_channel(n):
    for _ in range(n):
        cur.execute("""
            INSERT INTO dw.dim_channel (id_channel, name, region, insertion_timestamp)
            VALUES (%s, %s, %s, %s)
        """, (
            random.randint(100, 999),
            fake.company(),
            fake.state(),
            now
        ))

# Insert random data into dim_customer
def insert_dim_customer(n):
    for _ in range(n):
        cur.execute("""
            INSERT INTO dw.dim_customer (id_customer, name, type, city, state, country, insertion_timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            random.randint(100, 999),
            fake.name(),
            random.choice(['Individual', 'Company']),
            fake.city(),
            fake.state_abbr(),
            fake.country(),
            now
        ))

# Insert into fact_sales
def insert_fact_sales(n):
    # Retrieve all existing surrogate keys for products, customers, channels, and dates
    cur.execute("SELECT sk_product FROM dw.dim_product")
    all_products = [row[0] for row in cur.fetchall()]  # List of all product surrogate keys

    cur.execute("SELECT sk_customer FROM dw.dim_customer")
    all_customers = [row[0] for row in cur.fetchall()]  # List of all customer surrogate keys

    cur.execute("SELECT sk_channel FROM dw.dim_channel")
    all_channels = [row[0] for row in cur.fetchall()]    # List of all channel surrogate keys

    cur.execute("SELECT sk_date FROM dw.dim_date")  # Fetch all date surrogate keys
    all_dates = [row[0] for row in cur.fetchall()]   # List of all date surrogate keys

    for _ in range(n):
        cur.execute("""
            INSERT INTO dw.fact_sales (sk_product, sk_customer, sk_channel, sk_date, quantity, sales_value, insertion_timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            random.choice(all_products),  # Select a random product surrogate key
            random.choice(all_customers),  # Select a random customer surrogate key
            random.choice(all_channels),    # Select a random channel surrogate key
            random.choice(all_dates),       # Select a random date surrogate key
            random.randint(1, 20),          # Random quantity
            round(random.uniform(10.0, 500.0), 2),  # Random sales value
            now                             # Current timestamp
        ))

# Generate random number of rows
num_products = random.randint(1, 5)
num_channels = random.randint(1, 5)
num_customers = random.randint(1, 5)
num_facts = random.randint(5, 10)

# Insert into dimension tables
insert_dim_product(num_products)
insert_dim_channel(num_channels)
insert_dim_customer(num_customers)

# Insert into fact table
insert_fact_sales(num_facts)

# Finalize
conn.commit()
cur.close()
conn.close()

print(f"✅ Inserted {num_products} products, {num_channels} channels, {num_customers} customers, {num_facts} sales records.")