# database_from_excel_with_python

<h3> Created using... </h3>
<p> This projects was created by usings MySQL Workbench and Python.<br>
 XAMPP is also needed for MySQL workbench, since it MySQL Workbench needs a server to work with.<br>
  XAMPP provides a kind of virtual server, which is contained within one's computer.<br>
 </p>

<h3> Files contains? </h3>

<ul>
  <li><b>alter_tables</b> = just alter table commands in sql</li>
  <li><b>Creating_database_...</b> is creating tables and database (foreign are also created here)</li>
  <li><b>Database_project_exels</b> is the excel file from which data is extracted</li>
  <li><b>Dict_manipulation_..</b> is where data is extracted from dictionary and made suitable for a sql command</li>
  <li><b>Excel_data_to_dict</b> is the code which extracts the data from the excel file</li>
  <li>the sql file is the database which was created from these</li>
</ul>

<h2> Excel_data_to_dict and dict_manipulation... </h2>
  <p> Excel_data_to_dict = exceldict<br>
  dict_manipulation = dict_m</p>
  <p> <br> exceldict needs import openpyxl to work.<br>
  exceldict should extract all the data from an excel file and put it into a dictionary.<br>
  Exceldict ignores the first row in the excel file. <br>
  I am not sure how data extraction behaves with empty fields<br>
  Indexing will be done with putting sheet name + str(for loop number) to dictionary<br><br>
  -> sheet_name = dog &emsp; for x in range(1,5) &emsp;--> dictionary['dog1'], dictionary['dog2'] and so on..<br><br>
  There are two methods, one can get dictionary or dictionary and workbook_names (sheet names in an excel file)<br>
  <b>Methods don't return anything</b><br> -> put values into GLOBAL dictionary (workbook_names have to be put into global array if used)
  <br><br>
  dict_m manipulates the values of dictionary (from excel) so, that they´re ready to be inserted into database<br>
  In a sense, if one has already built a database, one can create an excel file with database's table (table name = sheet name)<br>
  While inserting, the field values have to be also in same order in excel file. <br>
  TABLE asd (id,first_name,last_name) with excel Sheetname asd (id,first_name,last_name) <br>
  This code doesn't insert into auto_increment fields, it ignores them. 
  </p>
  
