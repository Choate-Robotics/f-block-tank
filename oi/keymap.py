import commands2
import wpilib

from robotpy_toolkit_7407.oi import (
    XBoxController,
    LogitechController,
    JoystickAxis,
    DefaultButton,
)

from robotpy_toolkit_7407.oi.joysticks import Joysticks

controllerDRIVER = XBoxController
controllerOPERATOR = XBoxController
controllerNUMPAD = XBoxController


class Controllers:
    DRIVER = 0
    OPERATOR = 1
    NUMPAD = 2

    DRIVER_CONTROLLER = wpilib.Joystick(0)
    OPERATOR_CONTROLLER = wpilib.Joystick(1)
    NUMPAD_CONTROLLER = wpilib.Joystick(2)


class Keymap:
    class Drivetrain:
        DRIVE_X_AXIS = JoystickAxis(Controllers.DRIVER, controllerDRIVER.L_JOY[1])
        DRIVE_Y_AXIS = JoystickAxis(Controllers.DRIVER, controllerDRIVER.R_JOY[1])
        DRIVE_ROTATION_AXIS = JoystickAxis(
            Controllers.DRIVER, controllerDRIVER.R_JOY[0]
        )
        # RESET_GYRO = commands2.Trigger(
        #     Joysticks.joysticks[Controllers.DRIVER], controllerDRIVER.B
        # )
        # RESET_ODOMETRY = commands2.Trigger(
        #     Joysticks.joysticks[Controllers.DRIVER], controllerDRIVER.Y
        # )
        # SLOW_FORWARD = commands2.Trigger(
        #     lambda: Controllers.DRIVER_CONTROLLER.getRawAxis(-controllerDRIVER.RT) > 0.5
        # )
        # X_MODE = commands2.Trigger(
        #     Joysticks.joysticks[Controllers.DRIVER], controllerDRIVER.X
        # )
        # AUTO_ROUTE = commands2.Trigger(
        #     lambda: Controllers.DRIVER_CONTROLLER.getRawAxis(-controllerDRIVER.LT) > 0.5
        # )
    class Manipulator:
        RUN_IN = JoystickAxis(Controllers.DRIVER, 3)
        RUN_OUT = JoystickAxis(Controllers.DRIVER, 2)
