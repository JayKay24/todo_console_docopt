# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:33:33 2017

@author: James Kinyua
"""
class Item:
    def __init__(self, name, id=None, collection=None):
        self.id = id
        self.name = name
        self.collection = collection
