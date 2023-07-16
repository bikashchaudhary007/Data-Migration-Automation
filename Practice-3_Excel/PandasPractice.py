import pandas as pd
import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Excel file path
excel_file_path = 'MemberData.xlsx'
# excel_file_path = 'D:\Bikash Migration\MigrationPython\MemberRegistration.xlsx'

# # SQL table name
# table_name = 'MemberTable'

# Read Excel data using pandas
df = pd.read_excel(excel_file_path)
# print(df)

# print(df['age'].max())
# print(df['age'].mean())
# print(df.age.describe())
# print(df[df.age == df.age.max()])
# print(df.fullname[df.age == df.age.max()])

#new excel
# df.to_excel('NewExcel.xlsx', sheet_name='data', index=False)
# print('New Excel Formed')

"""
print('-------Rows X Columns------------')
print(df.shape)

print('\n -------Displays few top rows------------')
print(df.head())

print('\n -------Displays few bottom rows------------')
print(df.tail())


print('\n -------Slilcing------------')
print(df[2:5])


# print('\n -------Display Columns------------')
# print(df.columns)

print('\n -------Display Two Columns data------------')
print(df[['MemberId', 'FirstName']])
"""
"""
# Connect to the SQL Server database
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Get the columns of the SQL table
cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME NOT LIKE 'id'")
columns = [column[0] for column in cursor.fetchall()]

# Insert data into the SQL table
for _, row in df.iterrows():
    values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for _, value in row.items() if _ in columns])
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values})"
    print(query)  # Print the query for debugging purposes
    try:
        cursor.execute(query)
    except pyodbc.ProgrammingError as e:
        print(e)  # Print the error message for debugging purposes

# Commit the changes
connection.commit()

# Close the connection
cursor.close()
connection.close()

print('Data inserted successfully.')
"""