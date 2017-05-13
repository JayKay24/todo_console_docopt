# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:07:22 2017

@author: James Kinyua
"""
import sys
import unittest

# Add classes directory to sys.path to load it into the Python Environment.
sys.path.append('../classes')

from collection import Collection

class CollectionTest(unittest.TestCase):
    def setUp(self):
        self.colletion1 = Collection('Avatar')
        
    def test_collection1_has_name(self):
        self.assertEqual(self.colletion1.name, 'Avatar',
                         "Name attribute should be present")
                         
    def test_id_is_none(self):
        self.assertIsNone(self.colletion1.id)
        