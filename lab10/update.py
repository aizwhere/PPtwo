import psycopg2
import csv
def update_phone_number_by_name(first_name, new_phone_number):
    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE PhoneBook SET phone_number = %s WHERE first_name = %s",
        (new_phone_number, first_name)
    )
    
    conn.commit()
    conn.close()