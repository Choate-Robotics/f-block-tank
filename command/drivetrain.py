from subsystem.config.subsystem_base import SubsystemCommand
from subsystem import Drivetrain

from oi.keymap import Keymap

class DriveTrain(SubsystemCommand[Drivetrain]):

    def __init__(self, subsystem: Drivetrain):
        super().__init__(subsystem)
        self.subsystem = subsystem
    
    def initialize(self) -> None:
        ...

    def execute(self) -> None:
        left = Keymap.Drivetrain.DRIVE_X_AXIS.value
        right = Keymap.Drivetrain.DRIVE_Y_AXIS.value

        self.subsystem.set_raw_output(left, True)
        self.subsystem.set_raw_output(right, False)

    def isFinished(self) -> bool:
        return False
    
    def end(self) -> None:
        self.subsystem.stop()
