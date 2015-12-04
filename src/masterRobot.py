from robot import Robot
from myExceptions import \
    TooBusyException, NotBusyException

class MasterRobot(Robot):
    """
    MasterRobot: implements the Robot interface
    and represents a robot that can perform one
    task at a time. MasterRobot may or may not
    recruit other robots for help with a task. 
    """
    def __init__(self, mediator=None):
        """
        MasterRobot's __init__ method: constructor
        for MasterRobot class.
        
        Arguments:
        mediator - RobotMediator object - When this 
            argument is supplied, MasterRobot can
            ask other robots for help. It acts as a
            middle man so that each type of robot is
            not tightly coupled to one another.
        """
        super(MasterRobot, self).__init__()
        self._queued = 0 # Number of jobs in queue
        self._running = 0 # Number of running jobs.
        self._mediator = mediator
        if self._mediator:
            self._mediator.addRobot(self)
    
    def isRunning(self):
        """
        isRunning checks returns true when there
        is at least one task running, othrewise
        returns false.
        """
        return self._running > 0

    def doWork(self):
        """
        doWork: Used to assign a new task to the
        MasterRobot.
        """
        if self._running < 1:
            self._running = self._running + 1
        else:
            # Ask for help
            self._getHelp()

    def getStatus(self):
        """
        getStatus: Prints information about
        the robot's tasks.
        """
        print "MasterRobot: %d jobs running. %d jobs queued."\
            % (self._running, self._queued)
    
    def getRunningJobs(self):
        """
        getRunningJobs: A getter for the number
        of currently running jobs/tasks.
        """
        return self._running

    def getQueuedJobs(self):
        """
        getQueuedJobs: A getter for the number
        of jobs/tasks in the queue.
        """
        return self._queued

    def finishWork(self):
        """
        finishWork: Finishes a task.
        """
        # Decide which type of task was finished.
        if self._queued > 0:
            self._queued = self._queued - 1
        elif self._running > 0:
            self._running = self._running - 1
        else:
            raise NotBusyException

    def _getHelp(self):
        """
        getHelp: Tries to ask a helper
        robot for help with a task.
        """
        try:
            self._mediator._pollForHelp(self)
            self._running = self._running + 1
        except Exception:
            self._queued = self._queued + 1

