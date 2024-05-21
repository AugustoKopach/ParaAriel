from hardware.hardware import HARDWARE

class LongTermScheduler:
    def __init__(self, kernel, process_table):
        self._kernel = kernel
        self._process_table = process_table
        self._next_pid = 1

    def create_process(self, program):
        memory_location = self.allocate_program_in_memory(program)
        self._create_pcb(program, memory_location)
        pid = self._increase_next_pid()
        return memory_location, memory_location + len(program.instructions) - 1
        
    def allocate_program_in_memory(self, program):
        if self._kernel.has_free_memory(len(program.instructions)):
            return self._kernel.allocate(program.instructions)
        else:
            raise Exception("No hay suficiente memoria disponible")

    def _create_pcb(self, program, memory_location):
        pid = self._next_pid
        self._next_pid += 1
        pcb = {
            "pid": pid,
            "program_name": program.name,
            "memory_location": memory_location,
            "state": "ready"
        }
        self._process_table[pid] = pcb

    def _increase_next_pid(self):
        self._next_pid += 1