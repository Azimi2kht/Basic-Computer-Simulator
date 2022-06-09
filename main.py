import assembler

# read the assembly code
file = open('assembly.asm', 'r')
code = file.read()
instruction_list = code.splitlines()

# assemble
a = assembler.Assembler()
a.assemble(instruction_list)

# printing the result
for line in instruction_list:
    print(line.replace(' ', ''))
