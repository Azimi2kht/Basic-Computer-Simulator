from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.http import HttpResponse
# Create your views here.


def assembler(lines):
    # TODO: handle the cases where a non-memory reference instruction is used with indirect
    instructions = {
        # memory reference
        'AND': '0000',
        'ADD': '0001',
        'LDA': '0010',
        'STA': '0011',
        'BUN': '0100',
        'BSA': '0101',
        'ISZ': '0110',

        'AND I': '1000',
        'ADD I': '1001',
        'LDA I': '1010',
        'STA I': '1011',
        'BUN I': '1100',
        'BSA I': '1101',
        'ISZ I': '1110',

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
    variableTable = {}

    # read the assembly code
    # file = open('assembly.txt', 'r')
    # content = file.read()
    lineCounter = 0
    flag = True

    # first time reading:
    index = 0
    while index < len(lines):
        lines[index] = onlyOneSpace = ' '.join(lines[index].split())
        if 'ORG' in lines[index]:
            lineCounter = int(onlyOneSpace[3:])
            # delete the line
            lines.pop(index)
            index -= 1
        elif ',' in lines[index]:
            variableTable[lineCounter] = onlyOneSpace[0:onlyOneSpace.find(
                ',')]
            # delete the line
            lines.pop(index)
            index -= 1
        elif 'END' in lines[index]:
            # delete the line
            lines.pop(index)
            index -= 1
            break
        else:
            instruction = lines[index][0:3]
            if instruction in instructions:
                lines[index] = lines[index].replace(
                    instruction, instructions[instruction])
        index += 1
        lineCounter += 1

    # second time reading:
    for index in range(len(lines)):
        if len(lines[index].split()) > 1:
            lines[index] = lines[index].replace(lines[index].split()[1], str(list(
                variableTable.keys())[list(variableTable.values()).index(lines[index].split()[1])]))

    return lines
    # printing the result
    # for line in lines:
    #     print(line)


class InputAssembler(View):
    form_class = forms.InputAssembler
    template_name = 'input_assembler.html'
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            lines = assembler(form.cleaned_data['input'].splitlines())
            return redirect('assembler:output_assembler', lines)


class OutputAssembler(View):
    form_class = forms.InputAssembler
    template_name = 'output_assembler.html'

    def get(self, request, *args, **kwargs):
        text = ' '
        for line in kwargs['lines'].split(','):
            line = line.replace("'", "")
            line = line.replace("[", "")
            line = line.replace("]", "")
            line = line.replace(" ", "")
            text += line + '\n\n'
            print(line)

        form = self.form_class(initial={'input':text})
        return render(request, self.template_name, {'form': form})
