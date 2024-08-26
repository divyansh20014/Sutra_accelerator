# import psycopg2
# import json
# from datetime import datetime

# def get_customer_profile(customer_id):
#     """
#     Fetch customer profile from PostgreSQL database based on customer ID.

#     Args:
#     - customer_id (int): The ID of the customer whose profile is to be fetched.

#     Returns:
#     - dict: Customer profile data if successful, else None.
#     """
#     try:
#         conn = psycopg2.connect(
#             database="mydb",
#             user="postgres",
#             password="Admin@123",
#             host="127.0.0.1",
#             port="5432"
#         )
#         cursor = conn.cursor()

#         # Query to fetch customer profile
#         query = """
#         SELECT 
#             full_name, date_of_birth, address, last_transaction_amount, 
#             phone_number, account_number, account_balance, 
#             last_transaction_time, transaction_count_last_20_minutes
#         FROM customer_profile
#         WHERE customer_id = %s;
#         """
        
#         cursor.execute(query, (customer_id,))
#         row = cursor.fetchone()

#         if row:
#             profile = {
#                 "full_name": row[0],
#                 "date_of_birth": row[1].isoformat() if row[1] else None,
#                 "address": row[2],
#                 "last_transaction_amount": float(row[3]),
#                 "phone_number": row[4],
#                 "account_number": row[5],
#                 "account_balance": float(row[6]),
#                 "last_transaction_time": row[7].isoformat() if row[7] else None,
#                 "transaction_count_last_20_minutes": int(row[8])
#             }
#             return profile
#     except Exception as e:
#         print(f"Error fetching customer profile: {e}")
#     finally:
#         cursor.close()
#         conn.close()
    
#     return None

# fetch_customer_profile.py

import psycopg2
import json
from datetime import datetime

def get_customer_profile(customer_id):
    """
    Fetch customer profile from PostgreSQL database based on customer ID.

    Args:
    - customer_id (int): The ID of the customer whose profile is to be fetched.

    Returns:
    - dict: Customer profile data if successful, else None.
    """
    try:
        conn = psycopg2.connect(
            database="defaultdb",
            user="avnadmin",
            password="AVNS_2XQTCdBeEubwHxg8p7A",
            host="pg-3986967a-gupta-e6ec.h.aivencloud.com",
            port="28514"
        )
        cursor = conn.cursor()

        # Query to fetch customer profile
        query = """
        SELECT 
            full_name, date_of_birth, address, last_transaction_amount, 
            phone_number, account_number, account_balance, 
            last_transaction_time, transaction_count_last_20_minutes
        FROM customer_profile
        WHERE customer_id = %s;
        """
        
        cursor.execute(query, (customer_id,))
        row = cursor.fetchone()

        if row:
            profile = {
                "full_name": row[0],
                "date_of_birth": row[1].isoformat() if row[1] else None,
                "address": row[2],
                "last_transaction_amount": float(row[3]),
                "phone_number": row[4],
                "account_number": row[5],
                "account_balance": float(row[6]),
                "last_transaction_time": row[7].isoformat() if row[7] else None,
                "transaction_count_last_20_minutes": int(row[8])
            }
            return profile
        else:
            print(f"No profile found for customer_id: {customer_id}")
    except Exception as e:
        print(f"Error fetching customer profile: {e}")
    finally:
        cursor.close()
        conn.close()
    
    return None
