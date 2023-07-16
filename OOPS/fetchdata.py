from CRUD_Operations import CRUDOperations

# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

def getData():
    # Connect to the database
    crud.connect()

    # Execute a SELECT query
    crud.execute_query('SELECT * FROM TestTable')

    # Fetch all rows
    rows = crud.fetch_all_rows()

    # Process the fetched data
    for row in rows:
        print(row)

    # Disconnect from the database
    crud.disconnect()


getData()
