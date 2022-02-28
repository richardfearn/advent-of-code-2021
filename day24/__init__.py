ALL_VARIABLES = W, X, Y, Z = "w", "x", "y", "z"

INSTRUCTION_4_CONSTANTS = [1, 1, 1, 26, 1, 1, 26, 1, 26, 1, 26, 26, 26, 26]
INSTRUCTION_5_CONSTANTS = [11, 12, 10, -8, 15, 15, -11, 10, -3, 15, -3, -1, -10, -16]
INSTRUCTION_15_CONSTANTS = [8, 8, 12, 10, 2, 8, 4, 9, 10, 3, 7, 7, 2, 2]

DIGITS_ASCENDING = range(1, 10)
DIGITS_DESCENDING = range(9, 0, -1)


def run_program(lines, inputs):
    variables = {var: 0 for var in ALL_VARIABLES}

    for line in lines:
        line = line.split(" ")
        instruction = line[0]
        args = line[1:]

        if instruction == "inp":
            var = args[0]
            variables[var] = inputs.pop(0)

        elif instruction == "add":
            a, b = args
            a_val = variables[a]
            b_val = variables[b] if (b in ALL_VARIABLES) else int(b)
            variables[a] = a_val + b_val

        elif instruction == "mul":
            a, b = args
            a_val = variables[a]
            b_val = variables[b] if (b in ALL_VARIABLES) else int(b)
            variables[a] = a_val * b_val

        elif instruction == "div":
            a, b = args
            a_val = variables[a]
            b_val = variables[b] if (b in ALL_VARIABLES) else int(b)
            variables[a] = a_val // b_val

        elif instruction == "mod":
            a, b = args
            a_val = variables[a]
            b_val = variables[b] if (b in ALL_VARIABLES) else int(b)
            variables[a] = a_val % b_val

        elif instruction == "eql":
            a, b = args
            a_val = variables[a]
            b_val = variables[b] if (b in ALL_VARIABLES) else int(b)
            variables[a] = 1 if (a_val == b_val) else 0

        else:
            raise Exception("Unknown instruction: " + instruction)

    return variables


def monad_interpreted(lines, model_number):
    digits = [int(n) for n in str(model_number)]
    return run_program(lines, digits)[Z]


def monad_hand_coded(model_number):
    digits = [int(n) for n in str(model_number)]
    z = 0
    for step, digit in enumerate(digits):
        z = monad_hand_coded_one_step(step, z, digit)
    return z


def monad_hand_coded_one_step(step, z, w):
    # Instruction 0:
    #   inp w

    # Instructions 1-3:
    #   mul x 0
    #   add x z
    #   mod x 26
    x = z % 26

    # Instruction 4:
    #   div z <1 or 26>
    z = z // INSTRUCTION_4_CONSTANTS[step]

    # Instruction 5:
    #   add x <constant>
    x += INSTRUCTION_5_CONSTANTS[step]

    # Instructions 6-17:
    #   eql x w
    #   eql x 0
    #   mul y 0
    #   add y 25
    #   mul y x
    #   add y 1
    #   mul z y
    #   mul y 0
    #   add y w
    #   add y <constant>
    #   mul y x
    #   add z y
    if x != w:
        z = (26 * z) + (w + INSTRUCTION_15_CONSTANTS[step])

    return z


def part_1_answer():
    return search(DIGITS_ASCENDING)


def part_2_answer():
    return search(DIGITS_DESCENDING)


def search(digits):
    states = {0: [(0, 0, 0)]}
    for step in range(1, 15):
        print("Step %d" % step)
        prev_states = states.pop(step - 1)
        new_states = {}
        print("  generating new states from %d previous states" % len(prev_states))
        for (_, prev_num, prev_z_after) in prev_states:
            for d in digits:
                new_num = prev_num * 10 + d
                new_z = monad_hand_coded_one_step(step - 1, prev_z_after, d)
                new_states[new_z] = (prev_z_after, new_num, new_z)
        states[step] = list(new_states.values())

    for (_, num, z) in states[14]:
        if z == 0:
            return num

    return None
