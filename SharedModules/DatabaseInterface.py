import mysql.connector

from SharedModules.Logger import trace_logging

LOCALUSER = 'root'
LOCALPASSWORD = 'password'
LOCALHOST = 'localhost'
DATABASE = 'dni'

@trace_logging()
def newConnector():
    """eventually there will be environment based toggles on this function to modify how it reaches out to the database."""
    return mysql.connector.connect(user=LOCALUSER, password=LOCALPASSWORD,
                              host=LOCALHOST,
                              database=DATABASE)


class DatabaseInterface:

    def __init__(self):
        self.db = None

    @trace_logging()
    def get_database(self):
        if not self.db:
            self.db = newConnector()
        return self.db

    @trace_logging()
    def close_database(self):
        if self.db:
            self.db.close()
        self.db = None

    @trace_logging()
    def select(self, query: str):
        cursor = self.get_database().cursor(dictionary=True, buffered=True)
        cursor.execute(query)
        results = cursor.fetchall()
        self.close_database()
        return results

    @trace_logging()
    def update(self, query: str):
        self.get_database().cursor().execute(query)
        self.get_database().commit()
        self.close_database()

    @trace_logging()
    def insert(self, query: str):
        mycursor = self.get_database().cursor()
        mycursor.execute(query)
        id = mycursor.lastrowid
        self.get_database().commit()
        self.close_database()
        return id
