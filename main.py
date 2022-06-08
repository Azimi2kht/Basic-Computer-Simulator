import re


# TODO: handle the cases where a non-memory reference instruction is used with indirect
def decimal_to_binary(num: int, width: int):
    if num >= 0:
        return bin(num)[2:].zfill(width)
    else:
        # convert to binary first
        pos_binary = bin(abs(num))[2:].zfill(width)

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


instructions = {
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
variableTable = {}

# read the assembly code
file = open('assembly.txt', 'r')
content = file.read()
lines = content.splitlines()

lineCounter = 0
scale = 16

# first time reading:
index = 0
while index < len(lines):
    lines[index] = onlyOneSpace = ' '.join(lines[index].split())
    if 'ORG' in lines[index]:
        lineCounter = int(onlyOneSpace[3:])
        # remove the line
        lines.pop(index)
        index -= 1
    elif ' I' in lines[index]:
        if ',' in lines[index]:
            variableTable[lineCounter] = onlyOneSpace[0:onlyOneSpace.find(',')]
        instruction = lines[index][lines[index].find(',') + 1: lines[index].find(' ')]
        lines[index] = lines[index].replace(instruction, instructions[instruction + 'I'])
        lines[index] = lines[index][lines[index].find(',') + 1:]
        lines[index] = lines[index].replace('I', '')

    elif ',' in lines[index] or 'HEX' in lines[index] or 'DEC' in lines[index]:
        variableTable[lineCounter] = onlyOneSpace[0:onlyOneSpace.find(',')]
        l = []
        # find number in line:
        for t in lines[index].split():
            try:
                l.append(str(int(t)))
            except ValueError:
                pass
        num = ''.join(l)

        if 'HEX' in lines[index]:
            decimal = int(num, 16)
            binary = bin(decimal)[2:0].zfill(16)
            lines[index] = binary
        else:
            binary = decimal_to_binary(int(num), 16)
            lines[index] = binary

    elif 'END' in lines[index]:
        # remove the line
        lines.pop(index)
        index -= 1
        break
    else:
        instruction = lines[index][0:3]
        if instruction in instructions:
            lines[index] = lines[index].replace(instruction, instructions[instruction])

    index += 1
    lineCounter += 1

# second time reading:
for index in range(len(lines)):
    if len(lines[index].split()) > 1:
        try:
            hexAddress = list(variableTable.keys())[list(variableTable.values()).index(lines[index].split()[1])]
            binaryAddress = bin(int(str(hexAddress), scale))[2:].zfill(12)
            lines[index] = lines[index].replace(lines[index].split()[1], str(
                binaryAddress))
        except ValueError:
            pass

# printing the result
for line in lines:
    print(line.replace(' ', ''))
