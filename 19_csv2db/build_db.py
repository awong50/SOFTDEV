"""
Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong
SoftDev
K19 - Creating databases with SQL
2024-10-18
time spent: 1.0
"""

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# This code is very static, and relies on changing many aspects for new tables
commandCreateTable1 = 'CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)' # Builds the query to create the table, seperated from the students one for easier changes (in the case of varying column amounts)
c.execute(commandCreateTable1) # Command creates a table called courses with the columns code, mark, and id

with open('courses.csv', 'r') as file: # Opens the courses.csv file to read it
    reader = csv.DictReader(file) # Sets variable named reader to DictReader, which will allow the iteration of the csv file as dictionaries for each row
    commandInsert = 'INSERT INTO courses VALUES (?, ?, ?);' # Sets the general query to a variable to be reused through the for loop below (the variables inserted are the only things that change)
    for _ in reader: # Note: The DictReader object automatically uses the first line of the CSV to generate the keys (the columns), so it does not need to be skipped  
        c.execute(commandInsert, (_.get('code'), _.get('mark'), _.get('id'))) # Inserts the values from each dictionary returned from the reader into the table

# Same process as above, but for the students.csv file
commandCreateTable2 = 'CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)'
c.execute(commandCreateTable2)

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    commandInsert = 'INSERT INTO students VALUES (?, ?, ?);'
    for _ in reader:
        c.execute(commandInsert, (_.get('name'), _.get('age'), _.get('id')))

#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database