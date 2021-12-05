def part_1_answer(commands):
    commands = [parse_command(c) for c in commands]

    horizontal_pos = 0
    depth = 0

    for direction, x in commands:
        if direction == "forward":
            horizontal_pos += x
        elif direction == "down":
            depth += x
        elif direction == "up":
            depth -= x

    return horizontal_pos * depth


def part_2_answer(commands):
    commands = [parse_command(c) for c in commands]

    horizontal_pos = 0
    depth = 0
    aim = 0

    for direction, x in commands:
        if direction == "down":
            aim += x
        elif direction == "up":
            aim -= x
        elif direction == "forward":
            horizontal_pos += x
            depth += aim * x

    return horizontal_pos * depth


def parse_command(command):
    direction, units = command.split(" ")
    return direction, int(units)
