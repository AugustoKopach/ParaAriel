class Process:
    def __init__(self,pid, memory_start, memory_end):
        self._pid = pid
        self.state = CREATED
        self.memory_start = memory_start
        self.memory_end = memory_end
        self.registers_cpu = {}

    def change_state(self, new_state):
        self.state = new_state

    