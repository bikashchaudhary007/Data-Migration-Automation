import pyodbc

class DatabaseConnection:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.connection_string, autocommit=True)
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

    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except pyodbc.Error as e:
            print('Error while fetching data:', str(e))


# Create an instance of DatabaseConnection
db_connection = DatabaseConnection('COSYSSERVER\\SQLEXPRESS', 'HelloDB', 'sa', 'Kt2GLWShdLua3')
db_connection.connect()

# Fetch data from the SQL Server using a query
query = 'SELECT * FROM TestTable'
result = db_connection.fetch_data(query)
for row in result:
    print(row)

# Disconnect from the SQL Server
db_connection.disconnect()

