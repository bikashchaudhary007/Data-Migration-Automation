import pandas as pd
import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"


try:
    # Excel file path
    excel_file_path = "MemberRegistration-5.xlsx"

    # SQL table name
    table_name = "MemMemberRegistration"

    # Read Excel data using pandas
    df = pd.read_excel(excel_file_path)

    # Define the data to update
    data = {
        "SycSalutationId": 30,    
    }
    df['SycSalutationId']=30


    '''
    set_values = []

    for key, value in data.items():
        set_values.append(f"{key}='{value}'")
    set_values_str = ', '.join(set_values)

    print(set_values_str)
    '''
    '''
    columns = ', '.join(data.keys())
    values = []
    for value in data.values():
        values.append(f"{value}")
    values_str_test = ', '.join(values)
    print(columns)
    print(values_str_test)
    '''

    # Connect to the SQL Server database
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Get the columns of the SQL table
    cursor.execute(
        f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME NOT LIKE 'id' AND COLUMNPROPERTY(OBJECT_ID('{table_name}'), COLUMN_NAME, 'IsIdentity') <> 1"
    )
    db_columns = [column[0] for column in cursor.fetchall()]

    # Map Excel columns to database table columns
    column_mapping = {}
    for column in df.columns:
        if column in db_columns:
            column_mapping[column] = column
    
    
 

    # print(column_mapping)
    # Insert data into the SQL table
    for index, row in df.iterrows():
        values = []
        for column in column_mapping.values():
            if isinstance(row[column], str):
                values.append(f"'{row[column]}'")
            else:
                values.append(f"'{str(row[column])}'")
                
        values_str = ", ".join(values)
        columns_str = ", ".join(column_mapping.values())

        for value in data.values():
            values.append(f"{str(value)}")
        
        values_str = ", ".join(values)
        for key in data.keys():
            column_mapping[f'{key}']=f'{key}'
      
        print(column_mapping)
        columns_str = ", ".join(column_mapping.keys())

        print(values_str)
        print(columns_str)
    
    

        # added code

        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

        try:
            cursor.execute(query)
        except pyodbc.ProgrammingError as e:
            print(e)

    # Commit the changes
    connection.commit()

    print("Data inserted successfully.")

except pyodbc.Error as e:
    print("Inserting Excel Data Issue: ", str(e))

finally:
    # Close the connection
    cursor.close()
    connection.close()
