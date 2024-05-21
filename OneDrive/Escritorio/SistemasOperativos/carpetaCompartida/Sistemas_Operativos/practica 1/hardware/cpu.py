from utilities.log import logger

class Cpu():
    """Models the hardware's CPU"""

    def __init__(self, memory):
        self._memory = memory
        self._pc = -1
        self._ir = None


    def tick(self, tickNbr):
        """Emulate a tick of the clock, performing the FDE cycle"""
        if (self._pc > -1):
            self._fetch()
            self._decode()
            self._execute()
        else:
            logger.info("cpu - NOOP")

    def _fetch(self):
        self._ir = self._memory.read(self._pc)
        self._pc += 1

    def _decode(self):
        # Current implementation does not do anything at the moment
        pass

    def _execute(self):
        logger.info("cpu - Exec: {instr}, PC={pc}".format(instr=self._ir, pc=self._pc))

    @property
    def pc(self):
        return self._pc

    @pc.setter
    def pc(self, addr):
        self._pc = addr

    def __repr__(self):
        return "CPU(PC={pc})".format(pc=self._pc)