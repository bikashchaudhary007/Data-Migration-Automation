from CRUD_Operations import CRUDOperations

# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

# Connect to the database
crud.connect()

# Define the data to update
data = {
    'product_rate': 370
}

# Update the data in the table
crud.update_data('TestTable', data, "product_name = 'John Doe'")
print('Data Updated')
# Disconnect from the database
crud.disconnect()
