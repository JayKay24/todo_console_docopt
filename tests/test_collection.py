# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:07:22 2017

@author: James Kinyua
"""
import unittest

from classes.collection import Collection

class CollectionTest(unittest.TestCase):
    def setUp(self):
        self.colletion1 = Collection('Avatar')
        
    def test_avatar_collection_has_name(self):
        self.assertEqual(self.colletion1.name, 'Avatar',
                         "Name attribute should be present")
                         
    def test_id_is_none(self):
        self.assertIsNone(self.colletion1.id)
        