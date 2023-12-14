import commands2
import ctre
import wpilib
import command
import config
import constants
from robot_systems import Robot
import sensors
import subsystem
import utils
from oi.OI import OI


class _Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()

    def robotInit(self):
        # Initialize Operator Interface
        OI.init()
        OI.map_controls()
        period = .03
        commands2.CommandScheduler.getInstance().setPeriod(period)
        
    def robotPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    # Initialize subsystems

    # Pneumatics

    def teleopInit(self):
        commands2.CommandScheduler.getInstance().schedule(
            command.DriveTrain(Robot.drivetrain).alongWith(
                command.Manipulator(Robot.manipulator)
            )
        )
        # a = ctre.VictorSPX(1)
        # a.set(ctre.ControlMode.PercentOutput, .5)

    def teleopPeriodic(self):
        pass
    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(_Robot)
