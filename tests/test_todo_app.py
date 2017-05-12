# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:16:03 2017

@author: James Kinyua
"""
import unittest

from test_collection import CollectionTest

def suite():
    """
    Return a composite test suite of test cases.
    """
    collection = unittest.makeSuite(CollectionTest)
    
    return unittest.TestSuite((collection,))
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
