from ConnectDatabase import DatabaseConnection

class CRUDOperations:
    def __init__(self, server, database, username, password):
        self.db = DatabaseConnection(server, database, username, password)
        self.cursor = None

    def connect(self):
        self.db.connect()
        self.cursor = self.db.connection.cursor()

    def disconnect(self):
        self.db.disconnect()
        self.cursor = None

    def execute_query(self, query):
        self.cursor.execute(query)

    def fetch_all_rows(self):
        return self.cursor.fetchall()

    def insert_data(self, table, data):
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.execute_query(query)
        self.db.connection.commit()

    def update_data(self, table, data, condition):
        set_values = ', '.join([f"{key}='{value}'" for key, value in data.items()])
        query = f"UPDATE {table} SET {set_values} WHERE {condition}"
        self.execute_query(query)
        self.db.connection.commit()

    def add_default_values(self, table, data):
        set_values = ', '.join([f"{key}='{value}'" for key, value in data.items()])
        query = f"UPDATE {table} SET {set_values}"
        self.execute_query(query)
        self.db.connection.commit()

    def delete_data(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)
        self.db.connection.commit()
