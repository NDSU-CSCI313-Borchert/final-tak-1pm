'''
import unittest

import test_Board
import test_Player
import test_Stone
import test_Capstone

suiteList = []
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_Board.test_Board))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_Player.test_Player))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_Stone.test_Stone))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_Capstone.test_Capstone))

comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=1).run(comboSuite)
'''
