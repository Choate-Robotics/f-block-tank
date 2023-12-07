from subsystem.config.subsystem_base import SubsystemCommand
from subsystem import Drivetrain
class DriveTrain(SubsystemCommand[Drivetrain]):

    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem
    
    def initialize(self) -> None:
        self.subsystem.init()

    def execute(self) -> None:
        ...

    def isFinished(self) -> bool:
        return False
    
    def end(self) -> None:
        self.subsystem.stop()
