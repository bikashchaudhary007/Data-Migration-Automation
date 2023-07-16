import pyodbc

class DatabaseConnection:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_string = f'DRIVER={{SQL Server}};SERVER={server};UID={username};PWD={password}'
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.connection_string) #,autocommit=True
            self.cursor = self.connection.cursor()
            print('Connected to SQL Server')
        except pyodbc.Error as e:
            print('Connection error:', str(e))

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print('Disconnected from SQL Server')

    

# Create an instance of DatabaseConnection
db_connection = DatabaseConnection('COSYSSERVER\SQLEXPRESS', 'HelloDB', 'sa', 'Kt2GLWShdLua3')




