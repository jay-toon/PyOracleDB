# connector.py
''' Connector.py is a module that connects to the database and returns a true/false value based on the connection status.
    It also contains a function that returns the connection object.
    
    The connection object is used to execute queries on the database, as well as declare which database you are connecting to.
    It uses syntax similar to OracleDB, with a console to ease functionality and a developers life.
'''

def connect(username, password):
    try:
        connection = cx_Oracle.connect(username, password, "localhost:1521/xe")
        return True
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(error.message)
        return False