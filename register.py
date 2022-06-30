class Register:
    def __init__(self, num_of_bits):
        self.__num_of_bits = num_of_bits
        self.__register = [0] * self.__num_of_bits

    def ld(self, reg):
        self.__register = reg