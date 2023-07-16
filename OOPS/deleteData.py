from CRUD_Operations import CRUDOperations

# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

# Connect to the database
crud.connect()

# Define the condition to specify the rows to delete
condition = "pid = 9"

# Delete the data from the table
crud.delete_data('TestTable', condition)
print('Data Deleted')

# Disconnect from the database
crud.disconnect()
