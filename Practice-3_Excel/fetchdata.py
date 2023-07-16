import pyodbc
from CRUD_Operations import CRUDOperations

# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

def getData(tableName):
    try: 
        # Connect to the database
        crud.connect()

        # Execute a SELECT query
        crud.execute_query(f'SELECT * FROM {tableName}')

        # Fetch all rows
        rows = crud.fetch_all_rows()

        # Process the fetched data
        for row in rows:
            print(row)
    except pyodbc.Error as e:
        print("Fetching error: ", str(e))
    
    finally:
        # Disconnect from the database
        crud.disconnect()

flag = True
while (flag == True) :
        #Taking user input
        print('******************Fetching data from database table************************')
        tblName = input("Enter the table name: ")

        getData(tblName)
        
        choice = input("Do you want to fetch again [Y/N]: ")
        if (choice.upper() == 'Y' or choice.upper() == 'YES'):
             flag = True
        else: 
             flag = False


             

