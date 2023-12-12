import pytest
import subsystem
import random
from ctre import TalonFX, ControlMode

subsystem = subsystem.Drivetrain()

# Monkey patched TalonFX class
class MockTalonFX(TalonFX):
    def __init__(self, talon: TalonFX):
        super().__init__(talon.getDeviceID())
        self._motor_output_percent = 0
        self._selected_sensor_velocity = 0

    def getMotorOutputPercent(self):
        return self._motor_output_percent
    
    def set(self, mode, value):
        if mode == ControlMode.PercentOutput:
            self._motor_output_percent = value
        elif mode == ControlMode.Velocity:
            self._selected_sensor_velocity = value

    def getSelectedSensorVelocity(self):
        return self._selected_sensor_velocity
    
# Intialize mock talons
subsystem.left_motor = MockTalonFX(subsystem.left_motor)
subsystem.left_motor_mirror = MockTalonFX(subsystem.left_motor_mirror)
subsystem.right_motor = MockTalonFX(subsystem.right_motor)
subsystem.right_motor_mirror = MockTalonFX(subsystem.right_motor_mirror)

# Test motor init class
def test_init():

    subsystem.init()
    
    assert subsystem.left_motor is not None
    assert subsystem.left_motor_mirror is not None
    assert subsystem.right_motor is not None
    assert subsystem.right_motor_mirror is not None

# Test set/get raw output
def test_raw_output():

    num = random.uniform(-1, 1)

    subsystem.set_raw_output(num, True)
    assert subsystem.get_raw_output(True) == num

    subsystem.set_raw_output(num, False)
    assert subsystem.get_raw_output(False) == num

def test_velocity():

    num = random.uniform(0, 6380)

    subsystem.set_velocity(num, True)
    assert round((subsystem.get_velocity(True)), 2) == round(num, 2)

    subsystem.set_velocity(num, False)
    assert round((subsystem.get_velocity(False)), 2) == round(num, 2)
