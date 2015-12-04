
class Robot(object):
    """
    Robot: An interface for various
    types of robots to implement.

    Also known as IRobot (Joke.)
    
    See concrete classes for info
    about each method.
    """
    def doWork(self):
        raise NotImplementedError
    def finishWork(self):
        raise NotImplementedError
    def isRunning(self):
        raise NotImplementedError

