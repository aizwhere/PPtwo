import psycopg2
import csv
def delete_by_first_name(first_name):
    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM PhoneBook WHERE first_name = %s",
        (first_name,)
    )
    
    conn.commit()
    conn.close()

# Пример использования
delete_by_first_name('John')