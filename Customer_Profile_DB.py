import psycopg2
from datetime import datetime, timedelta

def create_customer_profile_table():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        database="defaultdb",
        user="avnadmin",
        password="AVNS_2XQTCdBeEubwHxg8p7A",
        host="pg-3986967a-gupta-e6ec.h.aivencloud.com",
        port="28514"
    )
    cursor = conn.cursor()

    # Create table SQL
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS customer_profile (
        customer_id SERIAL PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        date_of_birth DATE,
        address TEXT,
        last_transaction_amount NUMERIC(10, 2),
        phone_number VARCHAR(15),
        account_number VARCHAR(20),
        account_balance NUMERIC(10, 2),
        last_transaction_time TIMESTAMP,
        transaction_count_last_20_minutes INT
    );
    """
    
    # Execute the SQL command to create the table
    cursor.execute(create_table_sql)
    conn.commit()
    print("Customer profile table created successfully.")

    # Insert 5 specific entries
    insert_sql = """
    INSERT INTO customer_profile (
        full_name, date_of_birth, address, last_transaction_amount, 
        phone_number, account_number, account_balance, 
        last_transaction_time, transaction_count_last_20_minutes
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    
    entries = [
        ("John D", "1985-03-25", "123 Elm St, Springfield", 250.75, "+1-555-1234", "000123456789", 1500.00, datetime.now() - timedelta(minutes=5), 3),
        ("Jane Smith", "1990-07-13", "456 Oak St, Springfield", 320.50, "+1-555-5678", "000987654321", 2200.00, datetime.now() - timedelta(minutes=10), 2),
        ("Alice Johnson", "1982-11-30", "789 Pine St, Springfield", 1500.00, "+1-555-8765", "000112233445", 5000.00, datetime.now() - timedelta(minutes=15), 1),
        ("Bob Brown", "1975-09-22", "101 Maple St, Springfield", 75.00, "+1-555-4321", "000556677889", 800.00, datetime.now() - timedelta(minutes=18), 4),
        ("Charlie Davis", "2000-01-01", "202 Birch St, Springfield", 420.00, "+1-555-6789", "000998877665", 3000.00, datetime.now() - timedelta(minutes=12), 5)
    ]
    
    for entry in entries:
        cursor.execute(insert_sql, entry)

    conn.commit()
    print("5 specific entries inserted successfully.")

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_customer_profile_table()
