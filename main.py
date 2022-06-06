file = open('assembly.txt', 'r')
content = file.read()

lines = content.splitlines()

instructions = {
    # memory reference
    'AND': '0000',
    'ADD': '0001',
    'LDA': '0010',
    'STA': '0011',
    'BUN': '0100',
    'BSA': '0101',
    'ISZ': '0110',

    # register reference
    'CLA': '0111',
    'CLE': '0111',
    'CMA': '0111',
    'CME': '0111',
    'CIR': '0111',
    'CIL': '0111',
    'INC': '0111',
    'SPA': '0111',
    'SNA': '0111',
    'SZA': '0111',
    'SZE': '0111',
    'HLT': '0111',

    # I/O reference
    'INP': '1111',
    'OUT': '1111',
    'SKI': '1111',
    'SKO': '1111',
    'ION': '1111',
    'IOF': '1111',
}

for line in lines:
    if ',' in line:
        pass

