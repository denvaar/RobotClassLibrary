from myExceptions import TooBusyException
from mediator import Mediator

class RobotMediator(Mediator):
    """
    RobotMediator: Implements the Mediator interface.
    Acts as a man in the middle that allows multiple
    robots to communicate with each other without 
    knowing any details about each other.
    """
    def __init__(self):
        """
        RobotMediator constructor.
        """
        super(RobotMediator, self).__init__()
        # List of robots that will be able to
        # communicate with each other.
        self._robots = []
    
    def _pollForHelp(self, sender):
        """
        pollForHelp: Request one of the other
        robots to perform a task. This method
        is intended to be protected, ie. only
        for use inside this class library.

        Arguments:
        sender - Robot object - The robot which
            requested help.
        """
        # Loop through the list of robots.
        for robot in self._robots:
            # Make sure that the sender is not
            # assigned to do the work.
            if robot is not sender:
                try:
                    robot.doWork()
                    return
                except TooBusyException:
                    # Try to see if there are any
                    # other helpers available.
                    continue
        # No other robots to help.
        raise TooBusyException
                
    def _notifyFinished(self, sender):
        """
        notifyFinished: Let a robot know that
        it has finished doing the task. This 
        method is intended to be protected. It
        should only be used internal to the lib-
        rary.

        Arguments:
        sender - Robot object - The robot which 
            has just finished the task.
        """
        # Loop through the robots.
        for robot in self._robots:
            # Make sure the robot is not the same
            # one that just sent the message.
            if robot is not sender:
                robot.finishWork()
                # If the master still has queued
                # jobs then the helper's work is
                # not done yet.
                if robot.getQueuedJobs() >= 0:
                    # Back to work, robot helper.
                    sender.doWork()
                # No need to go on.
                return

    def addRobot(self, robot):
        """
        addRobot: Add a robot to the list.

        Arguments:
        robot - Robot object - The robot to add.
        """
        self._robots.append(robot)
    
    def getRobots(self):
        """
        getRobots: Returns the robots that are 
        currently in the list.
        """
        return self._robots
