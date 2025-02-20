import mysql.connector
import random

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",  
    database="ecommerce"
)

cursor = db.cursor()

# Create the 'products' table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(255) PRIMARY KEY,
    price DECIMAL(10, 2)
)
""")

# Insert 1000 products
for i in range(1, 1001):
    product_id = f"prod_{i}"
    price = round(random.uniform(10.0, 100.0), 2)
    
    # Use a parameterized query to avoid SQL injection
    cursor.execute("INSERT INTO products (product_id, price) VALUES (%s, %s)", (product_id, price))

# Commit the transaction to the database
db.commit()

# Close the cursor and the connection
cursor.close()
db.close()

print("Products inserted successfully.")

# python3 -m venv venv