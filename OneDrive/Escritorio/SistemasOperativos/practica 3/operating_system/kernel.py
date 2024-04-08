from hardware.hardware import HARDWARE
from operating_system.scheduler.long_term_scheduler.longTermScheduler import LongTermScheduler
from utilities.printer import Printer

class Kernel:
    """Models the kernel of the OS"""
    def __init__(self):
        self._process_table = {}
        self._long_term_scheduler = LongTermScheduler(self, self._process_table)
        # This strategy is useful for now, but later on it will not work
        self._last_allocated_position = 0

       # HARDWARE.interrupt_vector.register(KILL_IRQ, KillInterruptionHandler(self))


    def create_process(self, program):
        # Delegate the task
        self._long_term_scheduler.create_process(program)

    def kill_process(self, pid):
        self._long_term_scheduler.kill_process(pid)
     

    def has_free_memory(self, size):
        return HARDWARE.memory.size - self._last_allocated_position >= size

    def allocate(self, data):
        # PREC there is enough free memory
        memory_location = self._last_allocated_position
        for i in range(0, len(data)):
            HARDWARE.memory.write(memory_location + i, data[i])
        self._last_allocated_position += len(data)
        return memory_location

    def free(self, pos):
        HARDWARE.memory.write(pos, '')

    def __repr__(self):
        os_config = Printer.tabulated([["No configuration yet"]],
                                    headers=["Configuration"])

        
        processes = []
        processes_added = 0
        proc_columns = 3

        for _, pcb in self._process_table.items():
            if (processes_added % proc_columns == 0):
                processes.append([])
            processes[-1].append(pcb)
            processes_added += 1

        # Now we can use out list
        os_proctable = Printer.tabulated(processes,
                                    headers=["Process Table", "--", "--"])
        return os_config + "\n\n" + os_proctable