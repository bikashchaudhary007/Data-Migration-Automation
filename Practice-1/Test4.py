import pyodbc
from DatabaseConnection import db_connection

# db_connection.connect()

connstring = db_connection.connection_string
print(connstring )

#Performing database operations

#Fetching data
def getData():
    try:
    # Establish a connection
        with pyodbc.connect(connstring) as connection:
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
    finally:
        #Disconnect from the database
        db_connection.disconnect()


# getData()


