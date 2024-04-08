KILL_IRQ = "#KILL"

class IRQ:
    @classmethod
    def KILL(self):
        return IRQ(KILL_IRQ, [])

    def __init__(self, code, arguments = []):
        self._code = code
        self._arguments = arguments

    @property
    def code(self):
        return self._code

    @property
    def arguments(self):
        return self._arguments