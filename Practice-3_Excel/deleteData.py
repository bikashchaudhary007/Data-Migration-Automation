from CRUD_Operations import CRUDOperations
import pyodbc
# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

def DeleteData(tableName, reqCondition):
    try: 
        # Connect to the database
        crud.connect()

        # Define the condition to specify the rows to delete
        condition = reqCondition

        # Delete the data from the table
        crud.delete_data(f'{tableName}', condition)
        print('Data Deleted')

    except pyodbc.Error as e:
        print('Deletation Error: ', str(e))
    
    finally:
        # Disconnect from the database
        crud.disconnect()

flag = True
while (flag == True) :
        #Taking user input
        print('******************Fetching data from database table************************')
        tblName = input("Enter the table name: ")
        userId = input('Enter the id: ')

        askConfirm = input(f'Are you sure to delete mid: {userId} from table: {tblName} [Y/N]: ')
        if (askConfirm.upper()=='Y' or askConfirm.upper()=='YES'):
            DeleteData(tableName=tblName, reqCondition=f'mid = {userId}')
        else: 
             print('Thank You!')
             break
        
        choice = input("Do you want to delete another data [Y/N]: ")
        if (choice.upper() == 'Y' or choice.upper() == 'YES'):
             flag = True
        else: 
             flag = False


