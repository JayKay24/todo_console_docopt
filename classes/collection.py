# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:29:08 2017

@author: James Kinyua
"""
class Collection:
    """
    Class used to make a collection object.
    """
    def __init__(self, name, id=None):
        self.id = id
        self.name = name