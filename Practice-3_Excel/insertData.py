from CRUD_Operations import CRUDOperations
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

# Connect to the database
crud.connect()

# Define the data to insert
data = {
    'product_name': 'TestData-2',
    'product_rate': 30
}

# Insert the data into the table
crud.insert_data('TestTable', data)
print('Data inserted')

# Disconnect from the database
crud.disconnect()
