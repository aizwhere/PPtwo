import psycopg2
import csv
def query_by_last_name(last_name):
    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM PhoneBook WHERE last_name = %s",
        (last_name,)
    )
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    conn.close()

