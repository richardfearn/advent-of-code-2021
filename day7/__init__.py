def part_1_answer(positions):
    return find_minimum_fuel(positions, part_1_cost)


def part_1_cost(n):
    return n


def part_2_answer(positions):
    return find_minimum_fuel(positions, part_2_cost)


def part_2_cost(n):
    return n * (n + 1) // 2


def find_minimum_fuel(positions, cost_fn):
    positions = [int(p) for p in positions.split(",")]
    return min(
        total_fuel(positions, align_pos, cost_fn)
        for align_pos in range(min(positions), max(positions) + 1))


def total_fuel(positions, align_pos, cost_fn):
    return sum(
        cost_fn(abs(crab_start_pos - align_pos))
        for crab_start_pos in positions)
