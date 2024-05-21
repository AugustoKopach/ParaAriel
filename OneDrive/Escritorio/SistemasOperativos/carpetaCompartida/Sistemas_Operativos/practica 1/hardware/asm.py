"""
Instructions used by the CPU.
Current implementation is just a string,
but they can be more complex entities if used properly.
"""

INSTRUCTION_IO = 'IO'
INSTRUCTION_CPU = 'CPU'
INSTRUCTION_EXIT = 'EXIT'

class ASM:
    """An utility class to create machine code programs"""
    @classmethod
    def EXIT(self):
        """Return the EXIT instruction"""
        return INSTRUCTION_EXIT

    @classmethod
    def IO(self, times=1):
        """Return as many IO instructions as required"""
        return [INSTRUCTION_IO] * times

    @classmethod
    def CPU(self, times=1):
        """Return as many CPU instructions as required"""
        return [INSTRUCTION_CPU] * times

    @classmethod
    def isEXIT(self, instruction):
        """Answer if the given instruction is the EXIT one"""
        return INSTRUCTION_EXIT == instruction

    @classmethod
    def isIO(self, instruction):
        """Answer if the given instruction is an IO one"""
        return INSTRUCTION_IO == instruction

    @classmethod
    def isCPU(self, instruction):
        """Answer if the given instruction is a CPU one"""
        return INSTRUCTION_CPU == instruction