from datetime import date
from EnglishNepaliDate import EnglishToNepali


today = date.today()

todayDateInBs=EnglishToNepali(str(today))

# print(EnglishToNepali(today))

default_values = {
    'SycMemberTypeId': 3,
    'UsmOfficeId': 2,
    'SycSalutationId': 30,
    'BirthOn': '1988-04-13',
    'BirthOnBS': '2045/01/01',
    'EmailAddress': 'name@gmail.com',
    'SycNationalityId': 5,
    'SycOccupationId': 2,
    'SycReligionId': 1,
    'SycMaritalStatusId': 3,
    'SycCasteId': 3,
    'SycGenderId': 1,
    'SycVdcId': 1,
    'RegistrationOn': '2013-04-14',
    'RegistrationOnBS': '2070/01/01',
    'IntroducedBy': 0,
    'SycStatusId': 1,
    'SycMemberGroupId': 11,
    'CreatedBy': 0,
    'CreatedOn':today,
    'CreatedOnBs':todayDateInBs,
    'CitizenShipIssuedOn':'2008-04-13',
    'CitizenShipIssuedOnBs':'2065/01/01',
    'SycStateVDCId':2
    # Add more column names and default values as needed
}


