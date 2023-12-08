from ctre import TalonSRX, ControlMode
from subsystem.config.subsystem_base import Subsystem
import config
import constants

class Manipulator(Subsystem):

    left_motor = TalonSRX(config.CAN_IDS_MANIPULATOR['left_motor'])
    right_motor = TalonSRX(config.CAN_IDS_MANIPULATOR['right_motor'])
    
    def __init__(self) -> None:
        super().__init__()

    def set_raw_output(self, speed: float, isLeft: bool) -> None:
        if isLeft:
            self.left_motor.set(ControlMode.PercentOutput, speed)
        else:
            self.right_motor.set(ControlMode.PercentOutput, speed)

    def get_raw_output(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getMotorOutputPercent()
        else:
            return self.right_motor.getMotorOutputPercent()

    def set_velocity(self, velocity: float, is_left: bool) -> None:
        if is_left:
            self.left_motor.set(ControlMode.Velocity, velocity * constants.intake_gear_ratio)
        else:
            self.right_motor.set(ControlMode.Velocity, velocity * constants.intake_gear_ratio)

    def get_velocity(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getSelectedSensorVelocity()/constants.intake_gear_ratio
        else:
            return self.right_motor.getSelectedSensorVelocity()/constants.intake_gear_ratio

    def stop(self) -> None:
        self.left_motor.set(ControlMode.PercentOutput, 0)
        self.right_motor.set(ControlMode.PercentOutput, 0)


        





