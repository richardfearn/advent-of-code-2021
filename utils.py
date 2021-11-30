from pathlib import Path


def read_input_lines(day):
    with day_path(day).open() as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    return lines


def read_input(day):
    with day_path(day).open() as file:
        text = file.read()
    return text.rstrip()


def day_path(day):
    return Path(__file__).parent / f"day{day}" / "input.txt"


def group_lines(lines):
    if isinstance(lines, str):
        lines = lines.strip().split("\n")

    groups = [[]]

    for line in lines:
        if line == "":
            groups.append([])
        else:
            groups[-1].append(line)

    return groups


def to_lines(text):
    return text.strip().split("\n")
