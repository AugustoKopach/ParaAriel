class InterruptVector():
    """
        Simulates the interruption vector.
        The interruption vector is a table that associates an interruption name/code,
        to a given handler. The vector allows to register new handlers for an
        interruption, and to handle such interruption by the associated handler
        when the interruption in thrown.
    """
    def __init__(self):
        self._handlers = {}

    def register(self, irqCode, interruptionHandler):
        """ Register a new interruption to the interruptor vector. """
        self._handlers[irqCode] = interruptionHandler

    def handle(self, irq):
        """ Handle an interruption with the registered handlers in the vector. """
        if irq.code in self._handlers:
            self._handlers[irq.code].execute(irq)
