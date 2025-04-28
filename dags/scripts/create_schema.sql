   -- Create schema if it doesn't exist
   CREATE SCHEMA IF NOT EXISTS dw AUTHORIZATION useradmin;

   -- Dimension: Product
   CREATE TABLE IF NOT EXISTS dw.dim_product (
       sk_product SERIAL PRIMARY KEY,
       id_product INT,
       name VARCHAR(255),
       category VARCHAR(255),
       insertion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   -- Dimension: Channel
   CREATE TABLE IF NOT EXISTS dw.dim_channel (
       sk_channel SERIAL PRIMARY KEY,
       id_channel INT,
       name VARCHAR(255),
       region VARCHAR(255),
       insertion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   -- Dimension: Customer
   CREATE TABLE IF NOT EXISTS dw.dim_customer (
       sk_customer SERIAL PRIMARY KEY,
       id_customer INT,
       name VARCHAR(255),
       type VARCHAR(255),
       city VARCHAR(255),
       state VARCHAR(50),
       country VARCHAR(255),
       insertion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   -- Dimension: Date
   CREATE TABLE IF NOT EXISTS dw.dim_date (
       sk_date SERIAL PRIMARY KEY,
       full_date DATE,
       day INT,
       month INT,
       year INT
   );

   -- Fact Table: Sales
   CREATE TABLE IF NOT EXISTS dw.fact_sales (
       sk_product INT NOT NULL,
       sk_customer INT NOT NULL,
       sk_channel INT NOT NULL,
       sk_date INT NOT NULL,
       quantity INT NOT NULL,
       sales_value DECIMAL(10, 2) NOT NULL,
       insertion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       PRIMARY KEY (sk_product, sk_customer, sk_channel, sk_date),
       FOREIGN KEY (sk_product) REFERENCES dw.dim_product (sk_product),
       FOREIGN KEY (sk_customer) REFERENCES dw.dim_customer (sk_customer),
       FOREIGN KEY (sk_channel) REFERENCES dw.dim_channel (sk_channel),
       FOREIGN KEY (sk_date) REFERENCES dw.dim_date (sk_date)
   );