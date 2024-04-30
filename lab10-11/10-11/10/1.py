import psycopg2 
import csv 
 
conn = psycopg2.connect( 
    host="localhost", 
    database="suppliers", 
    user="postgres", 
    password="151006" 
) 
 
cur = conn.cursor() 
 
def inputData(): 
        name = input("Hello input your name: ") 
        number = input("Input your phone number: ") 
        cur.execute(' INSERT INTO phonebook("name", "number") VALUES( %s, %s); ' , (name, number)) 
 
def importFromCSV(): 
        with open(r'C:\Users\murat\Documents\PPtwo\lab10-11\10-11\10\phoneBook.csv', 'r') as file: 
            reader = csv.reader(file) 
            for row in reader: 
                personName, phoneNumber = row 
                cur.execute(' INSERT INTO phonebook("name", "number") VALUES( %s, %s); ', (personName, phoneNumber)) 
 
 
def update_contact(personName, phoneNumber): 
        cur.execute(' UPDATE phonebook SET "number" = %s WHERE "name" = %s ', (phoneNumber, personName)) 
 
 
def deleteData(): 
        print("Which name do you want to delete?\n") 
        personName = input() 
        cur.execute(f''' DELETE FROM phonebook WHERE "name"='{personName}' ''') 
 
def deleteAllData(): 
        cur.execute(' DELETE FROM phonebook ') 
 
done = False 
while not done: 
        print("What do you want to do?\n\
        1. Input data from console\n\
        2. Upload form csv file\n\
        3. Update existing contact\n\
        4. Query data from the table\n\
        5. Delete data from table by person name\n\
        6. Delete all data from table\n\
        7. Exit")

        x = int(input("Enter number 1-5\n")) 
        if(x == 1): 
            inputData() 
        elif(x == 2): 
            importFromCSV() 
        elif(x == 3): 
            print("Which number do you want to update? Enter name and new number: ") 
            name = input() 
            newNumber = input() 
            update_contact(name, newNumber) 
        elif(x == 5): 
            deleteData() 
        elif(x == 6): 
            deleteAllData() 
        elif(x == 7): 
            done = True 
        conn.commit() 
         
cur.close() 
conn.close()