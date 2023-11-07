#!python
import sqlite3
"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

file = 'database.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()

query = """
create table if not exists customers (
id integer primary key autoincrement,
pet_name tinytext,
pet_species tinytext,
pet_breed tinytext,
owner_name tinytext,
owner_phone int,
owner_email tinytext,
owner_balance int,
dofv tinytext);
"""
cursor.execute(query)


petname = str(input("What is your pets name?: "))
petspecies = str(input("What species is your pet?: "))
petbreed = str(input("What breed is your pet?: "))
ownername = str(input("What is your name?: "))
ownerphone = int(input("What is your phone number?: "))
owneremail = str(input("What is your email?: "))
ownerbalance = int(input("What is your balance?: "))
dateofv = str(input("What is the date today?: "))


cursor.execute(query)
cursor.execute('PRAGMA table_info(customers);')
query = f"insert into customers (pet_name, pet_species, pet_breed, owner_name, owner_phone, owner_email, owner_balance, dofv) values ('{petname}','{petspecies}','{petbreed}','{ownername}','{ownerphone}','{owneremail}','{ownerbalance}','{dateofv}');"
print(query)
cursor.execute(query)
connection.commit()
query = "select * from customers"
cursor.execute(query)
print(cursor.fetchall())



ask = input("what would you like to search for? id, owner phone, or owner email: " ) 
if ask == "id":
    ans = input("what is your id?: ")
    query = f"select * from customers where id = '{ans}'"
    cursor.execute(query)
    print(cursor.fetchall())

elif ask == "owner phone":
    ans2 = int(input("what is your phone number?: "))
    query = f"select * from customers where owner_phone = '{ans2}'"
    cursor.execute(query)
    print(cursor.fetchall())

elif ask == "owner email":
    ans3 = str(input("what is your email?: "))
    query = f"select * from customers where owner_email = '{ans3}'"
    cursor.execute(query)
    print(cursor.fetchall())