import pandas as pd
import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Excel file path
    excel_file_path = 'MemberRegistration-2.xlsx'

    # SQL table name
    table_name = 'MemMemberRegistration'

    # Read Excel data using pandas
    df = pd.read_excel(excel_file_path)

    # Connect to the SQL Server database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Get the columns of the SQL table
    cursor.execute(
        f"SELECT COLUMN_NAME, COLUMN_DEFAULT FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME NOT LIKE 'id' AND COLUMNPROPERTY(OBJECT_ID('{table_name}'), COLUMN_NAME, 'IsIdentity') <> 1")
    db_columns = {column[0]: column[1] for column in cursor.fetchall()}

    # Map Excel columns to database table columns and default values
    column_mapping = {}
    for column in df.columns:
        if column in db_columns:
            column_mapping[column] = db_columns[column]

    print(column_mapping)
    # Insert data into the SQL table
    for _, row in df.iterrows():
        column_names = list(column_mapping.keys())
        column_values = []
        for column_name in column_names:
            if column_mapping[column_name] is not None:
                column_values.append(f"'{row[column_name]}'")
            else:
                column_values.append(str(column_mapping[column_name]))

        query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(column_values)})"
        try:
            cursor.execute(query)
        except pyodbc.ProgrammingError as e:
            print(e)  # Print the error message for debugging purposes

    # Commit the changes
    connection.commit()

    print('Data inserted successfully.')

except pyodbc.Error as e:
    print('Inserting Excel Data Issue: ', str(e))

finally:
    # Close the connection
    cursor.close()
    connection.close()
