import config

from ctre import TalonFX, ControlMode
from subsystem.config.subsystem_base import Subsystem

class Drivetrain(Subsystem):
    
    def init(self) -> None:
        self.left_motors = [TalonFX(config.CAN_IDS_DRIVETRAIN['left_1']), TalonFX(config.CAN_IDS_DRIVETRAIN['left_2'])]
        self.right_motors = [TalonFX(config.CAN_IDS_DRIVETRAIN['right_1']), TalonFX(config.CAN_IDS_DRIVETRAIN['right_2'])]

    def set_raw_output(self, speed: float, is_left: bool) -> None: 
        for motor in (self.left_motors if is_left else self.right_motors):
            motor.set(ControlMode.PercentOutput, speed)

    def set_velocity(self, velocity: float, is_left: bool) -> None:
        for motor in (self.left_motors if is_left else self.right_motors):
            motor.set(ControlMode.Velocity, velocity)

    def get_raw_output(self, is_left: bool) -> float:
        for motor in (self.left_motors if is_left else self.right_motors):
            return motor.getMotorOutputPercent()

        
    def get_velocity(self, is_left: bool) -> float:
        for motor in (self.left_motors if is_left else self.right_motors):
            return motor.getSelectedSensorVelocity()
    
    def stop(self) -> None:
        for motor in self.left_motors + self.right_motors:
            motor.set(ControlMode.PercentOutput, 0)