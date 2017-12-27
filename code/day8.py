def collect_variables(instructions):
    variables = {}
    for i in instructions:
        variables[re.match(r"^[a-z]+", i).group(0)] = 0
    return variables


def read_instruction(instruction):
    # split instruction into parts
    i_split = instruction.split(" ")

    # store each part of the instruction
    var = i_split[0]
    mod = i_split[1]
    val = i_split[2]
    d_var = i_split[4]
    conditional = i_split[5]
    mod_val = i_split[6]

    if var not in variables.keys() or d_var not in variables.keys():
        return None




def carry_out_instructions(instructions):
