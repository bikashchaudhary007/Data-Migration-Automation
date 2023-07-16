import pyodbc

# Connection details
server = 'COSYSSERVER\SQLEXPRESS'
database = 'HelloDB'
username = 'sa'
password = 'Kt2GLWShdLua3'


connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


# try:
#     # Establish a connection
#     with pyodbc.connect(connection_string) as connection:
#         print('Connected to SQL Server')
#         # Perform database operations here
        
# except pyodbc.Error as e:
#     print('Connection error:', str(e))


try:
    # Establish a connection
    with pyodbc.connect(connection_string) as connection:
        print('Connected to SQL Server')
        
        # Create a cursor
        cursor = connection.cursor()
        
        # Execute a query
        cursor.execute('SELECT * FROM TestTable')
        
        # Fetch the data
        rows = cursor.fetchall()
        
        # Process the data
        for row in rows:
            print(row)  # Print each row
            
except pyodbc.Error as e:
    print('Connection error:', str(e))
