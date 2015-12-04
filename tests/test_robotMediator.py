import unittest

from src.robotMediator import RobotMediator
from src.mediator import Mediator
from src.helperRobot import HelperRobot
from src.masterRobot import MasterRobot
from src.myExceptions import \
    TooBusyException, NotBusyException

class TestRobotMediator(unittest.TestCase):
    """
    A test case for the robot mediator class.
    The robot mediator's purpose is to allow
    a group of robots to communicate with 
    each other through the mediator design
    pattern.
    """
    def testInit(self):
        """
        Test the initialization of a robotMediator.
        """
        # Create a mediator object
        try:
            mediator = RobotMediator()
        except Exception as e:
            self.fail(e)
        # mediator should be an instance of
        # the RobotMediator class.
        self.assertIsInstance(mediator, RobotMediator)
        # It should also be an instance of the 
        # Mediator interface.
        self.assertIsInstance(mediator, Mediator)

        # RobotMediator should have an empty list.
        self.assertEquals([], mediator.getRobots())


