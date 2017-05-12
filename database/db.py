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
    
    def _make_collection(self, row):
        """
        Create a collection object using a row from a result set.
        """
        return Collection(row['coll_id'], row['coll_name'])
        
    def _make_item(self, row):
        """
        Create an item object using a row from a result set.
        """
        return Item(row['item_id'], row['item_name'], self._make_collection(row))
        
    def get_collections(self):
        """
        Return a list of collection objects.
        """
        query = '''SELECT coll_id, coll_name FROM collections'''
        with closing(self.conn.cursor) as c:
            c.execute(query)
            results = c.fetchall()
            
        collections = []
        # loop over each row in the result set.
        for row in results:
            # Append a collection object.
            collections.append(self._make_collection(row))
        return collections
        
    def get_collection(self, name):
        """
        Return a single collection object.
        """
        query = '''SELECT coll_id, coll_name FROM collections 
                WHERE coll_name=?'''
        with closing(self.conn.cursor()) as c:
            c.execute(query, (name,))
            row = c.fetchone()
        collection = self.make_collection(row)
        return collection
        
    def get_items(self, collection):
        """
        Return a list of item objects.
        """
        query = '''SELECT item_id, item_name, coll_id FROM items 
                WHERE coll_id=?'''
        with closing(self.conn.cursor) as c:
            c.execute(query, (collection.coll_id,))
            results = c.fetchall()
            
        items = []
        for row in results:
            items.append(self._make_item(row))
        return items
        
    def get_item(self, collection, name):
        """
        Return a single item object.
        """
        query = '''SELECT item_id, item_name, coll_id FROM items
                WHERE coll_id=?'''
        with closing(self.conn.cursor()) as c:
            c.execute(query, (collection.id,))
            row = c.fetchone()
        item = self.make_item(row)
        return item
        
    def add_collection(self, collection):
        """
        Add a collection into the database.
        """
        sql = '''INSERT INTO collections (coll_name) VALUES(?)'''
        with closing(self.conn.cursor()) as c:
            c.execute(sql, (collection.name,))
            self.conn.commit()
            print("Collection", collection.name, "was successfully created!")
            
    def add_item(self, item):
        """
        Add an item into the database.
        """
        sql = '''INSERT INTO items (item_name, coll_id) VALUES(?, ?)'''
        with closing(self.conn.cursor()) as c:
            c.execute(sql, (item.name, item.collection.id))
            self.conn.commit()
            print("Item", item.name, "was successfully added!")
            
    def delete_item(self, item):
        """
        Delete an item from a collection.
        """
        sql = '''DELETE FROM items WHERE item_id=?'''
        with closing(self.conn.cursor()) as c:
            c.execute(sql, (item.id,))
            self.conn.commit()
            print(item.name, "was successfully deleted.")
        