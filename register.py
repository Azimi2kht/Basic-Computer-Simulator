class Register:
    def __init__(self, num_of_bits):
        self.__num_of_bits = num_of_bits
        self.__register = [0] * self.__num_of_bits

    def clr(self):
        self.__register = [0] * self.__num_of_bits

    def inr(self):
        binary = list(bin(int(''.join(map(str, self.__register)), 2) + 1)[2:].zfill(self.__num_of_bits))
        self.__register = binary
