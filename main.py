import re
# TODO: handle the cases where a non-memory reference instruction is used with indirect
def flip(c):
    return '1' if (c == '0') else '0'


def twos_complement(b):
    n = len(b)
    ones = ""
    twos = ""

    # for ones complement flip every bit
    for i in range(n):
        ones += flip(b[i])

    # for two's complement go from right
    # to left in ones complement and if
    # we get 1 make, we make them 0 and
    # keep going left when we get first
    # 0, make that 1 and go out of loop
    ones = list(ones.strip(""))
    twos = list(ones)
    for i in range(n - 1, -1, -1):

        if ones[i] == '1':
            twos[i] = '0'
        else:
            twos[i] = '1'
            break

    i -= 1
    # If No break : all are 1 as in 111 or 11111
    # in such case, add extra 1 at beginning
    if i == -1:
        twos.insert(0, '1')
    return ''.join(twos)


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
            if int(num) >= 0:
                binary = bin(int(num))[2:].zfill(16)
            else:
                binary = twos_complement(bin(abs(int(num)))).zfill(16)
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
    print(line.replace(' ',''))
