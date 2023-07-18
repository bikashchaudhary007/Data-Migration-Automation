from CRUD_Operations import CRUDOperations

# Connection details
from configuration.config import server, database, username, password

# Create an instance of CRUDOperations
crud = CRUDOperations(server, database, username, password)

#Adding defaultvalues to member registration table
def MemberDefaultValues():
    # Connect to the database
    crud.connect()

    # Define the data to update
    data = {
        'SycMemberTypeId':3,
        'UsmOfficeId':2,
        'SycSalutationId': 30,
        'BirthOn':'1988-04-13',
        'BirthOnBS': '2045/01/01',
        'RegistrationOn': '2022-01-14',
        'SycMemberGroupId':11,
        'CreatedBy':0,
        'CreatedOn': '2022-01-14'

    }

    # Update the data in the table
    crud.add_default_values('MemMemberRegistration', data)
    print('Data Updated')
    # Disconnect from the database
    crud.disconnect()

