import config
import constants

from ctre import TalonSRX, ControlMode, FollowerType
from subsystem.config.subsystem_base import Subsystem

class Manipulator(Subsystem):

    left_motor = TalonSRX(config.CAN_IDS_MANIPULATOR['left_motor'])
    right_motor = TalonSRX(config.CAN_IDS_MANIPULATOR['right_motor'])
    
    def __init__(self) -> None:
        super().__init__()

    def init(self) -> None:
        # Invert right motor so its opposite of left value
        self.right_motor.setInverted(True)
        self.right_motor.follow(self.left_motor, FollowerType.PercentOutput)

    def set_raw_output(self, speed: float) -> None:
        self.left_motor.set(ControlMode.PercentOutput, speed)

    def get_raw_output(self) -> float:
        return self.left_motor.getMotorOutputPercent()

    def set_velocity(self, velocity: float) -> None:
        self.left_motor.set(ControlMode.Velocity, velocity * constants.INTAKE_GEAR_RATIO)

    def get_velocity(self) -> float:
        return self.left_motor.getSelectedSensorVelocity()/constants.INTAKE_GEAR_RATIO

    def stop(self) -> None:
        self.left_motor.set(ControlMode.PercentOutput, 0)


        





