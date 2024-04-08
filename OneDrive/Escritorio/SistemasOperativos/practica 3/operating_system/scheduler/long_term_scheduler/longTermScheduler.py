from hardware.hardware import HARDWARE
from operating_system.process import Process
class LongTermScheduler:
    def __init__(self, kernel, process_table):
        self._kernel = kernel
        self._process_table = process_table
        self._next_pid = 1
        

    def create_process(self, program):
        memory_location = self.allocate_program_in_memory(program)
        self._create_pcb(program, memory_location)
        pid = self._next_pid
        self._increase_next_pid()
        print("ID del proceso:", pid)
        return pid

    def kill_process(self, id):
        pcb = self._process_table[id]
        self.deallocate_program_in_memory(pcb)
        self.delete_pcb(pcb)

    def deallocate_program_in_memory(self, pcb):
        for pos in range(pcb.memory_start, pcb.memory_end + 1):
            self._kernel.free(pos)
    
    def delete_pcb(self, pcb):
        del self._process_table[pcb.id]

    def allocate_program_in_memory(self, program):
        if self._kernel.has_free_memory(len(program.instructions)):
            return self._kernel.allocate(program.instructions)
        else:
            raise Exception("No hay suficiente memoria disponible")
    
    def _create_pcb(self, program, memory_location):
        pid = self._next_pid
        process = Process(pid, memory_location, memory_location + len(program.instructions) - 1)
        self._process_table [pid] = process
       
    def _increase_next_pid(self):
        self._next_pid += 1
