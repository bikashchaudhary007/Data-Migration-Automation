import pandas as pd
import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

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
    
    # Specify default values for specific columns
    default_values = {
        'SycSalutationId': 30,
        # Add more column names and default values as needed
    }
    
    # Insert data into the SQL table
    # Insert data into the SQL table
    # Insert data into the SQL table
    for index, row in df.iterrows():
        values = []
        for column in column_mapping.values():
            if column in row and isinstance(row[column], str):
                values.append(f"'{row[column]}'")
            elif column in row:
                values.append(f"'{str(row[column])}'")
            elif column in default_values:
                values.append(f"'{default_values[column]}'")
            else:
                values.append("NULL")

        values_str = ', '.join(values)
        columns_str = ', '.join([column for column in column_mapping.values() if column in row or column in default_values])
        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

        try:
            cursor.execute(query)
        except pyodbc.ProgrammingError as e:
            print(e)


    # Commit the changes
    connection.commit()

    print('Data inserted successfully.')

except pyodbc.Error as e:
    print('Inserting Excel Data Issue:', str(e))

finally: 
    # Close the connection
    cursor.close()
    connection.close()
