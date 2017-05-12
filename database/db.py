# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:50:26 2017

@author: James Kinyua
"""
import sqlite3

from contextlib import closing

from .. import Collection, Item

db_name = 'todo.sqlite'

class TodoDB:
    def __init__(self):
        # Define a connection object.
        self.conn = None
        
    def connect_db(self):
        """
        Connect to the database.
        """
        if not self.conn:
            # Connect to the database and return a connection object.
            self.conn = sqlite3.connect(db_name)
            # Allow the use of column names when accessing the result sets.
            self.conn.row_factory = sqlite3.Row
        
    def close_db(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
    
    def make_collection(self, row):
        """
        Create a collection object using a row from a result set.
        """
        return Collection(row['coll_id'], row['coll_name'])
        
    def make_item(self, row):
        """
        Create an item object using a row from a result set.
        """
        return Item(row['item_id'], row['item_name'], self.make_collection(row))
        
    def get_collections(self):
        """
        Return a list of collection objects.
        """
        query = '''SELECT coll_id, coll_name FROM collection'''
        with closing(self.conn.cursor) as c:
            c.execute(query)
            results = c.fetchall()
            
        collection = []
        # loop over each row in the result set.
        for row in results:
            # Append a collection object.
            collection.append(self.make_collection(row))
        return collection
        
    def get_items(self, collection_name):
        """
        Return a list of item objects.
        """
        query = '''SELECT coll_id, coll_name from collections WHERE coll_name=?'''
        with closing(self.conn.cursor) as c:
            c.execute(query, (collection_name))
            row = c.fetchone()
        collection = self.make_collection(row)
            
        query = '''SELECT item_id, item_name, coll_id FROM items WHERE coll_id=?'''
        with closing(self.conn.cursor) as c:
            c.execute(query, (collection.coll_id,))
            results = c.fetchall()
            
        items = []
        for row in results:
            items.append(self.make_item(row))
        return items