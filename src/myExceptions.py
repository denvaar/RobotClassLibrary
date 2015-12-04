
class TooBusyException(Exception):
    """
    An exception that should be raised
    when a robot is too busy to take on
    more work.
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class NotBusyException(Exception):
    """
    An exception that should be raised
    when a robot is asked to finish a 
    task, but is not working on one.
    """
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

