import pandas as pd
import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Default values for columns
default_values = {
    'SycSalutationId': 30,
    # Add more columns and their default values as needed
}

try:
    # Excel file path
    excel_file_path = 'MemberRegistration-5.xlsx'

    # SQL table name
    table_name = 'MemMemberRegistration'

    # Read Excel data using pandas
    df = pd.read_excel(excel_file_path)

    # Connect to the SQL Server database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Get the columns of the SQL table
    cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME NOT LIKE 'id' AND COLUMNPROPERTY(OBJECT_ID('{table_name}'), COLUMN_NAME, 'IsIdentity') <> 1")
    db_columns = [column[0] for column in cursor.fetchall()]

    # Map Excel columns to database table columns
    column_mapping = {}
    for column in df.columns:
        if column in db_columns:
            column_mapping[column] = column
    # Include default values for columns not present in the Excel data
    for column in db_columns:
        if column in default_values:
            column_mapping.setdefault(column, default_values[column])

    print(column_mapping.values())

    # Insert data into the SQL table
    for _, row in df.iterrows():
        values = ', '.join(
            [f"'{row.get(column, default_values.get(column, ''))}'" if isinstance(row.get(column), str) else f"'{str(row.get(column))}'" if column in row else f"{default_values.get(column, '')}" for column in column_mapping.values()])
        query = f"INSERT INTO {table_name} ({', '.join(column_mapping.values())}) VALUES ({', '.join(str(column_mapping[column]) for column in column_mapping)})"
        print(query)  # Print the query for debugging purposes
        try:
            cursor.execute(query)
        except pyodbc.ProgrammingError as e:
            print(e)

    # Commit the changes
    connection.commit()

    print('Data inserted successfully.')

except pyodbc.Error as e:
    print('Inserting Excel Data Issue: ', str(e))

finally:
    # Close the connection
    cursor.close()
    connection.close()
