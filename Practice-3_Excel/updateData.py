from CRUD_Operations import CRUDOperations

# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

def MemberDefaultValues():
    # Connect to the database
    crud.connect()

    # Define the data to update
    data = {
        'SycSalutationId': 30,
        'PermanentAddessDetail':'KTM'
    }

    # Update the data in the table
    crud.update_data('MemMemberRegistration', data, "MemberId like '%MR%'")
    print('Data Updated')
    # Disconnect from the database
    crud.disconnect()
