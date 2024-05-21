from hardware.memory import Memory
from hardware.cpu import Cpu

class Hardware():
    """
    Represents a full computer hardware, the 'motherboard' along with the
    other components wired in, if you may.
    """

    def setup(self, memorySize):
        self._memory = Memory(memorySize)
        self._cpu = Cpu(self._memory)

    @property
    def cpu(self):
        return self._cpu

    @property
    def memory(self):
        return self._memory

    def __repr__(self):
        return "HARDWARE state {cpu}\n{mem}".format(cpu=self._cpu, mem=self._memory)


"""An instance of the hardware that acts as a global variable
being accessible from anywhere"""
HARDWARE = Hardware()