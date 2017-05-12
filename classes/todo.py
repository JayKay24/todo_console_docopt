# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:36:21 2017

@author: James Kinyua
"""
from . import Collection, Item
from .. import TodoDB

class Todo:
    def __init__(self):
        self.db = TodoDB()
        
    def create_collection():