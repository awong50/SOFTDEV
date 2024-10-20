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

# Dynamic Code that adjusts for any number of columns, column names and csv files

def typeTest(value): 
    try: # Attempts to make the string an int --> if it works its an int
        int(value)
        return 'INTEGER'
    except ValueError:
        try: # Attempts to make it a float
            float(value)
            return 'REAL'
        except ValueError: # If not a number, make it text
            return 'TEXT'
    

def createTable(tableName, file_path): # Takes in the desired table name and the file path to the csv file
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        header = True # Tracks if it is the first iteration of the loop
        columns = [] # Will contain the column name and its type
        columnsName = []  # Only contains the column name
        for _ in reader:
            if header: # Create the table if it is the first iteration of the loop
                for col in _.keys():
                    #print(_.get(col)) 
                    colType = typeTest(_.get(col)) # Uses typeTest function to get the type of the value in each column key
                    columns.append(f'{col} {colType}') # Adds the information to columns list
                    columnsName.append(f'{col}') # Adds the name of the column to the columnsName list 
                command = f'CREATE TABLE {tableName} ({", ".join(columns)})' # Builds query to create the table
                c.execute (command) # Executes query
                header = False # Tells the loop that it is no longer the first iteration --> The code in this if statement can only be run once per function run
            
            placeholders = ','.join('?' for name in columnsName) # Variable amount of placeholders '?' (Due to unknown amount of columns)
            values = tuple(_[value] for value in columnsName) # Creates an immutable tuple for every value in each key of columnsName 
            command = f'INSERT INTO {tableName} VALUES ({placeholders});' # Creates query to add it to the table
            c.execute(command, values) # Executes query

# Runs the createTable function for courses.csv and students.csv               
createTable('courses', 'courses.csv')
createTable('students', 'students.csv')

#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database