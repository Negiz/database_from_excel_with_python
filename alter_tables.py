# -*- coding: utf-8 -*-
from __future__ import print_function
import mysql.connector as sql

# my tables had some bad naming, forgotten columns and problems with auto_increment so I needed to alter them a bit

DB='Workers_and_departments'
connection = sql.connect(user="root", db=DB )
cursor = connection.cursor()

#cursor.execute("ALTER TABLE who_works_where ADD worked_hours int(4) ")
#cursor.execute("ALTER TABLE department CHANGE department_location location varchar(20)")

# This altering is because of the Auto_Increment increasing eventhough one does not commit to database
# Foreign key constraint fails if auto_increment values are wrong
# So if one has played with cursor.execute() and tried to insert values to a table and it FAILS
# -> AUTO_INCREMENT Value += 1
# So resetting the AUTO_INCREMENT Value to 1 is needed
cursor.execute("ALTER TABLE employee AUTO_INCREMENT =1")
cursor.execute("ALTER TABLE department AUTO_INCREMENT =1")
cursor.close()
connection.close()

