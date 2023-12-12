import pytest
import subsystem
import random
from ctre import TalonSRX, ControlMode

subsystem = subsystem.Manipulator()

# Monkey patched TalonSRX class
class MockTalonSRX(TalonSRX):
    def __init__(self, talon: TalonSRX):
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
subsystem.left_motor = MockTalonSRX(subsystem.left_motor)
subsystem.right_motor = MockTalonSRX(subsystem.right_motor)

# Test motor init class
def test_init():

    subsystem.init()
    
    assert subsystem.left_motor is not None
    assert subsystem.right_motor is not None


# Test set/get raw output
def test_raw_output():

    num = random.uniform(-1, 1)

    subsystem.set_raw_output(num)
    assert subsystem.get_raw_output() == num


def test_velocity():

    num = random.uniform(0, 6380)

    subsystem.set_velocity(num)
    assert round((subsystem.get_velocity()), 2) == round(num, 2)