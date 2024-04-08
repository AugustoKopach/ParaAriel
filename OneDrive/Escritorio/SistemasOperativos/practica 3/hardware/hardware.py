from hardware.memory import Memory
from hardware.cpu import Cpu
from hardware.clock import Clock
from hardware.interrupt_vector import InterruptVector

class Hardware():
    """
    Represents a full computer hardware, the "motherboard" along with the
    other components wired in, if you may.
    """

    def setup(self, memorySize = 20, clockSpeed = 1):
        self._memory = Memory(memorySize)
        self._interrupt_vector = InterruptVector()
        self._cpu = Cpu(self._memory, self._interrupt_vector)
        self._clock = Clock(clockSpeed)
        self._clock.addSubscriber(self._cpu)

    @property
    def cpu(self):
        return self._cpu

    @property
    def memory(self):
        return self._memory

    @property
    def interrupt_vector(self):
        return self._interrupt_vector

    @property
    def clock(self):
        return self._clock

    def turnOn(self):
        self._clock.start()
        self._cpu.resume()

    def turnOff(self):
        self._clock.stop()
        self._cpu.halt()

    def __repr__(self):
        return "{cpu}\n{mem}".format(cpu=self._cpu, mem=self._memory)


"""An instance of the hardware that acts as a global variable
being accessible from anywhere"""
HARDWARE = Hardware()