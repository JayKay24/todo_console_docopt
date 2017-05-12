# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:16:03 2017

@author: James Kinyua
"""
import unittest

from test_collection import CollectionTest
from test_item import ItemTest

def suite():
    """
    Return a composite test suite of test cases.
    """
    collection = unittest.makeSuite(CollectionTest)
    item = unittest.makeSuite(ItemTest)
    
    return unittest.TestSuite((collection, item))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
