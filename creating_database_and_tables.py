# -*- coding: utf-8 -*-

from __future__ import print_function
import mysql.connector as sql
from mysql.connector import errorcode

# This is done mostly according to examples provided in site:
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html


#database name
DB='Workers_and_departments'

# A dictionary is declared for tables
TABLES = {}

# just basic sql to create tables.
#interesting part is that there will be errors if one uses '' -notations when declaring a field
# 'employee_id' incorrect  -------> employee_id correct



TABLES['employee']=(
        "CREATE TABLE employee("
        " employee_id int(11) NOT NULL AUTO_INCREMENT, "
        " first_name varchar(20) NOT NULL, "
        " last_name varchar(25) NOT NULL, "
        " telephone varchar(10) NOT NULL, "
        " address varchar(30) NOT NULL, "
        " city varchar(20) NOT NULL, "
        " zip int(5) NOT NULL, "
        " PRIMARY KEY(employee_id)"
        ") ENGINE=InnoDB")

TABLES['department']=(
        "CREATE TABLE department("
        " department_id int(11) NOT NULL AUTO_INCREMENT, "
        " name varchar(15) NOT NULL, "
        " floor_number int(2) NOT NULL, "
        " department_location varchar(20) NOT NULL, "
        " PRIMARY KEY (department_id) "
        ") ENGINE=InnoDB")

# I had troulbe with Foreign keys. I thought it was an index problem, but it appeared to be a comma in wrong place
# INDEX and CONSTRAINT sentences are probably not needed then...
# This table had other problems as well, since it has two foreign keys with both being an auto_increment value.


TABLES['who_works_where']=(
        "CREATE TABLE who_works_where("
        " department_departmentid int(11) NOT NULL, "
        " employee_employeeid int(11) NOT NULL, "
        " INDEX fk_who_works_where_department1_idx (department_departmentid), "
        " INDEX fk_who_works_where_employee1_idx (employee_employeeid), "
        " PRIMARY KEY (department_departmentid, employee_employeeid), "
        " CONSTRAINT fk_who_works_where_department1 "
        " FOREIGN KEY (department_departmentid) "
        " REFERENCES Workers_and_departments.department (department_id), "
        " CONSTRAINT fk_who_works_where_employee1 "
        " FOREIGN KEY (employee_employeeid) "
        " REFERENCES Workers_and_departments.employee (employee_id) "
        ") ENGINE=InnoDB")

# connection to database with mysql.connector --> as sql
connection = sql.connect(user="root")
# cursor is the object which allows querying data or inserting it. 
# Kind of textfield in which one puts command and which interracts with the database  
cursor = connection.cursor()

# this def is to create a database if the database doesn't exist, see the try: except: AFTER the whole def function

def create_db(cursor):
    try:
        cursor.execute("CREATE DATABASE {}".format(DB))
    except sql.Error:
        print("Failed to create database: {}".format(sql.Error))
        exit(1)

# if connection cannot be eshtablished then we goto def create_db
try:
    connection.database = DB
except sql.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        
        create_db(cursor)
        # after creating db we try to connect to it.
        connection.database=DB
    # if this doesn't work we just say there is a somesort of error
    else:
        print("There was an error: ", err)
    # exit(1) means usually an unsuccessful termination of a process? - exit(0) means successful program termination
        exit(1)

# goint through the the TABLE dictionary with .items()
for table, lines in TABLES.items():
    
    # try is there to resist if a certain table exists already
    try:
        
        # it is probably a good conduct to get a message what the program is doing
        print("Creating table: {}".format(table), end='')
        
        # this is where the information is made into a command to the database
        cursor.execute(lines)
        
    except sql.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(" already exists.")
        else:
            print(err.msg)

# apparently there is no connection.commit() needed when creating tables
# when inserting values into tables then connection.commit() is needed
cursor.close()
connection.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
