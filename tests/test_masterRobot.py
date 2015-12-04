import unittest

from src.helperRobot import HelperRobot
from src.masterRobot import MasterRobot
from src.robotMediator import RobotMediator
from src.robot import Robot
from src.myExceptions \
    import TooBusyException, NotBusyException

class TestMasterRobot(unittest.TestCase):
    """
    A test case that focuses on the
    MasterRobot class.
    """
    def testInit(self):
        """
        testInit makes assertations about things
        that should happen when a MasterRobot
        is created.
        """
        mediator = RobotMediator()
        helper = HelperRobot(mediator)
        master = MasterRobot(mediator)

        # Is helper an instance of MasterRobot?
        self.assertIsInstance(master, MasterRobot)
        # Is helper also an instance of Robot?
        self.assertIsInstance(master, Robot)
        # Robot should not be working on a task yet.
        self.assertFalse(master.isRunning())
        # master should have been added to mediator's
        # list of robots.
        self.assertIn(master, mediator.getRobots())
        # helper should have been added to mediator's
        # list of robots too.
        self.assertIn(helper, mediator.getRobots())
        # Master can also be alone without any helpers.
        masterAlone = MasterRobot()
        self.assertNotIn(masterAlone,
            mediator.getRobots())
        
    def testDoWorkA(self):
        """
        testDoWork makes assertations about things
        that should happen when a MasterRobot is asked
        to perform a task.
        """
        # -------------------------- #
        # 1 master and 1 helper      #
        # -------------------------- #
        mediator = RobotMediator()
        helper = HelperRobot(mediator)
        master = MasterRobot(mediator)
    
        # Assign one job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 1 running 0 queued.
        self.assertEquals(1, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Assign second job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 0 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

        # Assign third job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 1 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(1, master.getQueuedJobs())

        # Assign fourth job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 2 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(2, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            helper.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 1 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(1, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            helper.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 0 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        

        # Tell the helper that it's finished doing
        # its job.
        try:
            helper.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 1 running 0 queued.
        self.assertEquals(1, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 0 running 0 queued.
        self.assertEquals(0, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

    def testDoWorkB(self):
        """
        testDoWork makes assertations about things
        that should happen when a MasterRobot is asked
        to perform a task.
        """
        # -------------------------- #
        # 1 master and 2 helpers     #
        # -------------------------- #
        mediator = RobotMediator()
        helper1 = HelperRobot(mediator)
        helper2 = HelperRobot(mediator)
        master = MasterRobot(mediator)
    
        # Assign one job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 1 running 0 queued.
        self.assertEquals(1, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Assign second job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 0 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

        # Assign third job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 3 running 0 queued.
        self.assertEquals(3, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

        # Assign fourth job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 3 running 1 queued.
        self.assertEquals(3, master.getRunningJobs())
        self.assertEquals(1, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 3 running 0 queued.
        self.assertEquals(3, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 0 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        

        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 1 running 0 queued.
        self.assertEquals(1, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 0 running 0 queued.
        self.assertEquals(0, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

    def testDoWorkC(self):
        """
        testDoWork makes assertations about things
        that should happen when a MasterRobot is asked
        to perform a task.
        """
        # -------------------------- #
        # 1 master and 3 helpers     #
        # -------------------------- #
        mediator = RobotMediator()
        helper1 = HelperRobot(mediator)
        helper2 = HelperRobot(mediator)
        helper3 = HelperRobot(mediator)
        master = MasterRobot(mediator)
    
        # Assign one job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 1 running 0 queued.
        self.assertEquals(1, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Assign second job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 0 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

        # Assign third job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 3 running 0 queued.
        self.assertEquals(3, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

        # Assign fourth job.
        try:
            master.doWork()
        except TooBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 4 running 0 queued.
        self.assertEquals(4, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 3 running 0 queued.
        self.assertEquals(3, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 2 running 0 queued.
        self.assertEquals(2, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        

        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 1 running 0 queued.
        self.assertEquals(1, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())
        
        # Tell the helper that it's finished doing
        # its job.
        try:
            master.finishWork()
        except NotBusyException as e:
            self.fail(e)
        # Verify the status.
        # Should be 0 running 0 queued.
        self.assertEquals(0, master.getRunningJobs())
        self.assertEquals(0, master.getQueuedJobs())

    def testFinishWork(self):
        """ 
        testFinishWork makes assertations about things
        that should happen when a HelperRobot is asked
        to finish a task.
        """
        mediator = RobotMediator()
        helper = HelperRobot(mediator)
        master = MasterRobot(mediator)

        # Try telling master to finish job without
        # assigning any work.
        with self.assertRaises(NotBusyException):
            master.finishWork()
            master.finishWork()
        
        # But if it's working on a task, it should
        # gracefully finish the task.
        try:
            master.doWork()
            master.finishWork()
        except Exception as e:
            self.fail(e)  
      
