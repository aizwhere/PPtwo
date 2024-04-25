import psycopg2
import csv
filename="C:\Users\Admin\Desktop\pp2spring\lab9\3.csv"
def insert_data_from_csv(filename):
    conn = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовки
        for row in reader:
            cursor.execute(
                "INSERT INTO PhoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )
    
    conn.commit()
    conn.close()

insert_data_from_csv('phonebook.csv')