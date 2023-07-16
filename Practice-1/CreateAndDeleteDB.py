from DatabaseConnection import db_connection
import pyodbc


# Connect to the database
db_connection.connect()


# Create the database
def create_database(database_name):
    '''
    This is used to create database in SQL Server
    '''
    try:
        create_db_query = f'CREATE DATABASE {database_name}'
        db_connection.cursor.execute(create_db_query)
        print(f'Database {database_name} created successfully.')
    except pyodbc.Error as e:
        print('Database creation error:', str(e))



# delete database
def delete_database(database_name):
    '''
    This is used to delete database in SQL Server
    '''
    try:
        delete_db_query = f'DROP DATABASE {database_name}'
        db_connection.cursor.execute(delete_db_query)
        print(f'Database {database_name} deleted successfully.')
    except pyodbc.Error as e:
        print('Database deletation error:', str(e))


# #Creating Database
# create_database('SampleDB')

# delete_database('SampleDB')

# Disconnect from the database
db_connection.disconnect()
