import config

from ctre import TalonFX, ControlMode, FollowerType
from subsystem.config.subsystem_base import Subsystem

class Drivetrain(Subsystem):
    
    def init(self) -> None:
        self.left_motor = TalonFX(config.CAN_IDS_DRIVETRAIN['left_1'])
        self.left_motor_mirror =  TalonFX(config.CAN_IDS_DRIVETRAIN['left_2'])
        self.left_motor_mirror.follow(self.left_motor, FollowerType.PercentOutput)

        self.right_motor = TalonFX(config.CAN_IDS_DRIVETRAIN['right_1'])
        self.right_motor_mirror = TalonFX(config.CAN_IDS_DRIVETRAIN['right_2'])
        self.right_motor_mirror.follow(self.right_motor, FollowerType.PercentOutput)

    def set_raw_output(self, speed: float, is_left: bool) -> None: 
        if is_left:
            self.left_motor.set(ControlMode.PercentOutput, speed)
        else:
            self.right_motor.set(ControlMode.PercentOutput, speed)

    def set_velocity(self, velocity: float, is_left: bool) -> None:
        if is_left:
            self.left_motor.set(ControlMode.Velocity, velocity)
        else:
            self.right_motor.set(ControlMode.Velocity, velocity)

    def get_raw_output(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getMotorOutputPercent()
        else:
            return self.right_motor.getMotorOutputPercent()

    def get_velocity(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getSelectedSensorVelocity()
        else:
            return self.right_motor.getSelectedSensorVelocity()
    
    def stop(self) -> None:
        self.left_motor.set(ControlMode.PercentOutput, 0)
        self.right_motor.set(ControlMode.PercentOutput, 0)