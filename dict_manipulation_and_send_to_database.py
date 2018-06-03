# -*- coding: utf-8 -*-

# excel_data_to_dict is my own module
from excel_data_to_dict import excel_to_dictionary
import mysql.connector as sql
from mysql.connector import errorcode

# there is the excel file name I want to load from the same file this code file lies, otherwise "import os" is needed
excel_file ='database_project_exels.xlsx'
DB ='workers_and_departments'

connection= sql.connect(host="Localhost", user="root", passwd="", db= DB)
cursor = connection.cursor()

# these are globals so we can make "excel_data_to_dict" work
dicta = {}
workbook_names = []

# information is put to dicta and workbook_names
excel_to_dictionary(excel_file, dicta, workbook_names)

# print(dicta)
# print(workbook_names)

# iterating all of the sheet names
for sheet_name in workbook_names:
     # this is to put all of the items which contains sheet_name string in them to an array
     # excel_data_to_dict creates indexes to a dictionary with for loop. --> sheet name + str(i)
     # sheet_name = dog ---> for i in range(0,5) ---> dict['dog1'], dict['dog2'], dict['dog3'] and so on...
     asd = [value for key, value in dicta.items() if sheet_name in key.lower()]
     # datafields are reset when new sheet name
     # datafields are the fields to insert some values in a table 
     data_fields = ""
     
     
     # This is for the cursor to execute. This says to get fields that doesn't have attribute auto_increment
     # database system creates automatically the value when a field is created with auto_increment so...
     # we probably even cannot insert a value in a field with auto_increment attribute
     to_execute = ("SHOW FIELDS FROM "+DB+"."+sheet_name+" WHERE Extra NOT LIKE 'auto_increment'")
     
     #cursor now contains the query and now we can iterate over the cursor
     cursor.execute(to_execute)
     
     # we iterate over the cursor to create the fields we want to insert the values.
     for field in cursor:
         # print(field[0])
         # appending to string the datafields where we want to add to information
         data_fields += "{}, ".format(field[0])
     
     # we manipulate the string so that cursor can excute it
     # -2 because last value cannot have a comma. ---> data_fields - (comma + whitespace)
     data_fields= "("+ data_fields[:-2] +")"
     # print("datafields: ", data_fields)
     
     # adding data string for cursor to execute.
     add_data = ("INSERT INTO "+DB+"." + sheet_name + " " +data_fields +
                 " VALUES ")
     # list contains a list which has dictionaries in them so we must iterate over it like so
     for x in range(0,len(asd)):
         # temp_string is where the data is put
         temp_string = ""
         
         
         for y in range(0,len(asd[0])):
             # line by line the temp string gets the values of the list-dictionary-excel data into it
             # also what is interesting that now '' -notations are needed 
             temp_string += "\'{}\', ".format(asd[x][y])
             
             
         # string manipulation is needed again.
         temp_string = "(" +temp_string[:-2]+")"
         # print(temp_string)
         
         #add_data + temp_string makes the sql command complete and it is ready to be passed to cursor
         add_data += temp_string
         cursor.execute(add_data)
         
         # print("datan add: ",add_data)
         
         # After adding we delete the temp_string part from add_data and start again
         add_data = add_data[:-len(temp_string)] 
         
         
         # print("after cut:", add_data)
         
# remember to commit the changes, if one have done inserting without commit, auto_increment values are broken
# One needs to alter the table 
connection.commit()
cursor.close()

connection.close()