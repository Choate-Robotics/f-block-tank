import config, constants

from ctre import TalonFX, ControlMode, FollowerType
from subsystem.config.subsystem_base import Subsystem

# Drivetrain subsystem
class Drivetrain(Subsystem):

    # Initialize motors pre-init, DONT MOVE INSIDE INIT OR TESTS CRASH
    left_motor = TalonFX(config.CAN_IDS_DRIVETRAIN['left_1'])
    right_motor = TalonFX(config.CAN_IDS_DRIVETRAIN['right_1'])
    left_motor_mirror =  TalonFX(config.CAN_IDS_DRIVETRAIN['left_2'])
    right_motor_mirror = TalonFX(config.CAN_IDS_DRIVETRAIN['right_2'])

    # Initialize subclass (from commands2)
    def __init__(self) -> None:
        super().__init__()
    
    # Mirror other left/right motor
    def init(self) -> None:
        self.left_motor_mirror.follow(self.left_motor, FollowerType.PercentOutput)
        self.right_motor_mirror.follow(self.right_motor, FollowerType.PercentOutput)

    def set_raw_output(self, speed: float, is_left: bool) -> None: 
        if is_left:
            self.left_motor.set(ControlMode.PercentOutput, speed)
        else:
            self.right_motor.set(ControlMode.PercentOutput, speed)

    def set_velocity(self, velocity: float, is_left: bool) -> None:
        if is_left:
            self.left_motor.set(ControlMode.Velocity, velocity * constants.DRIVETRAIN_GEAR_RATIO)
        else:
            self.right_motor.set(ControlMode.Velocity, velocity * constants.DRIVETRAIN_GEAR_RATIO)

    def get_raw_output(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getMotorOutputPercent()
        else:
            return self.right_motor.getMotorOutputPercent()

    def get_velocity(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor.getSelectedSensorVelocity()/constants.DRIVETRAIN_GEAR_RATIO
        else:
            return self.right_motor.getSelectedSensorVelocity()/constants.DRIVETRAIN_GEAR_RATIO
    
    def stop(self) -> None:
        self.left_motor.set(ControlMode.PercentOutput, 0)
        self.right_motor.set(ControlMode.PercentOutput, 0)