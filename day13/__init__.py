import utils


def part_1_answer(lines):
    dots, folds = parse_input(lines)
    dots = do_folds(dots, folds[:1])
    return len(dots)


def do_folds(dots, folds):
    for fold in folds:
        new_dots = set()

        if fold[0] == "x":
            fold_x = fold[1]
            for dot in dots:
                x, y = dot
                if x > fold_x:
                    x = fold_x - (x - fold_x)
                new_dots.add((x, y))

        elif fold[0] == "y":
            fold_y = fold[1]
            for dot in dots:
                x, y = dot
                if y > fold_y:
                    y = fold_y - (y - fold_y)
                new_dots.add((x, y))

        dots = new_dots

    return dots


def part_2_answer(lines):
    dots, folds = parse_input(lines)
    dots = do_folds(dots, folds)
    return to_text(dots)


def to_text(dots):
    width = max(d[0] for d in dots) + 1
    height = max(d[1] for d in dots) + 1
    grid = [["#" if (x, y) in dots else "." for x in range(width)] for y in range(height)]
    return "\n".join("".join(row) for row in grid)


def parse_input(lines):
    dots, folds = utils.group_lines(lines)  # pylint: disable=unbalanced-tuple-unpacking

    dots = [d.split(",") for d in dots]
    dots = [(int(d[0]), int(d[1])) for d in dots]

    folds = [f.split(" ")[2] for f in folds]
    folds = [f.split("=") for f in folds]
    folds = [(f[0], int(f[1])) for f in folds]

    return dots, folds
