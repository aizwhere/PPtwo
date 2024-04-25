import psycopg2
import csv
def insert_data_from_console():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone_number = input("Введите номер телефона: ")

    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
        (first_name, last_name, phone_number)
    )
    
    conn.commit()
    conn.close()

insert_data_from_console()