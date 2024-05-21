#!/usr/bin/env python3
from time import sleep
from hardware.hardware import HARDWARE
from hardware.asm import ASM

from utilities.compiler import Compiler

from os.kernel import Kernel

if __name__ == '__main__':
    HARDWARE.setup(10)

    program1 = Compiler.compile('mi programa', [
        ASM.CPU(1),
        ASM.IO(1),
        ASM.CPU(3)
    ])

    os = Kernel()
    os.load_program(program1)

    # Esto no se hace acá
    # for i in range(0, len(program1.instructions)):
    #    HARDWARE.memory.write(i, program1.instructions[i])

    HARDWARE.cpu.pc = 0
    for i in range(0, 100):
        HARDWARE.cpu.tick(i)
        print(HARDWARE)
        sleep(1)