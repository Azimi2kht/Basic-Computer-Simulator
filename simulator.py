from register import Register
from register_clr_inr import RegisterClearIncrement


class Simulator:
    def __init__(self):
        self.ar = RegisterClearIncrement(12)
        self.pc = RegisterClearIncrement(12)
        self.dr = RegisterClearIncrement(16)
        self.ac = RegisterClearIncrement(16)
        self.inpr = Register(8)
        self.ir = Register(16)
        self.tr = RegisterClearIncrement(16)
        self.outr = Register(8)


