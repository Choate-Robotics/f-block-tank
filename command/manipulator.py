from subsystem.config.subsystem_base import SubsystemCommand
from subsystem import Manipulator

from oi.keymap import Keymap

class Manipulator(SubsystemCommand[Manipulator]):

    def __init__(self, subsystem: Manipulator):
        super().__init__(subsystem)
        self.subsystem = subsystem
    
    def initialize(self) -> None:
        ...

    def execute(self) -> None:
        run_in = Keymap.Manipulator.RUN_IN.value
        run_out = Keymap.Manipulator.RUN_OUT.value

        if run_in > 0:
            # Forward
            self.subsystem.set_raw_output(run_in)
        else:
            # Reverse
            self.subsystem.set_raw_output(-run_out)

    def isFinished(self) -> bool:
        return False
    
    def end(self, interrupted) -> None:
        pass
