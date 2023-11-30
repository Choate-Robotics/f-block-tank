from typing import Generic, TypeVar
import commands2

class Subsystem(commands2.SubsystemBase):
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
