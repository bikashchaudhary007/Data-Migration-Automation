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
    cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME NOT LIKE 'id' AND COLUMNPROPERTY(OBJECT_ID('{table_name}'), COLUMN_NAME, 'IsIdentity') <> 1")
    db_columns = [column[0] for column in cursor.fetchall()]

    # Default values for columns not present in the Excel data
    default_values = {
        'SycSalutationId': 30,
        # Add more columns and their default values as needed
    }

    # Map Excel columns to database table columns
    column_mapping = {}
    for column in df.columns:
        if column in db_columns:
            column_mapping[column] = column
        elif column in default_values:
            column_mapping[column] = default_values[column]

    # Insert data into the SQL table
    for _, row in df.iterrows():
        values = []
        for column in column_mapping.values():
            if column in row:
                value = row[column]
            else:
                value = default_values[column]
            if isinstance(value, str):
                value = f"'{value}'"
            elif isinstance(value, pd.Timestamp):
                value = f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'"
            else:
                value = str(value)
            values.append(value)
        values = ', '.join(values)


        query = f"INSERT INTO {table_name} ({', '.join(column_mapping.values())}) VALUES ({values})"
        print(query)  # Print the query for debugging purposes
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
