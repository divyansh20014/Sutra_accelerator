import psycopg2

try:
    conn = psycopg2.connect(
         database="defaultdb",
        user="avnadmin",
        password="AVNS_2XQTCdBeEubwHxg8p7A",
        host="pg-3986967a-gupta-e6ec.h.aivencloud.com",
        port="28514"
    )
    print("Connection successful!")
except Exception as e:
    print("Error:", e)
finally:
    if conn:
        conn.close()