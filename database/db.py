# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:50:26 2017

@author: James Kinyua
"""
import sqlite3

from contextlib import closing

db_name = 'todo.sqlite'
# Define a global connection object
conn = None

def connect_db():
    """
    Connect to the database.
    """
    global conn
    if not conn:
        # Connect to the database and return a connection object.
        conn = sqlite3.connect(db_name)
        # Allow the use of column names when accessing the result sets.
        conn.row_factory = sqlite3.Row
        
def close_db():
    """
    Close the database connection.
    """
    if conn:
        conn.close()
