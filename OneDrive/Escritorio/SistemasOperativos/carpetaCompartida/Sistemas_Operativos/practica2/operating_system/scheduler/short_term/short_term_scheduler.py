class short_term_scheduler:
    def __init__(self):
        self.ready_queue = []

    def schedule(self, ready_queue):
        if ready_queue:
            return ready_queue.pop(0) # returns the first process queued
        else:
            # if  the ready queue is empty, there are no processes to run
            return None