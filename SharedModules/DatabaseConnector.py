import mysql.connector

LOCALUSER = 'root'
LOCALPASSWORD = 'password'
LOCALHOST = 'localhost'
DATABASE = 'dni'

def newConnector():
    """eventually there will be environment based toggles on this function to modify how it reaches out to the database."""
    return mysql.connector.connect(user=LOCALUSER, password=LOCALPASSWORD,
                              host=LOCALHOST,
                              database=DATABASE)
