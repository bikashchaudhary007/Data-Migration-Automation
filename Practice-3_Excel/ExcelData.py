import pandas as pd
import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Excel file path
excel_file_path = 'MemberData.xlsx'

# SQL table name
table_name = 'MemberTable'

# Read Excel data using pandas
df = pd.read_excel(excel_file_path)

# Connect to the SQL Server database
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Insert data into the SQL table
for index, row in df.iterrows():
    values = ', '.join([f"'{value}'" for value in row])
    query = f"INSERT INTO {table_name} VALUES ({values})"
    cursor.execute(query)

# Commit the changes
connection.commit()

# Close the connection
cursor.close()
connection.close()

print('Data inserted successfully.')
