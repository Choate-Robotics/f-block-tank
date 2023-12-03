from typing import Generic, TypeVar
import commands2
import wpiutil._wpiutil

class SubsystemBase(commands2.Subsystem, wpiutil._wpiutil.Sendable):
    """
    A base for subsystems that handles registration in the constructor, and
    provides a more intuitive method for setting the default command.
    """
    def __init__(self) -> None: ...
    def addChild(self, name: str, child: wpiutil._wpiutil.Sendable) -> None: 
        """
        Associate a Sendable with this Subsystem.
        Also update the child's name.

        :param name:  name to give child
        :param child: sendable
        """
    def getName(self) -> str: 
        """
        Gets the name of this Subsystem.

        :returns: Name
        """
    def getSubsystem(self) -> str: 
        """
        Gets the subsystem name of this Subsystem.

        :returns: Subsystem name
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    def setName(self, name: str) -> None: 
        """
        Sets the name of this Subsystem.

        :param name: name
        """
    def setSubsystem(self, name: str) -> None: 
        """
        Sets the subsystem name of this Subsystem.

        :param name: subsystem name
        """
    pass

class Subsystem(SubsystemBase):
    """
    Extendable subsystem
    """
    ...

T = TypeVar("T", bound=Subsystem)

class BasicCommand(commands2.CommandBase):
    """
    Extendable basic command
    """
    ...


class SubsystemCommand(BasicCommand, Generic[T]):
    """
    Extendable subsystem command
    """

    def __init__(self, subsystem: T):
        super().__init__()
        self.subsystem = subsystem
        self.addRequirements(subsystem)
