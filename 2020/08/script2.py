import operator
ops = { "+": operator.add, "-": operator.sub }

instructions = [x.replace('\n', '') for x in open("input.txt").readlines()]

def execute_instruction(instruction: str, arg: str, accum: int, line: int) -> (int, int):
    if instruction == 'acc':
        return (ops[arg[0]](accum, int(arg[1:])), line+1)
    if instruction == 'jmp':
        return (accum, ops[arg[0]](line, int(arg[1:])))
    return (accum, line+1)

def run_code(instructions: [str]):
    line = 0
    accum = 0
    lines_already_read = []
    while line not in lines_already_read and line < len(instructions):
        instruction,arg = instructions[line].split(' ')
        lines_already_read.append(line)
        accum,line = execute_instruction(instruction, arg, accum, line)

    return (accum, line)

def solve():
    last_line = len(instructions)
    print(f"last line: {last_line}")
    for index,instruction in enumerate(instructions):
        instructions_copy = instructions.copy()
        accum,line = run_code(instructions_copy)
        if line == last_line:
            print(f"accum: {accum}")
            break
        op,arg = instruction.split(' ')
        if op == 'jmp':
            instructions_copy[index] = 'nop' + ' ' + arg
        elif op == 'nop':
            instructions_copy[index] = 'jmp' + ' ' + arg
        accum,line = run_code(instructions_copy)
        if line == last_line:
            print(f"line: {line}")
            print(f"accum: {accum}")
            break

solve()
