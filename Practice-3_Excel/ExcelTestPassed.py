import pandas as pd
import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def InsertExcelData(tableName, excelPath, connection_string=connection_string):
    try: 
        # Excel file path
        excel_file_path = excelPath 

        # SQL table name
        table_name = tableName 

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
        
        # Insert data into the SQL table
        for _, row in df.iterrows():
            # values = ', '.join([f"'{row[column]}'" if isinstance(row[column], str) else str(row[column]) for column in column_mapping.values()])
            values = ', '.join([f"'{row[column]}'" if isinstance(row[column], str) else f"'{str(row[column])}'" for column in column_mapping.values()])

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

flag = True
while flag:
    # Taking user input
    print('******************Inserting excel data from database table************************')
    tblName = input("Enter the table name: ")
    exlPath = input("Enter the excel path: ")

    InsertExcelData(tableName=tblName, excelPath=exlPath)

    choice = input("Do you want to insert another excel data [Y/N]: ")
    if choice.upper() == 'Y' or choice.upper() == 'YES':
        flag = True
    else: 
        flag = False


