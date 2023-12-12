from utils import parse_fname, read_input


def parse_input(input_str):
    instrs = [
        (instr.split(" ")[0], int(instr.split(" ")[1]))
        for instr in input_str.split("\n") if instr != ""
    ]
    return instrs


def clean_up_code(instrs, acc_log, call_log):
    """Finds the instruction in a list of instructions that induces an infinite loop,
    fixes it, and performs the rest of the instructions

    Args:
        - instrs (list(str)): list of instructions to be performed
        - acc_log (list(int)): list of incremental values of accelerator values
        - call_log (list(int)): list of call positions

    Returns an int
    """
    for acc, idx in zip(acc_log[::-1], call_log[::-1]):
        instrs_mod = instrs.copy()
        last_instr, val = instrs[idx]
        if last_instr in ("jmp", "nop"):
            instrs_mod[idx] = ("nop" if last_instr == "jmp" else "jmp", val)
            temp_acc_log, temp_call_log, last_idx = run_boot_code(
                instrs_mod,
                starting_acc=acc,
                starting_idx=idx
            )
            acc = temp_acc_log[-1]
        if last_idx >= len(instrs):
            return acc


def run_boot_code(instrs, starting_acc=0, starting_idx=0):
    """Performs a series of instructions until an instruction is repeated or the
    instructon to be performed does not exist

    Args:
        - instrs (list(str)): list of instructions to be performed
        - starting_acc (int): the starting value of the accelerator which is
            incremented by certain instructions
        - starting_idx (int): zero-index position to start performing instructions
            from

    Returns two lists, the first is a log of the incremental values of the accelerator
    and the second is a log of all called instructions in the order they were called
    """
    acc = starting_acc
    idx = starting_idx
    acc_log = []
    call_log = []
    counts = [0 for _ in range(len(instrs))]
    while idx < len(instrs):
        counts[idx] += 1
        if max(counts) > 1:
            break
        instr, val = instrs[idx]
        if instr == "acc":
            acc += val
            idx += 1
        elif instr == "jmp":
            idx += val
        elif instr == "nop":
            idx += 1
        acc_log.append(acc)
        call_log.append(idx)
    return acc_log, call_log, idx


def main():
    input_str = read_input(*parse_fname(__file__))
    instrs = parse_input(input_str)

    acc_log, call_log, _ = run_boot_code(instrs)
    print(call_log)
    print("PART 1")
    print("Accelerator value after 1 loop: %i" % acc_log[-1])
    print()

    acc = clean_up_code(instrs, acc_log, call_log)
    print("PART 2")
    if acc is None:
        print("No solution found")
    else:
        print("Accelerator value after program ends: %i" % acc)


if __name__ == '__main__':
    main()
