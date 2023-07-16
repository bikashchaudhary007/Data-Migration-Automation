from CRUD_Operations import CRUDOperations

# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

# Connect to the database
crud.connect()

# Define the data to update
data = {
    'age': 27
}

# Update the data in the table
crud.update_data('MemberTable', data, "mid = 8")
print('Data Updated')
# Disconnect from the database
crud.disconnect()
