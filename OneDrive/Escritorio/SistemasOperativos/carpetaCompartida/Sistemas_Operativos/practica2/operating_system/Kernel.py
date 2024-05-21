from hardware.hardware import HARDWARE
from operating_system.process import Process  
from operating_system.scheduler.long_term.longTermScheduler import LongTermScheduler  

class kernel:
    def __init__(self):
        self._processes_table = {}
        self._longTermScheduler = LongTermScheduler(self, self._processes_table)
        self._last_allocation_position = 0

    def create_process(self, program):
        return self._longTermScheduler.create_process(program)

    # def kill_process(self, pid):
    #     if(pid in self._processes_table):
    #         del self._processes_table[pid]
    #         print("Process killed")
    #     else:
    #         print("Error! Process with id ", str(pid), " doesn't exist.")

    def has_free_memory(self, size):
        return HARDWARE.memory.size - self._last_allocation_position >= size

    def allocate(self, data):
        memory_location = self._last_allocation_position
        for i in range(0 , len(data)):
            HARDWARE.memory.write(memory_location + i, data[i])
        self._last_allocation_position += len(data)
        return memory_location