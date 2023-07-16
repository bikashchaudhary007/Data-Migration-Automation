import pyodbc
from configuration.config import server, database, username, password

class DatabaseConnection:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_string = f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.connection_string)
            print('Connected to SQL Server')
        except pyodbc.Error as e:
            print('Connection error:', str(e))

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print('Disconnected from SQL Server')
            self.connection = None


# c1 = DatabaseConnection(server, database, username, password)
# c1.connect()
