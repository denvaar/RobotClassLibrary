import unittest

from src.helperRobot import HelperRobot
from src.robotMediator import RobotMediator
from src.robot import Robot
from src.myExceptions \
    import TooBusyException, NotBusyException

class TestHelperRobot(unittest.TestCase):
    """
    A test case that focuses on the
    HelperRobot class.
    """
    def testInit(self):
        """
        testInit makes assertations about things
        that should happen when a HelperRobot
        is created.
        """
        mediator = RobotMediator()
        helper = HelperRobot(mediator)

        # Is helper an instance of HelperRobot?
        self.assertIsInstance(helper, HelperRobot)
        # Is helper also an instance of Robot?
        self.assertIsInstance(helper, Robot)
        # Robot should not be working on a task yet.
        self.assertFalse(helper.isRunning())
        # helper should have been added to mediator's
        # list of robots.
        self.assertIn(helper, mediator.getRobots())

    def testDoWork(self):
        """
        testDoWork makes assertations about things
        that should happen when a HelperRobot is asked
        to perform a task.
        """
        mediator = RobotMediator()
        helper = HelperRobot(mediator)
        
        # Assign one job.
        try:
            helper.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Try to assign another, but helper
        # should be too busy.
        with self.assertRaises(TooBusyException):
            helper.doWork()
            # Try again -- should still be busy.
            helper.doWork()
        # Tell helper it's finished with the task.
        helper.finishWork()
        # Now assign another job -- should accept.
        try:
            helper.doWork()
        except TooBusyException as e:
            self.fail(e)

    def testFinishWork(self):
        """
        testFinishWork makes assertations about things
        that should happen when a HelperRobot is asked
        to finish a task.
        """
        mediator = RobotMediator()
        helper = HelperRobot(mediator)
       
        # Trying to tell the helper to finish the
        # job when it's not working on anything
        # should result in a NotBusyException.
        with self.assertRaises(NotBusyException):
            helper.finishWork()
            helper.finishWork()
        # But if it's working on a task, it should
        # gracefully finish the task.
        try:
            helper.doWork()
            helper.finishWork()
        except Exception as e:
            self.fail(e)

