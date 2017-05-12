# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:36:21 2017

@author: James Kinyua
"""
from . import Collection, Item
from .. import TodoDB

class Todo:
    """
    Controller class in the application todo list.
    """
    def __init__(self):
        self.db = TodoDB()
        
    def create_collection(self, name):
        """
        Create a new collection of items.
        """
        collection = Collection(name)
        self.db.add_collection(collection)
        