import unittest

from tests.test_helperRobot import TestHelperRobot
from tests.test_masterRobot import TestMasterRobot
from tests.test_robotMediator import TestRobotMediator

testClasses = [TestHelperRobot,
               TestMasterRobot,
               TestRobotMediator]
loader = unittest.TestLoader()
suiteList = []

for test in testClasses:
    suite = loader.loadTestsFromTestCase(test)
    suiteList.append(suite)

bigSuite = unittest.TestSuite(suiteList)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(bigSuite)

