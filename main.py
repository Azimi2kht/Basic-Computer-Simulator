import assembler

# read the assembly code
file = open('assembly.asm', 'r')
code = file.read()
instruction_list = code.splitlines()

# assemble
a = assembler.Assembler()
assembly_list = a.assemble(instruction_list)

# printing the result
Ram = []
for line in assembly_list:
    Ram.append([line[0], line[1:4], line[5:]])

for line in Ram:
    print(line)
