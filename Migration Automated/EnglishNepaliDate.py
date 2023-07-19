import pyodbc
from configuration.config import server, database, username, password

# Connection details
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def EnglishToNepali(engDate):
    try:
        # Connect to the SQL Server database
        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        # Use parameterized query to prevent SQL injection
        query = "SELECT dbo.ConvertDateEnglishToNepali(?)"
        resultDate = cursor.execute(query, engDate).fetchone()

        return resultDate[0] if resultDate else None

    except pyodbc.Error as e:
        print(f"Error executing the SQL query: {str(e)}")

    finally:
        # Close the cursor and connection in the finally block
        cursor.close()
        connection.close()
