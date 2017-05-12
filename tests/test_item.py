# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:33:27 2017

@author: James Kinyua
"""
import unittest
import sys

# Add top_level directory room_allocator to sys.path
sys.path.append('../')

from classes.collection import Collection
from classes.item import Item

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.collection1 = Collection('Avatar')
        self.item1 = Item('Aang')
        
    def test_item1_has_name(self):
        self.assertEqual(self.item1.name, 'Aang',
                         'Item name attribute should not be none')
                         
    def test_item1_has_collection_object(self):
        self.item1.collection = self.collection1
        self.assertIsInstance(self.item1.collection, Collection)
        
    def test_item1_id_is_none(self):
        self.assertIsNone(self.item1.id)
        
