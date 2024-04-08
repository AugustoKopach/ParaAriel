class Process:
    def __init__(self, process_id, memory_start, memory_end):
        self.id = process_id
        self.state = "ready"
        self.memory_start = memory_start
        self.memory_end = memory_end
        self.registers_cpu = {}

    def change_state(self, new_state):
        self.state = new_state

    def getId(self):
        return self.id