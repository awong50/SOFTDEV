Elmos_Cheez-its: Amanda Tan, Ethan Sie, Aidan Wong

SoftDev

K19 - Creating databases with SQL

2024-10-18

time spent: 1.0

DISCOVERIES:
----------------------------------------------------
* Cannot run the build_db.py file multiple times without deleting the created database because tables with the same name cannot be created (would have to change the table name or the db output file)
* DictReader returns the contents of a CSV file in a dictionary and automatically sorts by each new line and seperates by comma
* When running SQL queries in the terminal, it requires the use of ';', but running it using c.execute() does not (or may have hidden consequences, but no visible differences)
* Multiple tables can exist in one database and thier names can be accessed using '.table' or '.tables' and their structures can be accessed using '.schema'
* Printing a 'c.execute' returns the sqlite3 cursor object


QUESTIONS/COMMENTS/CONCERNS:
----------------------------------------------------
Q: How secure are SQL queries without any guardrails/protections?

Q: Is there anyway to print the output when a SQL command is run through python?

C: Using '?' placeholders in the execution of SQL queries and defining what they are seems to be better practice and does not give an error (which happened when using fstring)
