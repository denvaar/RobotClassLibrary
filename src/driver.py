from masterRobot import MasterRobot
from helperRobot import HelperRobot
from robotMediator import RobotMediator

# Application entry point.
if __name__ == "__main__":
    mediator = RobotMediator()
    master = MasterRobot(mediator)
    helper = HelperRobot(mediator)
    #helper2 = HelperRobot(mediator)
    #helper3 = HelperRobot(mediator)
    
    master.doWork()
    master.getStatus()
    master.doWork()
    master.getStatus()
    master.doWork()
    master.getStatus()
    master.doWork()
    master.getStatus()
    helper.finishWork() 
    master.getStatus()
    helper.finishWork() 
    master.getStatus()
    helper.finishWork() 
    master.getStatus()
    master.finishWork() 
    master.getStatus()


