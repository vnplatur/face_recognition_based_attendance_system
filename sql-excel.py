import pandas as pd
import sqlite3

connection = sqlite3.connect("face.db")
# Construct your SQL query to get the databse info you need. Alternatively,
# you could grab individual tables as DataFrames and use pandas to merge them.
# If you just need a table, you can specify the table name instead of a SQL query
query = "SELECT * FROM ATTENDANCE"
df = pd.read_sql(query, connection)
df.to_excel("attendace_sheet.xlsx")