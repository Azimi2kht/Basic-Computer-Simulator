# TODO: handle the cases where a non-memory reference instruction is used with indirect


def decimal_to_binary(num: int, width: int):
    if num < 0:
        # convert to binary first
        pos_binary = bin(abs(num))[2:].zfill(width)

        # flip the bits after the first one found.
        num_of_bits = len(pos_binary)
        temp_list = list(pos_binary)
        index = num_of_bits - 1
        flag = False
        while index >= 0:
            if temp_list[index] == '1' and not flag:
                flag = True
                index -= 1
                continue
            if flag:
                if temp_list[index] == '1':
                    temp_list[index] = '0'
                else:
                    temp_list[index] = '1'
            index -= 1
        return ''.join(temp_list)
    return bin(num)[2:].zfill(width)


class Assembler:
    def __init__(self):
        self.instructions = {
            # memory reference
            'AND': '0000',
            'ADD': '0001',
            'LDA': '0010',
            'STA': '0011',
            'BUN': '0100',
            'BSA': '0101',
            'ISZ': '0110',

            'ANDI': '1000',
            'ADDI': '1001',
            'LDAI': '1010',
            'STAI': '1011',
            'BUNI': '1100',
            'BSAI': '1101',
            'ISZI': '1110',

            # register reference
            'CLA': '0111 100000000000',
            'CLE': '0111 010000000000',
            'CMA': '0111 001000000000',
            'CME': '0111 000100000000',
            'CIR': '0111 000010000000',
            'CIL': '0111 000001000000',
            'INC': '0111 000000100000',
            'SPA': '0111 000000010000',
            'SNA': '0111 000000001000',
            'SZA': '0111 000000000100',
            'SZE': '0111 000000000010',
            'HLT': '0111 000000000001',

            # I/O reference
            'INP': '1111 100000000000',
            'OUT': '1111 010000000000',
            'SKI': '1111 001000000000',
            'SKO': '1111 000100000000',
            'ION': '1111 000010000000',
            'IOF': '1111 000001000000',
        }
        self.variableTable = {}
        self.scale = 16

    def assemble(self, instruction_list: list):
        # first time reading
        line_counter = 0
        index = 0
        while index < len(instruction_list):
            instruction_list[index] = single_spaced = ' '.join(instruction_list[index].split())
            if 'ORG' in instruction_list[index]:
                line_counter = int(single_spaced[3:])
                # remove the line
                instruction_list.pop(index)
                index -= 1
            elif ' I' in instruction_list[index]:
                if ',' in instruction_list[index]:
                    self.variableTable[line_counter] = single_spaced[0:single_spaced.find(',')]
                instruction = instruction_list[index][
                              instruction_list[index].find(',') + 1: instruction_list[index].find(' ')]
                instruction_list[index] = instruction_list[index].replace(instruction,
                                                                          self.instructions[instruction + 'I'])
                instruction_list[index] = instruction_list[index][
                                          instruction_list[index].find(',') + 1:]
                instruction_list[index] = instruction_list[index].replace('I', '')

            elif ',' in instruction_list[index] or 'HEX' in instruction_list[index] or 'DEC' in \
                    instruction_list[
                        index]:
                self.variableTable[line_counter] = single_spaced[0:single_spaced.find(',')]
                temp_list = []
                # find number in line:
                for t in instruction_list[index].split():
                    try:
                        temp_list.append(str(int(t)))
                    except ValueError:
                        pass
                num = ''.join(temp_list)

                if 'HEX' in instruction_list[index]:
                    binary = decimal_to_binary(int(num, 16), self.scale)
                    instruction_list[index] = binary
                else:
                    binary = decimal_to_binary(int(num), self.scale)
                    instruction_list[index] = binary

            elif 'END' in instruction_list[index]:
                # remove the line
                instruction_list.pop(index)
                index -= 1
                break
            else:
                instruction = instruction_list[index][0:3]
                if instruction in self.instructions:
                    instruction_list[index] = instruction_list[index].replace(instruction,
                                                                              self.instructions[instruction])
                else:
                    raise Exception('Not a valid instruction at line:', index)
            index += 1
            line_counter += 1
        # second time reading
        for index in range(len(instruction_list)):
            if len(instruction_list[index].split()) > 1:
                try:
                    hex_address = list(self.variableTable.keys())[
                        list(self.variableTable.values()).index(instruction_list[index].split()[1])]
                    binary_address = bin(int(str(hex_address), self.scale))[2:].zfill(12)
                    instruction_list[index] = instruction_list[index].replace(
                        instruction_list[index].split()[1], str(binary_address))
                except ValueError:
                    pass
        pass
