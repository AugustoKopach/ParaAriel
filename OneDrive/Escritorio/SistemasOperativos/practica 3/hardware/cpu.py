from utilities.printer import Printer

from hardware.asm import ASM
from hardware.irq import IRQ

class Cpu():
    """Models the hardware"s CPU"""

    def __init__(self, memory, interrupt_vector):
        self._memory = memory
        self._interrupt_vector = interrupt_vector
        # Registries
        self._pc = 0
        self._ir = ASM.NOOP()
        self._halted = False
        # For printing purposes only
        self._lastTick = 0
        self._lastExecuted = ASM.NOOP()

    def halt(self):
        self._halted = True

    def resume(self):
        self._halted = False

    def tick(self, tickNbr):
        """Emulate a tick of the clock, performing the FDE cycle"""
        # If the computer is halted, no tick is performed
        if (self._halted):
            return
        # Remember lat tick for printing purposes
        self._lastTick = tickNbr-1
        # Perform FDE cycle
        self._fetch()
        self._decode()
        self._execute()

    def _fetch(self):
        self._ir =  self._memory.read(self._pc) or ASM.NOOP()
        self._pc = (self._pc + 1) % self._memory.size

    def _decode(self):
        # Current implementation does not do anything at the moment
        pass

    def _execute(self):
        self._lastExecuted = self._ir
        Printer.show("Executing instruction: {instr}".format(instr=ASM._colored_instruction_(self._ir)))
        if ASM.isEXIT(self._ir):
            self._interrupt_vector.handle(IRQ.KILL())

    @property
    def pc(self):
        return self._pc

    @pc.setter
    def pc(self, addr):
        self._pc = addr

    def __repr__(self):
        return Printer.tabulated([
            ["Last tick", self._lastTick],
            ["Last executed", self._lastExecuted],
            ["", ""], # To show an empty line
            ["PC", self._pc],
            ["IR", self._ir]
        ])
