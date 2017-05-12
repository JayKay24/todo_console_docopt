# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:36:21 2017

@author: James Kinyua
"""
from classes.collection import Collection
from classes.item import Item
from database.db import TodoDB

class Todo:
    """
    Controller class in the application todo list.
    """
    def __init__(self):
        self.db = TodoDB()
        self.current_collection = None
        self.current_item = None
        
    def add_a_collection(self, name):
        """
        Create a new collection of items.
        """
        collection = Collection(name)
        self.db.add_collection(collection)
        
    def open_collection(self, name):
        """
        Set aside a collection to add items.
        """
        self.current_collection = self.db.get_collection(name)
        print(self.current_collection.name, "has been opened.")
    
    def add_an_item(self, name):
        """
        Add an item to a collection.
        """
        if self.current_collection is not None:
            item = Item(name, collection=self.current_collection)
            self.db.add_item(item)
        
    def show_items(self):
        """
        Display all the items in a collection.
        """
        if self.current_collection is not None:
            items = self.db.get_items(self.current_collection)
            for item in items:
                print(item.name)
                
    def show_collections(self):
        """
        Display all the collections in the database.
        """
        collections = self.db.get_collections()
        for collection in collections:
            print(collection.name)
            
    def delete_an_item(self, name):
        """
        Delete an item from a collection.
        """
        if self.current_collection is not None:
            item = self.db.get_item(self.current_collection, name)
            self.db.delete_item(item)
            
    def delete_a_collection(self, name):
        """
        Delete an entire collection of items.
        """
        self.current_collection = None
        collection = Collection(name)
        self.db.delete_collection(collection)