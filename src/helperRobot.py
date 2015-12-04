from robot import Robot
from myExceptions \
    import TooBusyException, NotBusyException

class HelperRobot(Robot):
    """
    HelperRobot: A type of robot whose lot
    in life is to help out other robots.
    HelperRobot implements the Robot interface
    """
    def __init__(self, mediator):
        """
        HelperRobot's __init__ method: constructor.

        Arguments:
        mediator - RobotMediator object - It acts 
            as a middle man so that each type of
            robot is not tightly coupled to one
            another.
        """
        super(HelperRobot, self).__init__()
        # RobotHelper is either running or it's not.
        self._running = False
        self._mediator = mediator
        self._mediator.addRobot(self)
    
    def isRunning(self):
        """
        isRunning: a Getter for private _running 
        attribute to determine if it's running.
        """
        return self._running

    def doWork(self):
        """
        doWork: Used to assign a new task to the
        HelperRobot.
        """
        if not self._running:
            self._running = True
        else:
            # Raise an exception if already running.
            raise TooBusyException

    def finishWork(self):
        """
        finishWork: finishes a task.
        """
        # If this robot is running then
        # that means it's helping another
        # robot.
        if self._running:
            # Set to not running anymore.
            self._running = False
            # Notify the other robot that it's
            # finished.
            self._mediator._notifyFinished(self)
        else:
            raise NotBusyException
