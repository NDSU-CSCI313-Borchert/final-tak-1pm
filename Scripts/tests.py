import unittest

import test_Board
import test_Player

suiteList = []
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_Board.test_Board))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_Player.test_Player))

comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=0).run(comboSuite)
