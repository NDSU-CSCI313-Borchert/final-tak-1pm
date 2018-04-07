import unittest
from capstone import *

class test_Capstone(unittest.TestCase):
    def test_capstone_brown_can_be_created(self):
        capstone = Capstone("brown_capstone")
        self.assertTrue(True)
    
    def test_capstone_beige_can_be_created(self):
        capstone = Capstone("beige_capstone")
        self.assertTrue(True)


