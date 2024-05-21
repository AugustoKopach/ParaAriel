
from operating_system.scheduling.non_preemptive.non_preemptive_scheduler import NonPreemptiveSchedulerAlgorithm
from utilities.queue import Queue

class FCFSSchedulingAlgorithm(NonPreemptiveSchedulerAlgorithm):
    def __init__(self, kernel, quantum):
        super().__init__(kernel, quantum)
        self.ready_queue = Queue()  # Queue of ready processes

    

    @property
    def next_process_id(self):
        """
        Returns the next process ID to execute.
        """
        return self.ready_queue.front
            

    def move_to_ready(self, pid, pcb):
        """ Move a process with the given PID to the ready state. """
        self.ready_queue.enqueue(pid)

    def move_to_running(self, pid, pcb):
        """ Move a process with the given PID to the running state. """
        self.ready_queue.dequeue()

    def move_to_waiting(self, pid, pcb):
       pass

    def move_to_terminated(self, pid, pcb):
       pass

    # TODO (1) Complete the classe