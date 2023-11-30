import config

from ctre import TalonFX, ControlMode
from subsystem.config.subsystem_base import Subsystem

class Drivetrain(Subsystem):
    
    left_motor_1 = TalonFX(config.CAN_IDS_DRIVETRAIN['left_1'])
    right_motor_1 = TalonFX(config.CAN_IDS_DRIVETRAIN['right_1'])
    left_motor_2 = TalonFX(config.CAN_IDS_DRIVETRAIN['left_2'])
    right_motor_2 = TalonFX(config.CAN_IDS_DRIVETRAIN['right_2'])

    def set_raw_output(self, speed: float, is_left: bool) -> None: 
        if is_left: 
            self.left_motor_1.set(ControlMode.PercentOutput, speed)
            self.left_motor_2.set(ControlMode.PercentOutput, speed)
        else:
            self.right_motor_1.set(ControlMode.PercentOutput, speed)
            self.right_motor_2.set(ControlMode.PercentOutput, speed)

    def set_velocity(self, velocity: float, is_left: bool) -> None:
        if is_left:
            self.left_motor_1.set(ControlMode.Velocity, velocity)
            self.left_motor_2.set(ControlMode.Velocity, velocity)
        else:
            self.right_motor_1.set(ControlMode.Velocity, velocity)
            self.right_motor_2.set(ControlMode.Velocity, velocity)


    def get_raw_output(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor_1.getMotorOutputPercent()
        else:
            return self.right_motor_1.getMotorOutputPercent()
        
    def get_velocity(self, is_left: bool) -> float:
        if is_left:
            return self.left_motor_1.getSelectedSensorVelocity()
        else:
            return self.right_motor_1.getSelectedSensorVelocity()
    
    def stop(self) -> None:
        self.right_motor_1.set(0)
        self.right_motor_2.set(0)
        self.left_motor_1.set(0)
        self.left_motor_2.set(0)