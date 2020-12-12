import operator
ops = { "+": operator.add, "-": operator.sub }

instructions = [x.replace('\n', '')for x in open("input.txt").readlines()]

def execute_instruction(instruction: str, arg: str, accum: int, line: int) -> (int, int):
    if instruction == 'acc':
        return (ops[arg[0]](accum, int(arg[1:])), line+1)
    if instruction == 'jmp':
        return (accum, ops[arg[0]](line, int(arg[1:])))
    return (accum, line+1)

def read_instructions(instructions: [str]):
    line = 0
    accum = 0
    lines_already_read = []
    while line not in lines_already_read:
        instruction,arg = instructions[line].split(' ')
        lines_already_read.append(line)
        print(f"instruction: {instruction}, arg: {arg}")
        accum,line = execute_instruction(instruction, arg, accum, line)
        print(f"accum: {accum}, line: {line}")
    return accum

print(read_instructions(instructions))
